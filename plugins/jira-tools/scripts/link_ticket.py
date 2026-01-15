#!/usr/bin/env python3
"""
Jira Ticket Linking Script

Links Jira tickets together using direct REST API calls.
Uses API token authentication from environment variables.

Requirements:
    - ATLASSIAN_EMAIL environment variable
    - ATLASSIAN_API_TOKEN environment variable
    - ATLASSIAN_SITE environment variable (default: yoursite.atlassian.net)

Usage:
    python link_ticket.py --list-types                    # List available link types
    python link_ticket.py PROJ-123 --list                 # Show existing links
    python link_ticket.py PROJ-123 PROJ-456 "Blocks"      # Create a link
    python link_ticket.py PROJ-123 --remove 12345         # Remove a link
"""

import os
import sys
import json
import base64
import argparse
from typing import Dict, List, Optional, Tuple
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


class JiraLinker:
    """Handle Jira ticket linking using REST API."""

    def __init__(self, email: str, api_token: str, site: str):
        """
        Initialize the Jira linker.

        Args:
            email: Atlassian account email
            api_token: API token from Atlassian
            site: Jira site hostname (e.g., yoursite.atlassian.net)
        """
        self.email = email
        self.api_token = api_token
        self.site = site.replace("https://", "").replace("http://", "")
        self.base_url = f"https://{self.site}/rest/api/3"

        # Create auth header
        auth_string = f"{self.email}:{self.api_token}"
        auth_bytes = auth_string.encode("ascii")
        base64_bytes = base64.b64encode(auth_bytes)
        self.auth_header = f"Basic {base64_bytes.decode('ascii')}"

    def _make_request(
        self, url: str, method: str = "GET", data: Optional[Dict] = None
    ) -> Dict:
        """
        Make an authenticated request to Jira API.

        Args:
            url: Full URL to request
            method: HTTP method (GET, POST, DELETE)
            data: Optional JSON data for POST requests

        Returns:
            JSON response as dictionary

        Raises:
            Exception: If request fails
        """
        headers = {
            "Authorization": self.auth_header,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        request = Request(url, headers=headers, method=method)

        if data:
            request.data = json.dumps(data).encode("utf-8")

        try:
            with urlopen(request) as response:
                if response.status == 204:  # No content (success)
                    return {}
                body = response.read().decode("utf-8")
                if not body:
                    return {}
                return json.loads(body)
        except HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_json = json.loads(error_body)
                error_msg = error_json.get("errorMessages", [str(e)])[0]
            except:
                error_msg = str(e)
            raise Exception(f"HTTP {e.code}: {error_msg}") from e

    def get_link_types(self) -> List[Dict]:
        """
        Get all available issue link types.

        Returns:
            List of link type objects with id, name, inward, outward
        """
        url = f"{self.base_url}/issueLinkType"
        response = self._make_request(url)
        return response.get("issueLinkTypes", [])

    def find_link_type(self, name: str) -> Optional[Dict]:
        """
        Find a link type by name (case-insensitive, supports partial match).

        Args:
            name: Link type name to search for

        Returns:
            Link type object or None if not found
        """
        link_types = self.get_link_types()
        name_lower = name.lower()

        # Try exact match first
        for lt in link_types:
            if lt["name"].lower() == name_lower:
                return lt

        # Try partial match
        for lt in link_types:
            if name_lower in lt["name"].lower():
                return lt

        # Try matching inward/outward labels
        for lt in link_types:
            if name_lower in lt["inward"].lower() or name_lower in lt["outward"].lower():
                return lt

        return None

    def get_ticket(self, issue_key: str) -> Dict:
        """
        Get ticket details including issue links.

        Args:
            issue_key: Jira ticket key (e.g., PROJ-123)

        Returns:
            Ticket data
        """
        url = f"{self.base_url}/issue/{issue_key}?fields=summary,status,issuelinks"
        return self._make_request(url)

    def get_issue_links(self, issue_key: str) -> List[Dict]:
        """
        Get all links for a ticket.

        Args:
            issue_key: Jira ticket key (e.g., PROJ-123)

        Returns:
            List of issue link objects
        """
        ticket = self.get_ticket(issue_key)
        return ticket.get("fields", {}).get("issuelinks", [])

    def create_link(
        self,
        source_key: str,
        target_key: str,
        link_type_name: str,
        comment: Optional[str] = None,
    ) -> None:
        """
        Create a link between two issues.

        For "Blocks" link type: source_key blocks target_key
        NOTE: The Jira UI displays links opposite from API semantics, so we
        swap inward/outward to make the UI show the relationship correctly.
        - source_key becomes inwardIssue (so UI shows it as the blocker)
        - target_key becomes outwardIssue (so UI shows it as blocked)

        Args:
            source_key: The source issue key (does the action, e.g., "blocks")
            target_key: The target issue key (receives the action, e.g., "is blocked by")
            link_type_name: Name of the link type (e.g., "Blocks")
            comment: Optional comment to add to the target issue

        Raises:
            Exception: If link creation fails
        """
        url = f"{self.base_url}/issueLink"

        # NOTE: Swapped inward/outward to compensate for Jira UI displaying backwards
        data = {
            "type": {"name": link_type_name},
            "outwardIssue": {"key": target_key},
            "inwardIssue": {"key": source_key},
        }

        if comment:
            data["comment"] = {"body": comment}

        self._make_request(url, method="POST", data=data)

    def delete_link(self, link_id: str) -> None:
        """
        Delete an issue link.

        Args:
            link_id: The ID of the link to delete

        Raises:
            Exception: If deletion fails
        """
        url = f"{self.base_url}/issueLink/{link_id}"
        self._make_request(url, method="DELETE")

    def list_link_types(self) -> None:
        """Print available link types."""
        try:
            link_types = self.get_link_types()

            print("\nAvailable Link Types:")
            print("=" * 60)

            if not link_types:
                print("  (No link types available)")
                return

            for lt in link_types:
                print(f"\n  {lt['name']} (ID: {lt['id']})")
                print(f"    Outward: \"{lt['outward']}\"")
                print(f"    Inward:  \"{lt['inward']}\"")

            print("\n" + "=" * 60)
            print("Usage: link_ticket.py SOURCE TARGET \"Link Type Name\"")
            print("Example: link_ticket.py PROJ-123 PROJ-456 \"Blocks\"")
            print("         (PROJ-123 blocks PROJ-456)")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def list_issue_links(self, issue_key: str) -> None:
        """
        Print existing links for a ticket.

        Args:
            issue_key: Jira ticket key
        """
        try:
            ticket = self.get_ticket(issue_key)
            summary = ticket["fields"]["summary"]
            links = ticket["fields"].get("issuelinks", [])

            print(f"\n{issue_key}: {summary}")
            print("=" * 60)

            if not links:
                print("  No links found")
                return

            print(f"\nLinks ({len(links)}):")

            for link in links:
                link_type = link["type"]["name"]
                link_id = link["id"]

                # NOTE: Jira UI displays links opposite from API semantics.
                # We swap the labels to match what users see in the Jira UI.
                # - If link contains "outwardIssue", Jira UI shows outward label
                # - If link contains "inwardIssue", Jira UI shows inward label
                if "outwardIssue" in link:
                    direction = link["type"]["outward"]
                    linked_issue = link["outwardIssue"]
                else:
                    direction = link["type"]["inward"]
                    linked_issue = link["inwardIssue"]

                linked_key = linked_issue["key"]
                linked_summary = linked_issue["fields"]["summary"]
                linked_status = linked_issue["fields"]["status"]["name"]

                print(f"\n  [{link_id}] {direction}:")
                print(f"    {linked_key}: {linked_summary}")
                print(f"    Status: {linked_status}")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def execute_link(
        self,
        source_key: str,
        target_key: str,
        link_type_name: str,
        comment: Optional[str] = None,
        dry_run: bool = False,
    ) -> None:
        """
        Create a link between two issues with validation.

        Args:
            source_key: Source issue key (outward issue - "blocks")
            target_key: Target issue key (inward issue - "is blocked by")
            link_type_name: Link type name
            comment: Optional comment
            dry_run: If True, only show what would happen
        """
        try:
            # Validate link type
            link_type = self.find_link_type(link_type_name)
            if not link_type:
                print(f"Error: Unknown link type '{link_type_name}'")
                print("\nUse --list-types to see available link types")
                sys.exit(1)

            # Get ticket info for display
            source_ticket = self.get_ticket(source_key)
            target_ticket = self.get_ticket(target_key)

            source_summary = source_ticket["fields"]["summary"]
            target_summary = target_ticket["fields"]["summary"]

            print(f"\nSource: {source_key}: {source_summary}")
            print(f"Target: {target_key}: {target_summary}")
            print(f"\nLink Type: {link_type['name']}")
            print(f"  {source_key} {link_type['outward']} {target_key}")
            print(f"  {target_key} {link_type['inward']} {source_key}")

            if comment:
                print(f"\nComment: {comment}")

            if dry_run:
                print(f"\nDry run: No changes made")
                return

            # Create the link
            # In Jira's API:
            # - outwardIssue is the source (does the action, e.g., "blocks")
            # - inwardIssue is the target (receives the action, e.g., "is blocked by")
            self.create_link(source_key, target_key, link_type["name"], comment)

            print(f"\nLink created successfully!")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    def execute_remove(self, issue_key: str, link_id: str) -> None:
        """
        Remove a link from an issue.

        Args:
            issue_key: Issue key (for context/display)
            link_id: Link ID to remove
        """
        try:
            # Get current links to verify and display info
            links = self.get_issue_links(issue_key)

            # Find the link
            target_link = None
            for link in links:
                if str(link["id"]) == str(link_id):
                    target_link = link
                    break

            if not target_link:
                print(f"Error: Link ID {link_id} not found on {issue_key}")
                print("\nUse --list to see existing links and their IDs")
                sys.exit(1)

            # Display what we're removing
            # NOTE: Jira UI displays links opposite from API semantics.
            # We swap labels to match what users see in Jira UI.
            link_type = target_link["type"]["name"]
            if "outwardIssue" in target_link:
                direction = target_link["type"]["outward"]
                linked_key = target_link["outwardIssue"]["key"]
            else:
                direction = target_link["type"]["inward"]
                linked_key = target_link["inwardIssue"]["key"]

            print(f"\nRemoving link from {issue_key}:")
            print(f"  Link ID: {link_id}")
            print(f"  Type: {link_type}")
            print(f"  {direction} {linked_key}")

            # Delete the link
            self.delete_link(link_id)

            print(f"\nLink removed successfully!")

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Link Jira tickets together",
        epilog="Example: %(prog)s PROJ-123 PROJ-456 'Blocks'",
    )
    parser.add_argument(
        "source",
        nargs="?",
        help="Source issue key (e.g., PROJ-123)",
    )
    parser.add_argument(
        "target",
        nargs="?",
        help="Target issue key (e.g., PROJ-456)",
    )
    parser.add_argument(
        "link_type",
        nargs="?",
        help="Link type name (e.g., 'Blocks', 'Relates', 'Duplicate')",
    )
    parser.add_argument(
        "--list-types",
        action="store_true",
        help="List available link types",
    )
    parser.add_argument(
        "--list",
        "-l",
        action="store_true",
        help="List existing links for the source issue",
    )
    parser.add_argument(
        "--remove",
        "-r",
        metavar="LINK_ID",
        help="Remove a link by its ID",
    )
    parser.add_argument(
        "--comment",
        "-c",
        help="Add a comment when creating the link (added to target issue)",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Show what would happen without making changes",
    )
    parser.add_argument(
        "--site",
        default=os.getenv("ATLASSIAN_SITE", "yoursite.atlassian.net"),
        help="Atlassian site hostname (default: from ATLASSIAN_SITE env)",
    )

    args = parser.parse_args()

    # Get credentials from environment
    email = os.getenv("ATLASSIAN_EMAIL")
    api_token = os.getenv("ATLASSIAN_API_TOKEN")

    if not email or not api_token:
        print("Error: Missing credentials", file=sys.stderr)
        print("\nRequired environment variables:", file=sys.stderr)
        print("  - ATLASSIAN_EMAIL", file=sys.stderr)
        print("  - ATLASSIAN_API_TOKEN", file=sys.stderr)
        print("\nOptional:", file=sys.stderr)
        print("  - ATLASSIAN_SITE (default: yoursite.atlassian.net)", file=sys.stderr)
        sys.exit(1)

    # Create linker
    linker = JiraLinker(email, api_token, args.site)

    # Execute command
    if args.list_types:
        linker.list_link_types()
    elif args.list:
        if not args.source:
            print("Error: Issue key required with --list", file=sys.stderr)
            sys.exit(1)
        linker.list_issue_links(args.source)
    elif args.remove:
        if not args.source:
            print("Error: Issue key required with --remove", file=sys.stderr)
            sys.exit(1)
        linker.execute_remove(args.source, args.remove)
    else:
        # Create link
        if not args.source or not args.target or not args.link_type:
            print("Error: SOURCE, TARGET, and LINK_TYPE required", file=sys.stderr)
            print("\nUsage: link_ticket.py SOURCE TARGET LINK_TYPE", file=sys.stderr)
            print("       link_ticket.py --list-types", file=sys.stderr)
            print("       link_ticket.py SOURCE --list", file=sys.stderr)
            sys.exit(1)
        linker.execute_link(
            args.source, args.target, args.link_type, args.comment, args.dry_run
        )


if __name__ == "__main__":
    main()
