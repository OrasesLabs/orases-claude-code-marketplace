---
name: jira
description: Complete Jira ticket management including viewing tickets, transitioning statuses, linking tickets, searching, creating, and updating. Use when the user asks to view, show, display, check, move, transition, start, finish, complete, close, link, relate, block, duplicate, or manage Jira tickets. Supports natural language for all operations.
allowed-tools: Bash, Read, AskUserQuestion, TodoWrite
---

# Jira Management Skill

Complete Jira workflow management using direct REST API calls with API token authentication.

## When to Use This Skill

Activate when the user:
- **Viewing:** "Show me PROJ-123", "What's the status of PROJ-123?"
- **Transitioning:** "Move PROJ-123 to In Progress", "Mark it as done", "Start working on TICKET-123"
- **Linking:** "Link PROJ-123 to PROJ-456", "PROJ-123 blocks PROJ-456", "Show links for PROJ-123"
- **Searching:** "Find all my open tickets", "Show bugs in PROJ" (future)
- **Creating:** "Create a new bug ticket" (future)
- **Updating:** "Assign PROJ-123 to John" (future)

## Core Capabilities

### 1. View Tickets ✅

Display full ticket details including status, description, comments, attachments, and links.

**Script:** `scripts/view_ticket.py`
**Detailed Guide:** `skills/jira/docs/viewing.md`

**Quick Usage:**
```bash
# Basic view
python3 scripts/view_ticket.py TICKET-KEY

# Full details with comments
python3 scripts/view_ticket.py TICKET-KEY --full

# JSON output
python3 scripts/view_ticket.py TICKET-KEY --json
```

### 2. Transition Tickets ✅

Move tickets through workflow statuses (To Do → In Progress → Done).

**Script:** `scripts/transition_ticket.py`
**Detailed Guide:** `skills/jira/docs/transitioning.md`

**Quick Usage:**
```bash
# List available transitions
python3 scripts/transition_ticket.py TICKET-KEY --list

# Preview transition
python3 scripts/transition_ticket.py TICKET-KEY "Status Name" --dry-run

# Execute transition
python3 scripts/transition_ticket.py TICKET-KEY "Status Name"
```

### 3. Link Tickets ✅

Create, view, and remove links between tickets (blocks, duplicates, relates).

**Script:** `scripts/link_ticket.py`
**Detailed Guide:** `skills/jira/docs/linking.md`

**Quick Usage:**
```bash
# List available link types
python3 scripts/link_ticket.py --list-types

# View existing links on a ticket
python3 scripts/link_ticket.py TICKET-KEY --list

# Create a link (SOURCE blocks TARGET)
python3 scripts/link_ticket.py SOURCE-KEY TARGET-KEY "Blocks"

# Create link with comment
python3 scripts/link_ticket.py SOURCE-KEY TARGET-KEY "Relates" --comment "Related work"

# Remove a link by ID
python3 scripts/link_ticket.py TICKET-KEY --remove 12345
```

### 5. Search Tickets (Coming Soon)
- JQL queries
- Natural language search
- Filter by assignee, status, project

### 6. Create Tickets (Coming Soon)
- Create with templates
- Set required fields
- Link to related tickets

### 7. Update Tickets (Coming Soon)
- Modify fields
- Add comments
- Change metadata

## Authentication

All scripts use **Atlassian API Token** authentication.

**Required environment variables:**
```bash
ATLASSIAN_EMAIL="your.email@company.com"
ATLASSIAN_API_TOKEN="ATATT..."
ATLASSIAN_SITE="yoursite.atlassian.net"
```

**Setup:** See `scripts/SETUP.md`

## Natural Language Mapping

Map common phrases to Jira actions:

| User Says | Action | Maps To |
|-----------|--------|---------|
| "show", "view", "display" | View | `view_ticket.py` |
| "start", "begin working" | Transition | "In Progress" |
| "finish", "complete", "done" | Transition | "Done" |
| "block", "blocked" | Transition | "Blocked" |
| "link X to Y" | Link | `link_ticket.py` |
| "X blocks Y" | Link | "Blocks" link type |
| "X duplicates Y" | Link | "Duplicate" link type |
| "relate X and Y" | Link | "Relates" link type |
| "show links for X" | Link | `link_ticket.py --list` |

See `docs/transitioning.md` and `docs/linking.md` for complete mapping tables.

## Workflow Patterns

### View a Ticket

**User:** "Show me PROJ-123"

**Steps:**
1. Parse ticket key
2. Execute: `python3 scripts/view_ticket.py PROJ-123`
3. Present formatted output

### Transition a Ticket

**User:** "Start working on PROJ-123"

**Steps:**
1. Parse intent: "start" → "In Progress"
2. Execute: `python3 scripts/transition_ticket.py PROJ-123 "In Progress"`
3. Confirm success

### Check Available Actions

**User:** "What can I do with PROJ-123?"

**Steps:**
1. Execute: `python3 scripts/transition_ticket.py PROJ-123 --list`
2. Display available transitions

### Link Tickets

**User:** "PROJ-123 blocks PROJ-456"

**Steps:**
1. Parse intent: "blocks" → "Blocks" link type
2. Execute: `python3 scripts/link_ticket.py PROJ-123 PROJ-456 "Blocks"`
3. Confirm success

### View Existing Links

**User:** "Show links for PROJ-123"

**Steps:**
1. Execute: `python3 scripts/link_ticket.py PROJ-123 --list`
2. Display linked issues with relationship types

## Error Handling

### Authentication Errors (401)
- **Cause:** Invalid or expired API token
- **Fix:** Regenerate token at https://id.atlassian.com/manage-profile/security/api-tokens
- **Action:** Update `ATLASSIAN_API_TOKEN` environment variable

### Ticket Not Found (404)
- **Cause:** Invalid ticket key or no permission
- **Fix:** Verify ticket key and access permissions

### Transition Not Available
- **Cause:** Requested transition not allowed from current status
- **Action:** List available transitions with `--list` flag
- **Suggest:** Alternative valid transitions

See detailed error guides in:
- `docs/viewing.md#error-handling`
- `docs/transitioning.md#error-handling`

## Best Practices

1. **Always verify first** - Check current state before making changes
2. **Use dry-run** - Preview important transitions with `--dry-run`
3. **List transitions** - Check available options with `--list` before transitioning
4. **Handle errors gracefully** - Offer alternatives when operations fail
5. **Confirm bulk operations** - Ask before changing multiple tickets

## Examples

See `examples/` directory for common usage patterns:
- View and transition workflow
- Checking permissions
- Bulk operations (future)
- Integration with other tools (future)

## Testing

**Test ticket:** PROJ-123

```bash
# Test viewing
python3 scripts/view_ticket.py PROJ-123

# Test transitions
python3 scripts/transition_ticket.py PROJ-123 --list
python3 scripts/transition_ticket.py PROJ-123 "Ready to Launch" --dry-run
```

## Documentation Structure

```
skills/jira/
├── SKILL.md                   # This file - main skill definition
├── docs/
│   ├── viewing.md            # Detailed guide for view_ticket.py
│   ├── transitioning.md      # Detailed guide for transition_ticket.py
│   └── linking.md            # Detailed guide for link_ticket.py
└── examples/
    └── (coming soon)
```

## Scripts Reference

All scripts are in the plugin's root `scripts/` directory:

```
scripts/
├── view_ticket.py           # View ticket details
├── transition_ticket.py     # Transition ticket status
├── link_ticket.py           # Link tickets together
├── test_connection.py       # Test API authentication
├── README.md               # Complete scripts guide
└── SETUP.md               # Authentication setup
```

---

**For detailed usage:** See `docs/viewing.md`, `docs/transitioning.md`, and `docs/linking.md`
**For setup:** See `scripts/SETUP.md`
