# Changelog

## [1.0.0] - 2026-03-02

### Added
- Initial marketplace release
- `/tldv-notes:meeting-notes` slash command with argument parsing
- TLDV Processor skill for meeting note generation
- Confluence page templates for structured notes
- Per-user configuration via `.claude/tldv-notes.local.md`
- Per-project configuration via `.claude/tldv-notes.md`
- Configurable note sections (header, meeting_link, attendees, summary, discussion_notes, action_items, footer)
- Configurable timezone, footer text, and MCP server prefix
- Dry run mode for previewing without publishing
- Support for processing specific meetings by ID
- Meeting type variations (standup, planning, client call, 1:1)
- Duration rounding to 15-minute increments
- Action item extraction with assignee and deadline support
