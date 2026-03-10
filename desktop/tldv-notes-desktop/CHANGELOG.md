# Changelog

## [2.0.0] - 2026-03-10

### Changed

- **Restructured as Organization Skill** — replaced Project Knowledge format with Organization Skill format (zip with `SKILL.md`)
- Admin uploads once, all team members get the skill automatically
- Removed `project-knowledge/` directory and `custom-instructions.txt` (no longer needed)
- Replaced hard-coded MCP tool prefixes with generic connector references
- Simplified installation: zip and upload instead of per-user Project setup

### Added

- `tldv-meeting-notes/SKILL.md` — core skill file with YAML frontmatter
- Connector availability error handling

## [1.0.0] - 2026-03-10

### Added

- Initial release of tldv-notes-desktop (Project Knowledge format)
- Project knowledge document with full processing instructions, templates, and configuration
- Custom instructions for Claude.ai Teams Projects
- Support for all format settings from the CLI version
- Installation guide for Claude.ai Teams (web) and Claude Desktop app
- Adapted from [tldv-notes](../../plugins/tldv-notes/) (Claude Code CLI plugin)
