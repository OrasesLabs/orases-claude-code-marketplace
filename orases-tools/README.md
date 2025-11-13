# Orases Tools - Claude Code Plugin

A comprehensive Claude Code Plugin providing Orases productivity tools and platform integrations. Currently includes Jira workflow management with direct REST API access, with Confluence and additional integrations planned.

## Overview

This plugin extends Claude Code with specialized Skills and scripts for working efficiently with Orases platforms and services. Unlike simple scripts or manual workflows, this plugin provides autonomous, model-invoked capabilities that Claude uses automatically based on context.

## What is a Claude Code Plugin?

Plugins are modular packages that extend Claude Code's capabilities with:
- **Skills**: Model-invoked workflows (Claude decides when to use them)
- **Scripts**: Standalone utilities for direct API operations
- **Agents**: Specialized AI agents for complex workflows (planned)
- **Hooks**: Event-driven automation (planned)

## Current Features

### Jira Management

Complete Jira workflow management including:
- **View Tickets**: Display full ticket details with formatting
- **Transition Tickets**: Move tickets through workflow statuses
- **List Transitions**: See available workflow actions
- **Direct API Access**: Python scripts for standalone operations

### Skills

1. **jira-ticket-viewer** - View tickets with full context including comments, attachments, and linked issues
2. **jira-ticket-transition** - Transition ticket statuses with natural language support
3. **jira** - Unified Jira management combining viewing and transitions

### Scripts

Located in `scripts/` directory:
- `view_ticket.py` - View ticket details (basic, full, or JSON output)
- `transition_ticket.py` - Transition workflow statuses with dry-run support
- `test_connection.py` - Verify API authentication

## Installation

### Prerequisites

- Claude Code installed (>=1.0.0)
- Python 3.6+ (for Jira scripts)
- Access to Atlassian Jira instance
- Git (for cloning from private repository)

### Install from GitHub (Recommended)

```bash
# Install from private repository
claude plugin install git@github.com:OrasesLabs/claude-code-plugins.git
```

### Install Locally (Development)

```bash
# Clone the repository
git clone git@github.com:OrasesLabs/claude-code-plugins.git
cd claude-code-plugins

# Install the plugin
claude plugin install .
```

For detailed installation instructions, see **[INSTALL.md](INSTALL.md)**.

## Quick Start

See **[QUICKSTART.md](QUICKSTART.md)** for:
- 5-minute setup guide
- Authentication configuration
- Common usage examples
- Troubleshooting tips

## Configuration

### 1. Set Atlassian Hostname

Add to `~/.claude/CLAUDE.md`:

```markdown
- All Atlassian resources are found at the hostname `yoursite.atlassian.net`
```

### 2. Configure API Authentication

Generate an API token at: https://id.atlassian.com/manage-profile/security/api-tokens

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export ATLASSIAN_EMAIL="your.email@company.com"
export ATLASSIAN_API_TOKEN="ATATT..."
export ATLASSIAN_SITE="yoursite.atlassian.net"
```

For complete setup instructions, see **[INSTALL.md](INSTALL.md)**.

## Usage

### Autonomous (Skills)

Simply ask Claude to perform Jira tasks:

```
"Show me ticket PROJ-123"
"Move PROJ-123 to In Progress"
"What transitions are available for PROJ-123?"
"Mark PROJ-456 as done"
```

Claude will automatically invoke the appropriate skill based on your request.

### Direct (Scripts)

Run scripts standalone for automation or testing:

```bash
# View ticket
python3 scripts/view_ticket.py PROJ-123 --full

# List transitions
python3 scripts/transition_ticket.py PROJ-123 --list

# Transition ticket
python3 scripts/transition_ticket.py PROJ-123 "Done"

# Test authentication
python3 scripts/test_connection.py
```

## Plugin Structure

```
orases-tools/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
│
├── skills/                  # Model-invoked capabilities
│   └── jira/
│       ├── SKILL.md
│       ├── docs/
│       └── examples/
│
├── scripts/                 # Standalone utilities
│   ├── view_ticket.py
│   ├── transition_ticket.py
│   ├── test_connection.py
│   ├── SETUP.md
│   └── README.md
│
├── README.md               # This file
├── QUICKSTART.md           # Quick start guide
├── INSTALL.md              # Installation instructions
├── CHANGELOG.md            # Version history
└── LICENSE                 # MIT License
```

## Planned Features

### Jira Enhancements
- Search tickets with JQL support
- Create tickets with templates
- Update ticket fields
- Add comments
- Time tracking
- Bulk operations
- Sprint management

### Confluence Integration
- View pages
- Search content
- Create and update pages
- Manage spaces

### Additional Platforms
- Custom Orases integrations
- Workflow automation
- Git hooks for ticket linking
- CI/CD integration

## Development

### Creating New Skills

1. Create directory under `skills/`
2. Write `SKILL.md` with YAML frontmatter
3. Add supporting documentation
4. Test with natural language requests

Example SKILL.md:

```yaml
---
name: skill-name
description: What the skill does and when to use it
allowed-tools: [Bash, Read, Write]
---

# Detailed instructions for Claude

Additional context, examples, and guidance...
```

### Best Practices

- **Keep skills focused**: One capability per skill
- **Write specific descriptions**: Include trigger terms
- **Restrict tools appropriately**: Use `allowed-tools` for security
- **Document thoroughly**: Examples and edge cases
- **Version control**: Track changes in CHANGELOG.md

## Troubleshooting

### Skills Not Working

1. Restart Claude Code
2. Check YAML frontmatter is valid
3. Verify skill descriptions include trigger terms
4. Run `claude --debug` to see loading errors

### API Authentication Failures

1. Regenerate API token
2. Verify environment variables are set
3. Check email matches token owner
4. Test with `scripts/test_connection.py`

### Permission Errors

1. Verify Jira project permissions
2. Check ticket is accessible in browser
3. Contact Jira admin for access

For detailed troubleshooting, see:
- **[INSTALL.md](INSTALL.md)** - Installation issues
- **[scripts/SETUP.md](scripts/SETUP.md)** - API authentication
- **[skills/jira/docs/](skills/jira/docs/)** - Skill-specific documentation

## Architecture

This plugin uses a **hybrid authentication strategy**:
- **API Tokens** for Jira operations (simple, reliable, no OAuth complexity)
- **Direct REST API** calls via Python scripts (no external dependencies)
- **Modular Skills** for autonomous operation
- **Standalone Scripts** for automation and testing

## Contributing

Contributions are welcome! Please:

1. Create a new branch for your feature
2. Follow existing structure and conventions
3. Test thoroughly before submitting
4. Update documentation and CHANGELOG.md
5. Submit pull request with clear description

## Support

- **Documentation**: See INSTALL.md and QUICKSTART.md
- **Issues**: https://github.com/OrasesLabs/orases-claude-code-marketplace/issues
- **Script Help**: See scripts/README.md and scripts/SETUP.md
- **Skill Help**: See skills/jira/docs/ directory

## License

MIT License - See [LICENSE](LICENSE) file for details.

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Code Plugins Guide](https://docs.claude.com/en/docs/claude-code/plugins)
- [Atlassian Jira API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)

---

**Version:** 1.0.0
**Author:** Orases
**Repository:** https://github.com/OrasesLabs/orases-claude-code-marketplace
