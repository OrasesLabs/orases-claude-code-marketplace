# Changelog

## [1.0.0] - 2026-03-11

### Added
- Initial plugin release
- Work summary generator skill with 10-step workflow
- Client-friendly summary generator skill (standalone capable)
- Technical summary generator skill (standalone capable)
- `/work-summary:generate-work-summary` slash command
- `/work-summary:setup` command for guided settings configuration
- `/work-summary:help` command for capabilities overview and configuration assistance
- Configurable settings via three-tier hierarchy (user-global, project-scoped, project-local)
- Settings: `base_branch`, `atlassian_hostname`, `mcp_server`, `default_post_action`,
  `include_client_summary`, `include_technical_summary`, `local_save_path`,
  `auto_detect_ticket`, `file_categories`, `client_summary_template`,
  `technical_summary_template`, `review_display_template`
- Template override support for client summary, technical summary, and review display
- Client-friendly summary template (QA steps, testing checklist)
- Technical summary template (architecture, files, commits)
- Review display format template for Jira posting
- Local summary storage template
- Settings template with HTML comment examples for optional settings
- Error handling guide with CodeCommit and GitHub support
- File categorization reference with custom category examples
- "Post to Jira and save locally" option for combined post-and-save workflow
