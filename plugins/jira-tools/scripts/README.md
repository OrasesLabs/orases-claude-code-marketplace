# Jira Scripts

Python scripts for direct Jira REST API operations using API token authentication.

## Available Scripts

### 1. `view_ticket.py` - View Ticket Details

Display comprehensive ticket information including status, description, comments, and links.

```bash
# Basic view
python3 scripts/view_ticket.py TICKET-KEY

# Full details with comments
python3 scripts/view_ticket.py TICKET-KEY --full

# JSON output
python3 scripts/view_ticket.py TICKET-KEY --json
```

**Features:**
- Complete ticket metadata display
- Linked issues and subtasks
- Attachments information
- Rendered descriptions
- Optional full comment history
- JSON output for scripting

See `skills/jira/docs/viewing.md` for complete usage guide.

---

### 2. `transition_ticket.py` - Transition Tickets

Move tickets through workflow statuses.

```bash
# List available transitions
python3 scripts/transition_ticket.py TICKET-KEY --list

# Preview transition (dry run)
python3 scripts/transition_ticket.py TICKET-KEY "Status Name" --dry-run

# Execute transition
python3 scripts/transition_ticket.py TICKET-KEY "Status Name"
```

**Features:**
- List available transitions for any ticket
- Partial status name matching (e.g., "in prog" → "In Progress")
- Case-insensitive matching
- Dry-run mode to preview changes
- Clear error messages with suggestions
- Automatic transition ID lookup

See `skills/jira/docs/transitioning.md` for complete usage guide.

---

### 3. `link_ticket.py` - Link Tickets Together

Create, view, and remove links between Jira tickets.

```bash
# List available link types
python3 scripts/link_ticket.py --list-types

# View existing links on a ticket
python3 scripts/link_ticket.py TICKET-KEY --list

# Create a link (SOURCE blocks TARGET)
python3 scripts/link_ticket.py SOURCE-KEY TARGET-KEY "Blocks"

# Create link with comment
python3 scripts/link_ticket.py SOURCE-KEY TARGET-KEY "Relates" --comment "Related feature"

# Preview link creation (dry run)
python3 scripts/link_ticket.py SOURCE-KEY TARGET-KEY "Blocks" --dry-run

# Remove a link by ID
python3 scripts/link_ticket.py TICKET-KEY --remove 12345
```

**Features:**
- List all available link types
- View existing links on any ticket
- Create links with optional comments
- Fuzzy matching for link type names
- Dry-run mode to preview changes
- Remove links by ID

See `skills/jira/docs/linking.md` for complete usage guide.

---

### 4. `test_connection.py` - Test API Connection

Verify that your API token authentication is working correctly.

```bash
python3 scripts/test_connection.py
```

**Success output:**
```
✅ Connection Successful!

User: Your Name
Account ID: ...
Email: your.email@company.com
Active: True
```

**Failure output:**
```
❌ HTTP Error 401: Unauthorized

Authentication failed. Please check:
  1. API token is correct and not expired
  2. Email matches the account that created the token
  3. Token has not been revoked
```

---

## Setup

### Required Environment Variables

```bash
export ATLASSIAN_EMAIL="your.email@company.com"
export ATLASSIAN_API_TOKEN="ATATT..."
export ATLASSIAN_SITE="yoursite.atlassian.net"  # Optional, defaults to yoursite.atlassian.net
```

### Generate API Token

1. Visit: https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Name: `Claude Code Jira Plugin`
4. Copy the token (shown only once!)
5. Set environment variable: `export ATLASSIAN_API_TOKEN="paste_token"`

**See `SETUP.md` for detailed instructions.**

---

## Integration with Claude Code

These scripts are used by the `jira` skill.

When you ask Claude to view or transition a ticket, it calls these scripts:

```
User: "Show me PROJ-123"
              ↓
Claude invokes jira skill
              ↓
Skill runs: python3 scripts/view_ticket.py PROJ-123
              ↓
Reports formatted results to user
```

```
User: "Start working on PROJ-123"
              ↓
Claude invokes jira skill
              ↓
Maps "start" → "In Progress"
              ↓
Skill runs: python3 scripts/transition_ticket.py PROJ-123 "In Progress"
              ↓
Reports success to user
```

---

## Troubleshooting

### 401 Unauthorized

**Cause:** API token is invalid, expired, or revoked.

**Solution:** Generate a new token (see SETUP.md)

### 403 Forbidden

**Cause:** Your account doesn't have permission for this operation.

**Solution:** Check with Jira admin about your project permissions.

### 404 Not Found

**Cause:** Ticket doesn't exist or you don't have access.

**Solution:** Verify the ticket key and your project access.

### Transition not available

**Cause:** The workflow doesn't allow that status change from the current status.

**Solution:** Use `--list` to see available transitions.

---

## Dependencies

- **Python 3.6+**
- **No external packages required** (uses standard library only)
  - `urllib.request` - HTTP requests
  - `json` - JSON parsing
  - `base64` - Auth encoding
  - `argparse` - CLI arguments

---

## Security

⚠️ **Never commit API tokens to git!**

The `.gitignore` file is configured to exclude:
- `.env`
- `credentials.json`
- `secrets.json`

Store tokens in environment variables or secure credential managers.

---

## Quick Start

1. **Generate API token** → https://id.atlassian.com/manage-profile/security/api-tokens

2. **Set environment variables:**
   ```bash
   export ATLASSIAN_EMAIL="your.email@company.com"
   export ATLASSIAN_API_TOKEN="your_token_here"
   ```

3. **Test connection:**
   ```bash
   python3 scripts/test_connection.py
   ```

4. **View a ticket:**
   ```bash
   python3 scripts/view_ticket.py TICKET-123
   ```

5. **List available transitions:**
   ```bash
   python3 scripts/transition_ticket.py TICKET-123 --list
   ```

6. **Use with Claude:**
   ```
   "Show me TICKET-123"
   "Start working on TICKET-123"
   ```

---

## Files

```
scripts/
├── README.md              # This file
├── SETUP.md              # Detailed setup instructions
├── test_connection.py    # Test API authentication
├── view_ticket.py        # View ticket details
├── transition_ticket.py  # Transition workflow statuses
└── link_ticket.py        # Link tickets together
```

---

## Documentation

For detailed usage guides, see:
- `skills/jira/docs/viewing.md` - Complete guide for viewing tickets
- `skills/jira/docs/transitioning.md` - Complete guide for transitions
- `skills/jira/examples/common-workflows.md` - Real-world usage examples
