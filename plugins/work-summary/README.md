# Work Summary Plugin

Generates comprehensive work summaries from git branch changes and posts them as structured Jira comments. Produces both a client-friendly summary (business impact, QA steps) and a technical summary (architecture, files, commits) for stakeholder visibility.

## Features

- Analyzes git branch changes against the integration branch (`review` or `main`)
- Fetches Jira ticket details for context and acceptance criteria
- Generates a **client-friendly summary** with QA steps and testing checklist
- Generates a **technical summary** with architecture notes, file categories, and commits
- Posts combined summary as a structured Jira comment
- Saves a local copy for audit trail

## Prerequisites

- Atlassian MCP server configured for `orases.atlassian.net`
- Git repository with feature branches
- GitHub CLI (`gh`) for PR detection (optional)

## Usage

### Slash Command

```
/work-summary:work-summary ABC-123
```

Or without arguments to auto-detect the ticket from the branch name:

```
/work-summary:work-summary
```

### Natural Language

- "Generate a work summary for ABC-123"
- "Post a work summary to Jira"
- "Summarize my branch changes"

## Workflow

1. Identify Jira ticket (from argument, branch name, or prompt)
2. Verify ticket exists and confirm with user
3. Analyze git changes (commits, files, stats)
4. Check for existing PR
5. Generate client-friendly summary with QA steps
6. Generate technical summary with file categories
7. Present for user review and approval
8. Post to Jira as a structured comment
9. Save local copy to `.claude/work-summaries/`

## Configuration

Create `.claude/work-summary.local.md` in your project root to customize behavior:

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
```

Settings are loaded in priority order:
1. `.claude/work-summary.local.md` - Project-local (gitignored)
2. `.claude/work-summary.md` - Project-scoped (committable for team defaults)
3. `~/.claude/work-summary.md` - User-global (across all projects)

All settings are optional — sensible defaults are used when no settings file exists.

| Setting | Default | Description |
|---|---|---|
| `base_branch` | `auto` | Branch to diff against (`auto`, `review`, `main`, etc.) |
| `atlassian_hostname` | `orases.atlassian.net` | Jira instance hostname |
| `mcp_server` | `claude_ai_Atlassian` | MCP server prefix for Atlassian tools |
| `default_post_action` | `ask` | After generation: `post_to_jira`, `save_locally`, or `ask` |
| `include_client_summary` | `true` | Generate client-friendly summary section |
| `include_technical_summary` | `true` | Generate technical summary section |
| `local_save_path` | `.claude/work-summaries` | Directory for local summary copies |
| `auto_detect_ticket` | `true` | Extract ticket key from branch name |
| `file_categories` | *(built-in)* | Custom file categorization patterns |

**Note:** Add `.claude/*.local.md` to your `.gitignore` for local settings files.

## Components

| Component | Name | Description |
|-----------|------|-------------|
| Skill | `work-summary:work-summary-generator` | Core workflow and generation logic |
| Command | `/work-summary:work-summary` | Slash command entry point |
