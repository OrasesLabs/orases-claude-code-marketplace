# Settings Template

Template for `.claude/work-summary.local.md`. Copy this to the project root and customize.

```markdown
---
base_branch: auto
atlassian_hostname: orases.atlassian.net
mcp_server: claude_ai_Atlassian
default_post_action: ask
include_client_summary: true
include_technical_summary: true
local_save_path: .claude/work-summaries
auto_detect_ticket: true
---

# Work Summary Settings

Project-specific configuration for the work-summary plugin.
```

## Minimal Settings

For most projects, only override what differs from defaults:

```markdown
---
base_branch: review
---
```

## Settings Field Reference

### `base_branch`
- **Type**: string
- **Default**: `auto`
- **Values**: `auto`, `review`, `main`, `develop`, or any branch name
- **Description**: Branch to compare against when analyzing changes. `auto` checks for `review` first, then falls back to `main`.

### `atlassian_hostname`
- **Type**: string
- **Default**: `orases.atlassian.net`
- **Description**: Jira Cloud instance hostname.

### `mcp_server`
- **Type**: string
- **Default**: `claude_ai_Atlassian`
- **Description**: MCP server prefix for Atlassian tools. The full tool name is constructed as `mcp__{mcp_server}__toolName`.

### `default_post_action`
- **Type**: string
- **Default**: `ask`
- **Values**: `ask`, `post_to_jira`, `save_locally`
- **Description**: What happens after summary generation. `ask` prompts each time, `post_to_jira` posts without confirmation, `save_locally` skips Jira posting.

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
