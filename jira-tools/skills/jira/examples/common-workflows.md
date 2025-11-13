# Common Jira Workflows

Real-world examples of using the Jira skill for everyday tasks.

## Daily Standup Workflow

**User:** "Show me all my tickets"

*(Future - requires search functionality)*

**User:** "What's the status of PROJ-123?"

```bash
python3 scripts/view_ticket.py PROJ-123
```

**User:** "Start working on PROJ-123"

```bash
python3 scripts/transition_ticket.py PROJ-123 "In Progress"
```

## Bug Triage Workflow

**User:** "Show me BUG-456 with all details"

```bash
python3 scripts/view_ticket.py BUG-456 --full
```

Review the bug details, comments, and linked issues.

**User:** "Move BUG-456 to In Progress"

```bash
python3 scripts/transition_ticket.py BUG-456 "In Progress"
```

## Completing Work

**User:** "Show me PROJ-789"

```bash
python3 scripts/view_ticket.py PROJ-789
```

Verify the work is complete and requirements are met.

**User:** "Mark PROJ-789 as done"

```bash
python3 scripts/transition_ticket.py PROJ-789 "Done"
```

## Blocked Work

**User:** "I'm blocked on PROJ-234, move it to blocked"

```bash
python3 scripts/transition_ticket.py PROJ-234 "Blocked"
```

## View and Transition Combined

**User:** "Show me PROJ-555 and then move it to Ready to Launch"

1. First, view the ticket:
```bash
python3 scripts/view_ticket.py PROJ-555
```

2. Then transition it:
```bash
python3 scripts/transition_ticket.py PROJ-555 "Ready to Launch"
```

## Checking Permissions

**User:** "What can I do with PROJ-999?"

```bash
python3 scripts/transition_ticket.py PROJ-999 --list
```

This shows all available transitions based on:
- Current status
- Your permissions
- Workflow configuration

## Safe Transition with Dry Run

**User:** "Can I move PROJ-111 to production?"

1. Check what's possible:
```bash
python3 scripts/transition_ticket.py PROJ-111 --list
```

2. Preview the transition:
```bash
python3 scripts/transition_ticket.py PROJ-111 "Production" --dry-run
```

3. If safe, execute:
```bash
python3 scripts/transition_ticket.py PROJ-111 "Production"
```

## Handling Errors

**User:** "Move PROJ-222 to Done"

If transition fails:
```
❌ Cannot transition to 'Done'

Available transitions:
  - In Review
  - Blocked
```

**Response:** "I can't move it directly to Done from its current status. Would you like me to move it to 'In Review' first?"

## Getting JSON Data

For scripting or automation:

```bash
# Get ticket data as JSON
python3 scripts/view_ticket.py PROJ-333 --json

# Parse specific fields
python3 scripts/view_ticket.py PROJ-333 --json | jq '.fields.status.name'
python3 scripts/view_ticket.py PROJ-333 --json | jq '.fields.assignee.displayName'
```

## Tips

1. **Always view first** - Check current state before making changes
2. **Use --list** - Verify available transitions before attempting
3. **Use --dry-run** - Preview important changes
4. **Check --full** - Get complete context with comments when needed
5. **Natural language** - Ask in plain English, the skill handles mapping
