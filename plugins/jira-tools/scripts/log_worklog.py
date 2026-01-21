#!/usr/bin/env python3
"""
Jira Worklog Logger

Logs time to a Jira ticket with proper comment and date support.
Uses REST API v3 with ADF comment format.

Requirements:
    - ATLASSIAN_EMAIL environment variable
    - ATLASSIAN_API_TOKEN environment variable
    - ATLASSIAN_SITE environment variable (default: orases.atlassian.net)

Usage:
    python log_worklog.py AILASUP-148 "2h 30m" --date 2026-01-20
    python log_worklog.py AILASUP-148 "2h 30m" --date 2026-01-20 --comment "Custom comment"
    python log_worklog.py AILASUP-148 "45m" --date yesterday
    python log_worklog.py AILASUP-148 "1h" --date today
"""

import os
import sys
import json
import base64
import argparse
from typing import Dict, Optional
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from datetime import datetime, timedelta
import re


class JiraWorklogger:
    """Log time to Jira tickets using REST API v3."""

    def __init__(self, email: str, api_token: str, site: str):
        """
        Initialize the Jira worklog logger.

        Args:
            email: Atlassian account email
            api_token: API token from Atlassian
            site: Jira site hostname (e.g., orases.atlassian.net)
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
            method: HTTP method (GET, POST, etc.)
            data: Request body for POST/PUT requests

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

        body = json.dumps(data).encode("utf-8") if data else None
        request = Request(url, headers=headers, method=method, data=body)

        try:
            with urlopen(request) as response:
                return json.loads(response.read().decode("utf-8"))
        except HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_json = json.loads(error_body)
                error_msg = error_json.get("errorMessages", [str(e)])
                if isinstance(error_msg, list):
                    error_msg = "; ".join(error_msg)
            except:
                error_msg = str(e)
            raise Exception(f"HTTP {e.code}: {error_msg}") from e

    def get_ticket_summary(self, issue_key: str) -> str:
        """
        Get the summary/title of a Jira ticket.

        Args:
            issue_key: Jira ticket key (e.g., AILASUP-148)

        Returns:
            Ticket summary string
        """
        url = f"{self.base_url}/issue/{issue_key}?fields=summary"
        response = self._make_request(url)
        return response.get("fields", {}).get("summary", "")

    def parse_date(self, date_str: str) -> datetime:
        """
        Parse date string into datetime object.

        Supports:
            - "today" / "now"
            - "yesterday"
            - "YYYY-MM-DD" format
            - "M/D" format (assumes current year)

        Args:
            date_str: Date string to parse

        Returns:
            datetime object
        """
        date_str = date_str.lower().strip()

        if date_str in ("today", "now"):
            return datetime.now()

        if date_str == "yesterday":
            return datetime.now() - timedelta(days=1)

        # Try YYYY-MM-DD format
        try:
            return datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            pass

        # Try M/D format (assume current year)
        try:
            parsed = datetime.strptime(date_str, "%m/%d")
            return parsed.replace(year=datetime.now().year)
        except ValueError:
            pass

        # Try M-D format
        try:
            parsed = datetime.strptime(date_str, "%m-%d")
            return parsed.replace(year=datetime.now().year)
        except ValueError:
            pass

        raise ValueError(
            f"Cannot parse date '{date_str}'. "
            "Use YYYY-MM-DD, M/D, 'today', or 'yesterday'"
        )

    def format_started_date(self, dt: datetime) -> str:
        """
        Format datetime to Jira's expected ISO 8601 format.

        Args:
            dt: datetime object

        Returns:
            ISO 8601 formatted string like "2026-01-20T12:00:00.000+0000"
        """
        # Set to noon to avoid timezone edge cases
        dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
        # Format with timezone offset (assuming local time)
        return dt.strftime("%Y-%m-%dT%H:%M:%S.000+0000")

    def build_adf_comment(self, text: str) -> Dict:
        """
        Build an Atlassian Document Format (ADF) comment structure.

        Args:
            text: Plain text comment

        Returns:
            ADF document structure
        """
        return {
            "type": "doc",
            "version": 1,
            "content": [
                {
                    "type": "paragraph",
                    "content": [{"type": "text", "text": text}],
                }
            ],
        }

    def validate_time_spent(self, time_spent: str) -> str:
        """
        Validate and normalize time spent format.

        Args:
            time_spent: Time string like "2h", "30m", "2h 30m"

        Returns:
            Validated time string

        Raises:
            ValueError: If format is invalid
        """
        # Pattern: optional hours + optional minutes
        pattern = r"^(?:(\d+)h)?\s*(?:(\d+)m)?$"
        match = re.match(pattern, time_spent.strip().lower())

        if not match:
            raise ValueError(
                f"Invalid time format '{time_spent}'. "
                "Use formats like '2h', '30m', '2h 30m'"
            )

        hours, minutes = match.groups()
        if not hours and not minutes:
            raise ValueError("Time must include hours and/or minutes")

        # Reconstruct normalized format
        parts = []
        if hours:
            parts.append(f"{hours}h")
        if minutes:
            parts.append(f"{minutes}m")

        return " ".join(parts)

    def add_worklog(
        self,
        issue_key: str,
        time_spent: str,
        date: datetime,
        comment: Optional[str] = None,
    ) -> Dict:
        """
        Add a worklog entry to a Jira ticket.

        Args:
            issue_key: Jira ticket key (e.g., AILASUP-148)
            time_spent: Time spent string (e.g., "2h 30m")
            date: Date when work was performed
            comment: Optional comment (defaults to "TICKET: Summary")

        Returns:
            API response with created worklog
        """
        # Validate time format
        time_spent = self.validate_time_spent(time_spent)

        # Get ticket summary for default comment
        summary = self.get_ticket_summary(issue_key)

        # Build comment text
        if comment:
            comment_text = comment
        else:
            comment_text = f"{issue_key}: {summary}"

        # Build request body
        body = {
            "timeSpent": time_spent,
            "started": self.format_started_date(date),
            "comment": self.build_adf_comment(comment_text),
        }

        url = f"{self.base_url}/issue/{issue_key}/worklog"
        return self._make_request(url, method="POST", data=body)

    def log_time(
        self,
        issue_key: str,
        time_spent: str,
        date_str: str,
        comment: Optional[str] = None,
        dry_run: bool = False,
    ) -> None:
        """
        Log time to a Jira ticket with user-friendly output.

        Args:
            issue_key: Jira ticket key
            time_spent: Time spent string
            date_str: Date string (parsed by parse_date)
            comment: Optional custom comment
            dry_run: If True, show what would be logged without doing it
        """
        try:
            # Parse and validate inputs
            date = self.parse_date(date_str)
            time_spent = self.validate_time_spent(time_spent)

            # Get ticket info
            summary = self.get_ticket_summary(issue_key)
            comment_text = comment if comment else f"{issue_key}: {summary}"

            # Show preview
            print(f"\n{'[DRY RUN] ' if dry_run else ''}Logging time to Jira:")
            print(f"  Ticket:  {issue_key}")
            print(f"  Summary: {summary}")
            print(f"  Date:    {date.strftime('%Y-%m-%d')}")
            print(f"  Time:    {time_spent}")
            print(f"  Comment: {comment_text}")

            if dry_run:
                print("\n[DRY RUN] No changes made.")
                return

            # Create worklog
            result = self.add_worklog(issue_key, time_spent, date, comment)

            # Success output
            worklog_id = result.get("id", "?")
            print(f"\n✅ Worklog created successfully!")
            print(f"  Worklog ID: {worklog_id}")
            print(f"  View: https://{self.site}/browse/{issue_key}?focusedWorklogId={worklog_id}")

        except Exception as e:
            print(f"\n❌ Error: {e}", file=sys.stderr)
            sys.exit(1)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Log time to a Jira ticket with comment and date support",
        epilog="""
Examples:
  %(prog)s AILASUP-148 "2h 30m" --date 2026-01-20
  %(prog)s AILASUP-148 "45m" --date yesterday
  %(prog)s AILASUP-148 "1h" --date today --comment "Custom note"
  %(prog)s AILASUP-148 "2h" --date 1/20 --dry-run
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("issue_key", help="Jira ticket key (e.g., AILASUP-148)")
    parser.add_argument(
        "time_spent",
        help="Time spent (e.g., '2h', '30m', '2h 30m')",
    )
    parser.add_argument(
        "--date",
        "-d",
        required=True,
        help="Date of work (YYYY-MM-DD, M/D, 'today', 'yesterday')",
    )
    parser.add_argument(
        "--comment",
        "-c",
        help="Custom comment (default: 'TICKET: Summary')",
    )
    parser.add_argument(
        "--dry-run",
        "-n",
        action="store_true",
        help="Show what would be logged without making changes",
    )
    parser.add_argument(
        "--site",
        default=os.getenv("ATLASSIAN_SITE", "orases.atlassian.net"),
        help="Atlassian site hostname (default: orases.atlassian.net)",
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
        print("\nTo generate an API token:", file=sys.stderr)
        print("  https://id.atlassian.com/manage-profile/security/api-tokens", file=sys.stderr)
        sys.exit(1)

    # Create logger and log time
    logger = JiraWorklogger(email, api_token, args.site)
    logger.log_time(
        issue_key=args.issue_key,
        time_spent=args.time_spent,
        date_str=args.date,
        comment=args.comment,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
