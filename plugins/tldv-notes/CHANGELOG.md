# Changelog

## [1.2.2] - 2026-03-13

### Fixed
- **DST timezone bug** — Meeting times displayed incorrectly after Daylight Saving Time took effect (March 9, 2026). Added explicit DST handling rules, UTC offset lookup table for US timezones, and step-by-step timestamp conversion instructions to SKILL.md
- **DST-aware date ranges** — `from`/`to` parameters in Step 2 now include correct ISO 8601 UTC offsets based on whether DST is active on the target date
- **DST abbreviation in templates** — Added reminder to `section-formats.md` that `{TZ}` must use the DST-aware abbreviation (e.g., EDT not EST)

## [1.2.0] - 2026-03-04

### Changed
- **Default formats now match author's intended output:**
  - `duration_rounding` default changed from `none` to `ceil_15m` (round up to nearest 15 min)
  - `discussion_notes_format` default changed from `prose` to `bulleted`
  - `action_items_format` default changed from `flat` to `grouped_by_person`
- **Header format updated:** Date, time, and duration now render on a single pipe-separated line with meeting recording link below (matching the original plugin output)
- **Attendees section:** Organizer is now always bold with "(Organizer)" label in default format
- **Slash command simplified:** Removed duplicated formatting/configuration logic from the command — it now delegates entirely to the skill, eliminating maintenance drift between the two

### Fixed
- Discussion notes defaulting to prose paragraphs instead of bulleted lists
- Action items defaulting to flat checklist instead of grouped-by-person format
- Duration not being rounded to 15-minute increments by default

## [1.0.0] - 2026-03-02

### Added
- Initial marketplace release
- `/tldv-notes:generate-meeting-notes` slash command with argument parsing
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
