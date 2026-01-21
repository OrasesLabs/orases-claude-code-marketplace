# Changelog

All notable changes to the Orases Tools Plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-13

### Added
- Initial plugin release
- **jira** skill for unified Jira management (viewing and transitioning tickets)
- Python scripts for direct Jira API operations:
  - `view_ticket.py` - View ticket details with formatting
  - `transition_ticket.py` - Transition workflow statuses
  - `test_connection.py` - Test API authentication
- Comprehensive documentation:
  - README with full plugin overview
  - QUICKSTART for rapid onboarding
  - INSTALL for setup instructions
  - Feature-specific guides in `skills/jira/docs/`
  - Common workflow examples in `skills/jira/examples/`
- API token authentication for Jira operations
- MIT License

### Documentation Structure
- Lean SKILL.md with references to detailed docs
- `docs/viewing.md` - Complete guide for viewing tickets
- `docs/transitioning.md` - Complete guide for transitions
- `examples/common-workflows.md` - Real-world usage patterns

### Security
- Environment variable-based API token storage
- .gitignore configured to prevent credential leaks
- Clear security documentation in scripts/SETUP.md

## [1.1.0] - 2025-12-17

### Added
- **Link Tickets** - New capability to create, view, and remove issue links
  - `link_ticket.py` script for all linking operations
  - Support for all Jira link types (Blocks, Duplicate, Relates, etc.)
  - List available link types with `--list-types`
  - View existing links on a ticket with `--list`
  - Create links with optional comments
  - Remove links by ID with `--remove`
  - Dry-run mode to preview changes
  - Fuzzy matching for link type names
- Documentation for linking in `skills/jira/docs/linking.md`
- Natural language triggers for linking ("link X to Y", "X blocks Y", "show links for X")

## [1.2.0] - 2026-01-21

### Added
- **Log Work Time** - New capability to log time spent on tickets
  - `log_worklog.py` script for worklog operations
  - Flexible time formats (2h, 30m, 2h 30m)
  - Multiple date formats (today, yesterday, YYYY-MM-DD, M/D)
  - Auto-generated comments from ticket summary
  - Custom comment support with `--comment`
  - Dry-run mode to preview worklogs with `--dry-run`
  - ADF (Atlassian Document Format) comment support for rich text
- Documentation for time tracking in `skills/jira/docs/worklogging.md`
- Natural language triggers for logging time ("log 2h to X for today", "track time", "add time")
- Time tracking examples in `skills/jira/examples/common-workflows.md`

## [Unreleased]

### Planned - Jira Features
- Search tickets skill with JQL support
- Create tickets skill with templates
- Update tickets skill for field modifications
- Comment management
- Bulk operations support
- Sprint management features

### Planned - Confluence Features
- View Confluence pages
- Search Confluence content
- Create and update pages
- Manage spaces

### Planned - Other Integrations
- Additional Orases platform integrations
- Custom hooks for git integration
- Workflow automation
