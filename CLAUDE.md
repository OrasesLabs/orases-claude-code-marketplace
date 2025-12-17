# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **Orases Claude Code Marketplace** - a curated collection of Claude Code plugins that provide productivity tools and platform integrations. The repository contains multiple independent plugins, each extending Claude Code with Skills, scripts, and capabilities.

**Structure:**
```
orases-marketplace/
├── .claude-plugin/
│   └── marketplace.json      # Marketplace-level configuration
├── jira-tools/              # Production plugin
│   ├── .claude-plugin/
│   │   └── plugin.json
│   ├── skills/jira/         # Model-invoked capabilities
│   └── scripts/             # Standalone Python utilities
└── example-plugin/          # Template for new plugins
    └── agents/              # Example agent implementations
```

## Current Plugins

### jira-tools (v1.1.0)
Complete Jira workflow management with direct REST API access.

**Authentication:** API token-based (environment variables)
- `ATLASSIAN_EMAIL` - User email address
- `ATLASSIAN_API_TOKEN` - Generated from https://id.atlassian.com/manage-profile/security/api-tokens
- `ATLASSIAN_SITE` - Defaults to `orases.atlassian.net` (configured in user's CLAUDE.md)

**Skills:**
- `jira` - Complete Jira management (viewing, transitioning, linking, future: search/create/update)

**Scripts:** (located in `jira-tools/scripts/`)
- `view_ticket.py TICKET-KEY [--full|--json]` - View ticket details
- `transition_ticket.py TICKET-KEY "Status" [--list|--dry-run]` - Transition workflow statuses
- `link_ticket.py SOURCE TARGET "Type" [--list|--remove|--dry-run]` - Link tickets together
- `test_connection.py` - Verify API authentication

**Important:** All scripts use Python 3.6+ standard library only (no external dependencies).

## Plugin Architecture

### Plugin Components
1. **Skills** (`skills/*/SKILL.md`) - Model-invoked workflows with YAML frontmatter
2. **Scripts** (`scripts/*.py`) - Standalone utilities for direct API operations
3. **Agents** (`agents/*/AGENT.md`) - Specialized AI agents for complex workflows (planned)
4. **Hooks** - Event-driven automation (planned)

### Skill Structure
Skills must include YAML frontmatter:
```yaml
---
name: skill-name
description: Detailed description including trigger terms
allowed-tools:
  - Bash
  - Read
  - AskUserQuestion
---
```

Description should include:
- What the skill does
- When to use it (trigger phrases)
- Supported operations

## Development Workflow

### Testing Jira Scripts
```bash
# Test authentication
python3 jira-tools/scripts/test_connection.py

# View a ticket
python3 jira-tools/scripts/view_ticket.py PROJ-123

# List available transitions
python3 jira-tools/scripts/transition_ticket.py PROJ-123 --list

# Preview transition (dry run)
python3 jira-tools/scripts/transition_ticket.py PROJ-123 "Status Name" --dry-run

# Execute transition
python3 jira-tools/scripts/transition_ticket.py PROJ-123 "Status Name"
```

### Installing Plugins Locally
```bash
# Install entire marketplace
claude plugin install .

# Install specific plugin (development)
cd jira-tools
claude plugin install .
```

### Creating New Plugins
1. Create plugin directory in repository root
2. Add `.claude-plugin/plugin.json` with metadata
3. Add skills in `skills/*/SKILL.md` with YAML frontmatter
4. Add scripts in `scripts/` directory
5. Update `.claude-plugin/marketplace.json` to register plugin
6. Add plugin section to main `README.md`

**Required Plugin Files:**
- `.claude-plugin/plugin.json` - Plugin manifest
- `README.md` - Plugin overview
- `INSTALL.md` - Installation instructions
- `QUICKSTART.md` - Quick start guide
- `CHANGELOG.md` - Version history
- `LICENSE` - License file

## Key Design Patterns

### Authentication Strategy
Jira plugin uses **API token authentication** (not OAuth) for simplicity:
- Tokens stored in environment variables (never in code)
- Direct REST API calls via Python `urllib.request`
- No external dependencies required

### Natural Language Mapping
Skills should map common user phrases to actions:
- "show", "view", "display" → View operations
- "start", "begin working" → "In Progress" status
- "finish", "complete", "done" → "Done" status
- "block", "blocked" → "Blocked" status

### Error Handling
Scripts provide detailed error messages with actionable solutions:
- **401 Unauthorized** → Regenerate API token
- **403 Forbidden** → Check permissions
- **404 Not Found** → Verify ticket exists and user has access
- **Transition errors** → List available transitions with `--list`

## Security Best Practices

1. **Never commit credentials** - `.gitignore` excludes `.env`, `credentials.json`, `secrets.json`, `**/api_token*`
2. **Environment variables** - Use for all API tokens and credentials
3. **Tool restrictions** - Use `allowed-tools` in skill frontmatter to limit capabilities
4. **Dry-run mode** - Always support preview mode for destructive operations

## Documentation Standards

Each plugin should include:
1. **README.md** - Overview, features, usage examples
2. **INSTALL.md** - Detailed installation and configuration
3. **QUICKSTART.md** - 5-minute setup guide
4. **CHANGELOG.md** - Version history with semantic versioning
5. **skills/*/docs/** - Detailed guides for each capability
6. **skills/*/examples/** - Common workflow examples

## Repository Conventions

- Python scripts should be executable (`chmod +x`)
- Use Python 3.6+ standard library (avoid external dependencies when possible)
- Follow semantic versioning (MAJOR.MINOR.PATCH)
- Update CHANGELOG.md for all plugin changes
- Keep skills focused (one primary capability per skill)
- Document trigger phrases in skill descriptions

## Testing Before Release

Before committing plugin changes:
1. Test authentication with `test_connection.py`
2. Verify all scripts work with real API calls
3. Test skill invocation via natural language requests
4. Validate plugin.json schema
5. Update version numbers and CHANGELOG.md
6. Verify documentation is current

## Plugin Distribution

Plugins can be installed:
- **From GitHub:** `claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git`
- **Locally:** `claude plugin install .` (from plugin directory)
- **Marketplace-wide:** `claude plugin install .` (from repository root)

## Planned Features

### Jira Plugin Enhancements
- Search tickets with JQL support
- Create tickets with templates
- Update ticket fields and add comments
- Time tracking and bulk operations
- Sprint management

### Future Plugins
- Confluence integration (view, search, create pages)
- Custom Orases platform integrations
- Git hooks for ticket linking
- CI/CD integration

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Code Plugins Guide](https://docs.claude.com/en/docs/claude-code/plugins)
- [Atlassian Jira API](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
