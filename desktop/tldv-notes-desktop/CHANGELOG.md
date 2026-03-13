# Changelog

## [2.1.1] - 2026-03-13

### Fixed

- **DST timezone bug** — Meeting times displayed one hour behind after Daylight Saving Time took effect (March 9, 2026). Claude was defaulting to EST (UTC-5) instead of EDT (UTC-4) because the skill had no explicit DST handling instructions.
  - **Root cause:** LLMs don't have built-in timezone libraries. When given an IANA timezone like `America/New_York`, Claude defaulted to the more commonly referenced EST offset rather than checking whether DST was active on the meeting date.
  - **Fix:** Added "Timezone and Daylight Saving Time" section to SKILL.md with explicit DST rules, a UTC offset lookup table for US timezones, and step-by-step instructions for converting TLDV timestamps. Updated `from`/`to` parameter examples in Step 2 to show correct ISO 8601 offsets. Added DST-aware abbreviation reminder to `templates/section-formats.md`.

### Changed

- **Replaced generic connector references with explicit MCP tool names** — Claude Desktop could not match "Use the TLDV connector" to actual MCP tools (`list-meetings`, `get-transcript`, etc.). SKILL.md now references specific tool names with parameter details so Claude can find them via tool search.
  - **Root cause:** TLDV is a local MCP server extension, not an Organization Connector. Claude's tool search couldn't resolve generic "connector" references to the actual tool names.

### Added

- **Template files for progressive disclosure** — Moved inline templates from SKILL.md into `templates/` directory:
  - `templates/page-layout.md` — full page structure and section order
  - `templates/section-formats.md` — all format variants with examples
  - `templates/empty-states.md` — fallback messages and note generation guidelines
  - SKILL.md references these files in Step 4; Claude loads them on demand (Level 3 progressive disclosure), reducing SKILL.md from ~10KB to ~8.5KB
- DST lookup table covering `America/New_York`, `America/Chicago`, `America/Denver`, `America/Los_Angeles`

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
