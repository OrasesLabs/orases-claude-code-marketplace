#!/usr/bin/env python3
"""
Jira Ticket Viewer Script

Views detailed information about a Jira ticket using direct REST API calls.
Uses API token authentication from environment variables.

Requirements:
    - ATLASSIAN_EMAIL environment variable
    - ATLASSIAN_API_TOKEN environment variable
    - ATLASSIAN_SITE environment variable (default: yoursite.atlassian.net)

Usage:
    python view_ticket.py PROJ-123
    python view_ticket.py PROJ-123 --full      # Include all comments
    python view_ticket.py PROJ-123 --json      # Output JSON
"""

import os
import sys
import json
import base64
import argparse
from typing import Dict, List, Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from datetime import datetime


class JiraViewer:
    """View Jira ticket details using REST API."""

    def __init__(self, email: str, api_token: str, site: str):
        """
        Initialize the Jira viewer.

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

    def _make_request(self, url: str) -> Dict:
        """
        Make an authenticated GET request to Jira API.

        Args:
            url: Full URL to request

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

        request = Request(url, headers=headers, method="GET")

        try:
            with urlopen(request) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_json = json.loads(error_body)
                error_msg = error_json.get("errorMessages", [str(e)])[0]
            except:
                error_msg = str(e)
            raise Exception(f"HTTP {e.code}: {error_msg}") from e

    def get_ticket(self, issue_key: str, full: bool = False) -> Dict:
        """
        Get ticket details.

        Args:
            issue_key: Jira ticket key (e.g., PROJ-123)
            full: If True, fetch all fields including comments

        Returns:
            Ticket data
        """
        # Build fields list
        fields = [
            "summary",
            "description",
            "status",
            "issuetype",
            "assignee",
            "reporter",
            "priority",
            "created",
            "updated",
            "labels",
            "fixVersions",
            "components",
            "issuelinks",
            "attachment",
            "subtasks",
            "parent",
        ]

        if full:
            fields.append("comment")

        fields_param = ",".join(fields)
        expand_param = "renderedFields,names"

        url = f"{self.base_url}/issue/{issue_key}?fields={fields_param}&expand={expand_param}"
        return self._make_request(url)

    def format_date(self, date_string: str) -> str:
        """Format ISO date to readable string."""
        if not date_string:
            return "Unknown"
        try:
            dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))
            return dt.strftime("%Y-%m-%d %H:%M")
        except:
            return date_string

    def display_ticket(self, issue_key: str, full: bool = False, json_output: bool = False):
        """
        Display ticket information.

        Args:
            issue_key: Jira ticket key
            full: Show all comments
            json_output: Output raw JSON
        """
        try:
            ticket = self.get_ticket(issue_key, full=full)

            if json_output:
                print(json.dumps(ticket, indent=2))
                return

            fields = ticket.get("fields", {})

            # Header
            summary = fields.get("summary", "No title")
            print(f"\n📋 {issue_key}: {summary}")
            print("=" * 80)

            # Status and basic info
            status = fields.get("status", {}).get("name", "Unknown")
            issue_type = fields.get("issuetype", {}).get("name", "Unknown")
            priority = fields.get("priority", {}).get("name", "Unknown")

            print(f"\nStatus: {status}")
            print(f"Type: {issue_type}")
            print(f"Priority: {priority}")

            # People
            assignee = fields.get("assignee")
            reporter = fields.get("reporter")

            assignee_name = assignee.get("displayName", "Unassigned") if assignee else "Unassigned"
            reporter_name = reporter.get("displayName", "Unknown") if reporter else "Unknown"

            print(f"Assignee: {assignee_name}")
            print(f"Reporter: {reporter_name}")

            # Dates
            created = self.format_date(fields.get("created", ""))
            updated = self.format_date(fields.get("updated", ""))

            print(f"Created: {created}")
            print(f"Updated: {updated}")

            # Labels
            labels = fields.get("labels", [])
            if labels:
                print(f"Labels: {', '.join(labels)}")

            # Fix versions
            fix_versions = fields.get("fixVersions", [])
            if fix_versions:
                versions = [v.get("name", "") for v in fix_versions]
                print(f"Fix Versions: {', '.join(versions)}")

            # Components
            components = fields.get("components", [])
            if components:
                comp_names = [c.get("name", "") for c in components]
                print(f"Components: {', '.join(comp_names)}")

            # Description
            description = fields.get("description")
            if description:
                # Try to get rendered description
                rendered = ticket.get("renderedFields", {}).get("description")
                if rendered:
                    # Strip HTML tags for terminal display
                    import re
                    clean_desc = re.sub('<[^<]+?>', '', rendered)
                    print(f"\nDescription:")
                    print("-" * 80)
                    print(clean_desc[:500])  # Limit length
                    if len(clean_desc) > 500:
                        print("... (truncated)")
                else:
                    print(f"\nDescription: (complex formatting, view in browser)")

            # Comments
            if full:
                comments = fields.get("comment", {}).get("comments", [])
                if comments:
                    print(f"\nComments ({len(comments)} total):")
                    print("-" * 80)
                    for i, comment in enumerate(comments[-5:], 1):  # Last 5 comments
                        author = comment.get("author", {}).get("displayName", "Unknown")
                        created = self.format_date(comment.get("created", ""))
                        body = comment.get("body", "(empty)")

                        # Try to extract text from body
                        if isinstance(body, dict):
                            body = str(body)  # Complex format

                        print(f"\n{i}. {author} ({created}):")
                        print(f"   {body[:200]}")
                        if len(str(body)) > 200:
                            print("   ... (truncated)")
                else:
                    print("\nComments: None")

            # Linked issues
            issue_links = fields.get("issuelinks", [])
            if issue_links:
                print(f"\nLinked Issues:")
                print("-" * 80)
                for link in issue_links:
                    link_type = link.get("type", {}).get("name", "Related")

                    if "outwardIssue" in link:
                        linked = link["outwardIssue"]
                        direction = link.get("type", {}).get("outward", "links to")
                    elif "inwardIssue" in link:
                        linked = link["inwardIssue"]
                        direction = link.get("type", {}).get("inward", "linked from")
                    else:
                        continue

                    linked_key = linked.get("key", "?")
                    linked_summary = linked.get("fields", {}).get("summary", "")
                    linked_status = linked.get("fields", {}).get("status", {}).get("name", "")

                    print(f"  {direction}: {linked_key} - {linked_summary} ({linked_status})")

            # Subtasks
            subtasks = fields.get("subtasks", [])
            if subtasks:
                print(f"\nSubtasks ({len(subtasks)}):")
                print("-" * 80)
                for subtask in subtasks:
                    sub_key = subtask.get("key", "?")
                    sub_summary = subtask.get("fields", {}).get("summary", "")
                    sub_status = subtask.get("fields", {}).get("status", {}).get("name", "")
                    print(f"  {sub_key}: {sub_summary} ({sub_status})")

            # Parent (if this is a subtask)
            parent = fields.get("parent")
            if parent:
                parent_key = parent.get("key", "?")
                parent_summary = parent.get("fields", {}).get("summary", "")
                print(f"\nParent: {parent_key} - {parent_summary}")

            # Attachments
            attachments = fields.get("attachment", [])
            if attachments:
                print(f"\nAttachments ({len(attachments)}):")
                print("-" * 80)
                for att in attachments:
                    filename = att.get("filename", "Unknown")
                    size = att.get("size", 0)
                    size_kb = size / 1024 if size else 0
                    print(f"  {filename} ({size_kb:.1f} KB)")

            print("\n" + "=" * 80)
            print(f"View in browser: https://{self.site}/browse/{issue_key}")
            print()

        except Exception as e:
            print(f"❌ Error: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="View detailed information about a Jira ticket",
        epilog="Example: %(prog)s PROJ-123 --full",
    )
    parser.add_argument("issue_key", help="Jira ticket key (e.g., PROJ-123)")
    parser.add_argument(
        "--full", "-f", action="store_true", help="Show all comments and details"
    )
    parser.add_argument(
        "--json", "-j", action="store_true", help="Output raw JSON"
    )
    parser.add_argument(
        "--site",
        default=os.getenv("ATLASSIAN_SITE", "yoursite.atlassian.net"),
        help="Atlassian site hostname",
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
        sys.exit(1)

    # Create viewer
    viewer = JiraViewer(email, api_token, args.site)

    # Display ticket
    viewer.display_ticket(args.issue_key, full=args.full, json_output=args.json)


if __name__ == "__main__":
    main()
