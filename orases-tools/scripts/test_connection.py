#!/usr/bin/env python3
"""
Test Jira API Connection

Verifies that API token authentication is working correctly.

Usage:
    python test_connection.py
"""

import os
import sys
import base64
import json
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def test_connection():
    """Test API connection with current credentials."""
    # Get credentials
    email = os.getenv("ATLASSIAN_EMAIL")
    api_token = os.getenv("ATLASSIAN_API_TOKEN")
    site = os.getenv("ATLASSIAN_SITE", "yoursite.atlassian.net")

    print("Testing Jira API Connection...")
    print(f"Email: {email if email else '❌ NOT SET'}")
    print(f"Token: {'✅ SET' if api_token else '❌ NOT SET'}")
    print(f"Site: {site}\n")

    if not email or not api_token:
        print("❌ Error: Missing credentials\n")
        print("Please set environment variables:")
        print("  export ATLASSIAN_EMAIL='your.email@company.com'")
        print("  export ATLASSIAN_API_TOKEN='ATATT...'")
        print("\nTo generate an API token:")
        print("  1. Visit: https://id.atlassian.com/manage-profile/security/api-tokens")
        print("  2. Click 'Create API token'")
        print("  3. Name it 'Claude Code Jira Skills'")
        print("  4. Copy the token (shown only once!)")
        print("  5. Set it: export ATLASSIAN_API_TOKEN='paste_token_here'")
        return False

    # Create auth header
    try:
        auth_string = f"{email}:{api_token}"
        auth_bytes = auth_string.encode("ascii")
        base64_bytes = base64.b64encode(auth_bytes)
        auth_header = f"Basic {base64_bytes.decode('ascii')}"
    except Exception as e:
        print(f"❌ Error encoding credentials: {e}")
        return False

    # Test connection
    url = f"https://{site}/rest/api/3/myself"

    try:
        request = Request(
            url,
            headers={
                "Authorization": auth_header,
                "Accept": "application/json",
            },
        )

        with urlopen(request) as response:
            data = json.loads(response.read().decode("utf-8"))

            print("✅ Connection Successful!\n")
            print(f"User: {data.get('displayName', 'Unknown')}")
            print(f"Account ID: {data.get('accountId', 'Unknown')}")
            print(f"Email: {data.get('emailAddress', 'Unknown')}")
            print(f"Active: {data.get('active', False)}")

            return True

    except HTTPError as e:
        error_body = e.read().decode("utf-8")
        print(f"❌ HTTP Error {e.code}: {e.reason}\n")

        if e.code == 401:
            print("Authentication failed. Please check:")
            print("  1. API token is correct and not expired")
            print("  2. Email matches the account that created the token")
            print("  3. Token has not been revoked")
            print("\nTo create a new token:")
            print("  https://id.atlassian.com/manage-profile/security/api-tokens")
        elif e.code == 403:
            print("Permission denied. Your account may not have API access.")
        elif e.code == 404:
            print(f"Site not found. Check that '{site}' is correct.")
        else:
            print(f"Error details: {error_body}")

        return False

    except Exception as e:
        print(f"❌ Connection Error: {e}")
        print(f"\nCheck that '{site}' is accessible")
        return False


if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)
