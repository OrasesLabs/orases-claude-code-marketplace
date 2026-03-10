# Changelog

## [1.1.0] - 2026-03-10

### Added
- Configurable settings via `.claude/work-summary.local.md`
- Settings: `base_branch`, `atlassian_hostname`, `mcp_server`, `default_post_action`,
  `include_client_summary`, `include_technical_summary`, `local_save_path`,
  `auto_detect_ticket`, `file_categories`
- Three-tier settings lookup: project-local, project-scoped, user-global
- Settings template file with full field reference
- Step 0 (Load Configuration) in execution workflow

### Fixed
- MCP tool names now use configurable server prefix instead of hardcoded values
- `Task` tool references updated to `Agent` tool
- Removed `allowed-tools` from skill and command frontmatter (avoids breakage on tool renames)

## [1.0.0] - 2026-02-20

### Added
- Initial plugin release migrated from project-local skill
- Work summary generator skill with 9-step workflow
- `/work-summary:work-summary` slash command
- Client-friendly summary template (QA steps, testing checklist)
- Technical summary template (architecture, files, commits)
- Review display format for Jira posting
- Local summary storage template
- Error handling guide for common failure scenarios
