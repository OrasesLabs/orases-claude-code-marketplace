# API Token Setup Guide

Complete guide for setting up Atlassian API token authentication for the Jira scripts.

## Overview

The Jira scripts use **Atlassian API Token** authentication. This is a simple, secure method that doesn't require OAuth flows or complex setup.

## Step 1: Generate an API Token

1. Visit: **https://id.atlassian.com/manage-profile/security/api-tokens**
2. Click **"Create API token"**
3. Name it: `Claude Code Jira Plugin`
4. Click **"Create"**
5. **Copy the token immediately** (it's only shown once!)

## Step 2: Set Environment Variables

### Temporary (Current Session Only)

```bash
export ATLASSIAN_EMAIL="your.email@company.com"
export ATLASSIAN_API_TOKEN="ATATT3xFf..."  # Paste your token here
export ATLASSIAN_SITE="yoursite.atlassian.net"  # Optional, defaults to yoursite.atlassian.net
```

### Permanent (Recommended)

Add to your shell configuration file (`~/.bashrc`, `~/.zshrc`, or `~/.profile`):

```bash
# Jira API Credentials
export ATLASSIAN_EMAIL="your.email@company.com"
export ATLASSIAN_API_TOKEN="ATATT3xFf..."  # Your token here
export ATLASSIAN_SITE="yoursite.atlassian.net"
```

Then reload your shell:
```bash
source ~/.bashrc  # or ~/.zshrc or ~/.profile
```

### Verify Variables Are Set

```bash
echo $ATLASSIAN_EMAIL
echo $ATLASSIAN_API_TOKEN
echo $ATLASSIAN_SITE
```

## Step 3: Test the Connection

Run the test script to verify authentication:

```bash
python3 scripts/test_connection.py
```

### Expected Success Output

```
✅ Connection Successful!

User: Your Name
Account ID: 123abc...
Email: your.email@company.com
Active: True
```

### If Authentication Fails

```
❌ HTTP Error 401: Unauthorized

Authentication failed. Please check:
  1. API token is correct and not expired
  2. Email matches the account that created the token
  3. Token has not been revoked
```

**Solution:** Verify your environment variables and regenerate the token if needed.

## Step 4: Test Script Functionality

### View a Ticket

```bash
python3 scripts/view_ticket.py TICKET-KEY
```

### List Available Transitions

```bash
python3 scripts/transition_ticket.py TICKET-KEY --list
```

### Perform a Dry-Run Transition

```bash
python3 scripts/transition_ticket.py TICKET-KEY "Status Name" --dry-run
```

## Troubleshooting

### 401 Unauthorized

**Causes:**
- Token is expired (tokens can expire based on your Atlassian settings)
- Token was revoked
- Email doesn't match the account that created the token
- Token has insufficient permissions

**Solution:**
1. Generate a new token (Step 1)
2. Update the `ATLASSIAN_API_TOKEN` environment variable
3. Test again with `test_connection.py`

### Required Permissions

When creating the token, it automatically has:
- ✅ `read:jira-work` - View Jira tickets
- ✅ `write:jira-work` - Update Jira tickets

These permissions are sufficient for all script operations.

### Email Verification

Make sure the email in `ATLASSIAN_EMAIL` matches the account that created the token.

To verify your current email:
```bash
echo $ATLASSIAN_EMAIL
```

### Token Storage Security

⚠️ **Important Security Notes:**

1. **Never commit tokens to git**
   - The `.gitignore` excludes `.env`, `credentials.json`, `secrets.json`
   - Double-check before committing any files

2. **Use environment variables**
   - Don't hardcode tokens in scripts
   - Store in shell config files (which should not be in git)

3. **Regenerate if compromised**
   - If a token is exposed, revoke it immediately at:
     https://id.atlassian.com/manage-profile/security/api-tokens
   - Generate a new token

4. **Token expiration**
   - Tokens can be set to expire (check your Atlassian settings)
   - Regenerate when needed

## Alternative: Using .env File (Optional)

If you prefer using a `.env` file instead of shell exports:

1. Create `.env` in the plugin root:
   ```bash
   ATLASSIAN_EMAIL=your.email@company.com
   ATLASSIAN_API_TOKEN=ATATT3xFf...
   ATLASSIAN_SITE=yoursite.atlassian.net
   ```

2. Load before running scripts:
   ```bash
   export $(cat .env | xargs)
   python3 scripts/view_ticket.py TICKET-123
   ```

**Note:** The `.env` file is already in `.gitignore` to prevent accidental commits.

## Using with Claude Code

Once authentication is configured, you can use natural language with Claude:

```
"Show me TICKET-123"
"Start working on TICKET-456"
"Move TICKET-789 to Done"
"What can I do with TICKET-111?"
```

The `jira` skill will automatically use your configured credentials to execute these operations.

## Revoking Tokens

To revoke an API token:

1. Visit: https://id.atlassian.com/manage-profile/security/api-tokens
2. Find the token in your list
3. Click **"Revoke"**
4. Generate a new token if you want to continue using the scripts

## Platform-Specific Notes

### Linux/macOS

Environment variables can be set in:
- `~/.bashrc` (Bash)
- `~/.zshrc` (Zsh)
- `~/.profile` (Generic)

### Windows (WSL)

If using Windows Subsystem for Linux:
- Use the same files as Linux (`~/.bashrc`, etc.)
- Variables are session-specific to WSL

### Windows (Native)

If running Python natively on Windows:
- Set environment variables through System Properties → Environment Variables
- Or use `set` command in Command Prompt
- Or `$env:VARIABLE="value"` in PowerShell

## Summary

1. ✅ Generate API token at Atlassian
2. ✅ Set environment variables (email, token, site)
3. ✅ Test with `test_connection.py`
4. ✅ Start using scripts or Claude skill

For additional help, see:
- `scripts/README.md` - Scripts overview
- `skills/jira/docs/viewing.md` - Viewing tickets guide
- `skills/jira/docs/transitioning.md` - Transitioning tickets guide
