# Quick Start Guide

Get up and running with Orases Tools Plugin in 5 minutes.

## Prerequisites

- Claude Code installed and configured (>=1.0.0)
- Python 3.6+ for running scripts
- Access to yoursite.atlassian.net Jira instance
- Git access to OrasesLabs organization (for installation)

## Installation

### Step 1: Install the Plugin

```bash
# Install from private GitHub repository
claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git

# OR install locally (for development)
git clone git@github.com:OrasesLabs/orases-claude-code-marketplace.git
cd orases-claude-code-marketplace/orases-tools
claude plugin install .
```

### Step 2: Set Atlassian Hostname

Add to `~/.claude/CLAUDE.md`:

```markdown
- All Atlassian resources are found at the hostname `yoursite.atlassian.net`
```

### Step 3: Configure API Authentication

Generate an API token at: https://id.atlassian.com/manage-profile/security/api-tokens

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export ATLASSIAN_EMAIL="your.email@company.com"
export ATLASSIAN_API_TOKEN="ATATT..."
export ATLASSIAN_SITE="yoursite.atlassian.net"
```

Reload your shell:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

### Step 4: Verify Installation

Test API authentication:
```bash
python3 scripts/test_connection.py
```

Expected output:
```
✅ Connection Successful!
User: Your Name
Email: your.email@company.com
Active: True
```

## Test the Plugin

### 1. Test Skills (Autonomous)

Simply ask Claude to perform Jira tasks:

```
"Show me ticket PROJ-123"
"What's the status of PROJ-123?"
"Move PROJ-123 to In Progress"
```

Claude will automatically invoke the appropriate skill!

### 2. Test Scripts (Standalone)

Run scripts directly:

```bash
# View ticket
python3 scripts/view_ticket.py PROJ-123

# List transitions
python3 scripts/transition_ticket.py PROJ-123 --list

# Transition ticket (dry run)
python3 scripts/transition_ticket.py PROJ-123 "Done" --dry-run
```

## Common Usage Examples

### View Tickets

**Autonomous:**
```
"Show me ticket PROJ-123"
"What's in PROJ-123?"
"Display details for BUG-456"
```

**Script:**
```bash
# Basic view
python3 scripts/view_ticket.py PROJ-123

# Full details with comments
python3 scripts/view_ticket.py PROJ-123 --full

# JSON output
python3 scripts/view_ticket.py PROJ-123 --json
```

### Transition Tickets

**Autonomous:**
```
"Move PROJ-123 to In Progress"
"Mark PROJ-123 as done"
"Block ticket PROJ-456"
```

**Script:**
```bash
# List available transitions
python3 scripts/transition_ticket.py PROJ-123 --list

# Dry run (preview)
python3 scripts/transition_ticket.py PROJ-123 "Done" --dry-run

# Execute transition
python3 scripts/transition_ticket.py PROJ-123 "Done"
```

### Check Status

**Autonomous:**
```
"What transitions are available for PROJ-123?"
"Can I mark PROJ-123 as done?"
```

## What's Included

### Plugin Structure

```
orases-tools/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
│
├── skills/                  # Skills
│   └── jira/
│       ├── SKILL.md
│       ├── docs/
│       └── examples/
│
├── scripts/                 # Scripts
│   ├── view_ticket.py
│   ├── transition_ticket.py
│   ├── test_connection.py
│   ├── SETUP.md
│   └── README.md
│
├── README.md               # Plugin overview
├── QUICKSTART.md           # This file
├── INSTALL.md              # Installation guide
├── CHANGELOG.md            # Version history
└── LICENSE                 # MIT License
```

### Current Features

- ✅ View Jira tickets with full details
- ✅ Transition ticket statuses
- ✅ List available workflow transitions
- ✅ Natural language support
- ✅ Standalone Python scripts
- ✅ API token authentication

### Planned Features

- 🔄 Search tickets with JQL
- 🔄 Create new tickets
- 🔄 Update ticket fields
- 🔄 Add comments
- 🔄 Time tracking
- 🔄 Confluence integration
- 🔄 Bulk operations

## Troubleshooting

### Plugin Not Found

**Problem:** Installation fails

**Solution:**
- Verify GitHub SSH access: `ssh -T git@github.com`
- Check organization membership
- Try local installation instead

### Skills Not Working

**Problem:** Claude doesn't use the skills

**Solution:**
- Restart Claude Code
- Verify plugin installed: Check for plugin files
- Run debug mode: `claude --debug`

### API Authentication Failures (401)

**Problem:** Scripts return "Unauthorized"

**Solution:**
- Regenerate API token (may have expired)
- Verify environment variables: `echo $ATLASSIAN_API_TOKEN`
- Check email matches token owner
- Test with `scripts/test_connection.py`

### Permission Errors (403)

**Problem:** "You don't have permission"

**Solution:**
- Verify you can access ticket in browser
- Check Jira project permissions
- Contact Jira admin for access

### Python Not Found

**Problem:** `python3: command not found`

**Solution:**
- Install Python 3.6+
- On Ubuntu/WSL: `sudo apt install python3`
- On macOS: `brew install python3`

## Next Steps

### 1. Explore Capabilities

Try different natural language requests:
```
"Show me my open tickets"
"What's blocking PROJ-123?"
"Move ticket to ready for review"
"List all transitions for PROJ-123"
```

### 2. Customize for Your Workflow

Edit skills in `skills/jira/SKILL.md` to:
- Adjust output formatting
- Modify trigger descriptions
- Add custom workflows
- Restrict tool permissions

### 3. Create Automation

Use scripts in automation:
```bash
#!/bin/bash
# Daily standup script
for ticket in $(cat my_tickets.txt); do
  python3 scripts/view_ticket.py "$ticket"
done
```

### 4. Share with Team

The plugin is in a shared repository:
```bash
# Team members just install
claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git

# Updates are pulled automatically
claude plugin update orases-tools
```

## Tips & Best Practices

### Natural Language Tips

Claude understands these variations:
- "show", "view", "display", "check" → View ticket
- "start", "begin working" → In Progress
- "finish", "complete", "done" → Done
- "block", "blocked" → Blocked
- "ready", "ready to launch" → Ready to Launch

### Safety Features

- **Dry-run mode**: Test transitions before executing
- **Environment variables**: Credentials never in code
- **.gitignore**: Prevents credential commits
- **Permission checks**: Verifies access before operations

### Workflow Integration

1. **Morning standup**: "Show me my open tickets"
2. **Start work**: "Move PROJ-123 to In Progress"
3. **Complete work**: "Mark PROJ-123 as done"
4. **Review**: "What's the status of PROJ-123?"

## Resources

### Documentation

- **README.md** - Full plugin overview
- **INSTALL.md** - Detailed installation guide
- **CHANGELOG.md** - Version history
- **scripts/README.md** - Script documentation
- **scripts/SETUP.md** - API setup details

### Skill-Specific Docs

- `skills/jira/docs/` - Jira skill documentation
- `skills/jira/examples/` - Usage examples

### External Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Plugins](https://docs.claude.com/en/docs/claude-code/plugins)
- [Atlassian Jira API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)

## Get Help

1. Check plugin documentation (README, INSTALL)
2. Review troubleshooting guides in skill docs
3. Run `claude --debug` for detailed logs
4. Test scripts standalone: `python3 scripts/test_connection.py`
5. Report issues: https://github.com/OrasesLabs/orases-claude-code-marketplace/issues

## What's Next?

You're ready to:
1. ✅ View and transition Jira tickets
2. ✅ Use natural language or explicit commands
3. ✅ Run standalone scripts for automation
4. 🔄 Explore advanced features as they're added
5. 🔄 Contribute new skills and improvements

Happy coding! 🚀
