# Settings Template

Template for work-summary settings files. Copy one of the examples below to the appropriate
location and customize:

- `.claude/work-summary.local.md` — Project-local (gitignored, highest priority)
- `.claude/work-summary.md` — Project-scoped (committable for team defaults)
- `~/.claude/work-summary.md` — User-global (base defaults across all projects)

## Full Settings Template

```markdown
---
base_branch: auto
atlassian_hostname: orases.atlassian.net
<!-- mcp_server: claude_ai_Atlassian -->
default_post_action: ask
include_client_summary: true
include_technical_summary: true
<!-- local_save_path: .claude/work-summaries -->
<!-- auto_detect_ticket: true -->
<!-- client_summary_template: .claude/work-summary-templates/client-summary.md -->
<!-- technical_summary_template: .claude/work-summary-templates/technical-summary.md -->
<!-- review_display_template: .claude/work-summary-templates/review-display.md -->
<!-- file_categories:
  Controllers: "app/Http/Controllers/**/*.php"
  Models: "app/Models/**/*.php"
  Views: "resources/views/**/*.blade.php"
  Migrations: "database/migrations/**/*.php"
  Tests: "tests/**/*.php" -->
---

# Work Summary Settings

Project-specific configuration for the work-summary plugin.
```

## Minimal Settings

For most projects, only override what differs from defaults:

```markdown
---
base_branch: review
atlassian_hostname: orases.atlassian.net
---
```

## Settings Field Reference

### `base_branch`
- **Type**: string
- **Default**: `auto`
- **Values**: `auto`, `review`, `main`, `develop`, or any branch name
- **Description**: Branch to compare against when analyzing changes. `auto` checks for a beta/development branch (e.g., `review`, `develop`, `staging`) first, then falls back to `main`.

### `atlassian_hostname`
- **Type**: string
- **Default**: `orases.atlassian.net`
- **Description**: Jira Cloud instance hostname.

### `mcp_server`
- **Type**: string
- **Default**: `claude_ai_Atlassian`
- **Description**: MCP server prefix for Atlassian tools. Tool names may vary depending on the MCP server configuration.

### `default_post_action`
- **Type**: string
- **Default**: `ask`
- **Values**: `ask`, `post_to_jira`, `save_locally`, `both`
- **Description**: What happens after summary generation. `ask` prompts each time, `post_to_jira` posts without saving locally, `save_locally` skips Jira posting, `both` posts and saves.

### `include_client_summary`
- **Type**: boolean
- **Default**: `true`
- **Description**: Generate the client-friendly summary section with QA steps and testing checklist.

### `include_technical_summary`
- **Type**: boolean
- **Default**: `true`
- **Description**: Generate the technical summary section with architecture notes and file categories.

### `local_save_path`
- **Type**: string
- **Default**: `.claude/work-summaries`
- **Description**: Directory (relative to project root) for saving local summary copies.

### `auto_detect_ticket`
- **Type**: boolean
- **Default**: `true`
- **Description**: Attempt to extract Jira ticket key from the current git branch name when no ticket argument is provided.

### `client_summary_template`
- **Type**: string
- **Default**: *(built-in template)*
- **Description**: Path to a custom client summary template file. Overrides the built-in template.

### `technical_summary_template`
- **Type**: string
- **Default**: *(built-in template)*
- **Description**: Path to a custom technical summary template file. Overrides the built-in template.

### `review_display_template`
- **Type**: string
- **Default**: *(built-in template)*
- **Description**: Path to a custom review display format template file. Overrides the built-in template.

### `file_categories`
- **Type**: object (YAML mapping)
- **Default**: Built-in CakePHP patterns
- **Description**: Custom file categorization patterns for the Modified Files section. Override to match non-CakePHP project structures.
- **Example**:
  ```yaml
  file_categories:
    Controllers: "app/Http/Controllers/**/*.php"
    Models: "app/Models/**/*.php"
    Views: "resources/views/**/*.blade.php"
    Migrations: "database/migrations/**/*.php"
    Tests: "tests/**/*.php"
  ```
