#!/usr/bin/env python3
"""
Jira Ticket Transition Script

Transitions a Jira ticket to a new status using direct REST API calls.
Uses API token authentication from environment variables.

Requirements:
    - ATLASSIAN_EMAIL environment variable
    - ATLASSIAN_API_TOKEN environment variable
    - ATLASSIAN_SITE environment variable (default: yoursite.atlassian.net)

Usage:
    python transition_ticket.py PROJ-123 "In Progress"
    python transition_ticket.py PROJ-123 "Done"
    python transition_ticket.py PROJ-123 --list  # List available transitions
"""

import os
import sys
import json
import base64
import argparse
from typing import Dict, List, Optional, Tuple
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError


class JiraTransitioner:
    """Handle Jira ticket transitions using REST API."""

    def __init__(self, email: str, api_token: str, site: str):
        """
        Initialize the Jira transitioner.

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
            method: HTTP method (GET, POST, PUT)
            data: Optional JSON data for POST/PUT requests

        Returns:
            JSON response as dictionary

        Raises:
            HTTPError: If request fails
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
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_json = json.loads(error_body)
                error_msg = error_json.get("errorMessages", [str(e)])[0]
            except:
                error_msg = str(e)
            raise Exception(f"HTTP {e.code}: {error_msg}") from e

    def get_ticket(self, issue_key: str) -> Dict:
        """
        Get ticket details.

        Args:
            issue_key: Jira ticket key (e.g., PROJ-123)

        Returns:
            Ticket data
        """
        url = f"{self.base_url}/issue/{issue_key}"
        return self._make_request(url)

    def get_transitions(self, issue_key: str) -> List[Dict]:
        """
        Get available transitions for a ticket.

        Args:
            issue_key: Jira ticket key (e.g., PROJ-123)

        Returns:
            List of available transitions
        """
        url = f"{self.base_url}/issue/{issue_key}/transitions"
        response = self._make_request(url)
        return response.get("transitions", [])

    def find_transition(
        self, issue_key: str, target_status: str
    ) -> Optional[Tuple[str, str]]:
        """
        Find transition ID for a target status.

        Args:
            issue_key: Jira ticket key
            target_status: Desired status name (case-insensitive)

        Returns:
            Tuple of (transition_id, transition_name) or None if not found
        """
        transitions = self.get_transitions(issue_key)
        target_lower = target_status.lower()

        # Try exact match first
        for transition in transitions:
            if transition["name"].lower() == target_lower:
                return (transition["id"], transition["name"])

        # Try partial match
        for transition in transitions:
            if target_lower in transition["name"].lower():
                return (transition["id"], transition["name"])

        return None

    def transition_ticket(
        self, issue_key: str, transition_id: str, fields: Optional[Dict] = None
    ) -> None:
        """
        Execute a ticket transition.

        Args:
            issue_key: Jira ticket key
            transition_id: ID of the transition to execute
            fields: Optional fields to update during transition

        Raises:
            Exception: If transition fails
        """
        url = f"{self.base_url}/issue/{issue_key}/transitions"
        data = {"transition": {"id": transition_id}}

        if fields:
            data["fields"] = fields

        self._make_request(url, method="POST", data=data)

    def list_transitions(self, issue_key: str) -> None:
        """
        Print available transitions for a ticket.

        Args:
            issue_key: Jira ticket key
        """
        try:
            # Get current status
            ticket = self.get_ticket(issue_key)
            current_status = ticket["fields"]["status"]["name"]
            summary = ticket["fields"]["summary"]

            print(f"\n📋 {issue_key}: {summary}")
            print(f"Current Status: {current_status}")
            print("\nAvailable Transitions:")

            transitions = self.get_transitions(issue_key)

            if not transitions:
                print("  (No transitions available)")
                return

            for i, transition in enumerate(transitions, 1):
                to_status = transition.get("to", {}).get("name", "Unknown")
                transition_name = transition["name"]
                print(f"  {i}. {transition_name} → {to_status}")

        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)

    def execute_transition(
        self, issue_key: str, target_status: str, dry_run: bool = False
    ) -> None:
        """
        Find and execute a transition to target status.

        Args:
            issue_key: Jira ticket key
            target_status: Desired status name
            dry_run: If True, only show what would happen

        Raises:
            Exception: If transition fails or not found
        """
        try:
            # Get current ticket info
            ticket = self.get_ticket(issue_key)
            current_status = ticket["fields"]["status"]["name"]
            summary = ticket["fields"]["summary"]

            print(f"\n📋 {issue_key}: {summary}")
            print(f"Current Status: {current_status}")

            # Find transition
            result = self.find_transition(issue_key, target_status)

            if not result:
                print(f"\n❌ Cannot transition to '{target_status}'")
                print("\nAvailable transitions:")
                transitions = self.get_transitions(issue_key)
                for t in transitions:
                    to_status = t.get("to", {}).get("name", "Unknown")
                    print(f"  - {t['name']} → {to_status}")
                sys.exit(1)

            transition_id, transition_name = result
            to_status = None

            # Get the actual target status name
            transitions = self.get_transitions(issue_key)
            for t in transitions:
                if t["id"] == transition_id:
                    to_status = t.get("to", {}).get("name", target_status)
                    break

            if dry_run:
                print(f"\n🔍 Dry run: Would transition to '{to_status}'")
                print(f"   Using transition: {transition_name} (ID: {transition_id})")
                return

            # Execute transition
            print(f"Transitioning to: {to_status}")
            self.transition_ticket(issue_key, transition_id)

            # Verify
            updated_ticket = self.get_ticket(issue_key)
            new_status = updated_ticket["fields"]["status"]["name"]

            print(f"✅ Success! Status: {current_status} → {new_status}")

        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Transition a Jira ticket to a new status",
        epilog="Example: %(prog)s PROJ-123 'In Progress'",
    )
    parser.add_argument("issue_key", help="Jira ticket key (e.g., PROJ-123)")
    parser.add_argument(
        "status",
        nargs="?",
        help="Target status name (e.g., 'In Progress', 'Done')",
    )
    parser.add_argument(
        "--list", "-l", action="store_true", help="List available transitions"
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
        help="Atlassian site hostname (default: from ATLASSIAN_SITE env or yoursite.atlassian.net)",
    )

    args = parser.parse_args()

    # Get credentials from environment
    email = os.getenv("ATLASSIAN_EMAIL")
    api_token = os.getenv("ATLASSIAN_API_TOKEN")

    if not email or not api_token:
        print("❌ Error: Missing credentials", file=sys.stderr)
        print("\nRequired environment variables:", file=sys.stderr)
        print("  - ATLASSIAN_EMAIL", file=sys.stderr)
        print("  - ATLASSIAN_API_TOKEN", file=sys.stderr)
        print("\nOptional:", file=sys.stderr)
        print("  - ATLASSIAN_SITE (default: yoursite.atlassian.net)", file=sys.stderr)
        sys.exit(1)

    # Create transitioner
    transitioner = JiraTransitioner(email, api_token, args.site)

    # Execute command
    if args.list:
        transitioner.list_transitions(args.issue_key)
    else:
        if not args.status:
            print("❌ Error: Status required (or use --list)", file=sys.stderr)
            parser.print_help()
            sys.exit(1)
        transitioner.execute_transition(args.issue_key, args.status, args.dry_run)


if __name__ == "__main__":
    main()
