# Work Summary Plugin

Generates comprehensive work summaries from git branch changes and posts them as structured Jira comments. Produces both a client-friendly summary (business impact, QA steps) and a technical summary (architecture, files, commits) for stakeholder visibility.

## Features

- Analyzes git branch changes against a configurable base branch
- Fetches Jira ticket details for context and acceptance criteria
- Generates a **client-friendly summary** with QA steps and testing checklist
- Generates a **technical summary** with architecture notes, file categories, and commits
- Posts combined summary as a structured Jira comment
- Saves a local copy for audit trail
- Supports CodeCommit, GitHub, and other repository hosting services for PR detection
- Template overrides for full customization of summary output

## Prerequisites

- Atlassian MCP server configured for your Jira instance
- Git repository with feature branches
- AWS CLI (for CodeCommit PR detection) or GitHub CLI (for GitHub PR detection) — optional

## Usage

### Slash Commands

```
/work-summary:work-summary ABC-123
```

Or without arguments to auto-detect the ticket from the branch name:

```
/work-summary:work-summary
```

### Setup & Help

```
/work-summary:setup          # Guided settings configuration
/work-summary:help           # Capabilities overview and configuration
```

### Natural Language

- "Generate a work summary for ABC-123"
- "Post a work summary to Jira"
- "Summarize my branch changes"
- "Create a client summary of my changes"
- "Generate a technical summary for this branch"

## Workflow

1. Load configuration from settings files
2. Identify Jira ticket (from argument, branch name, or prompt)
3. Verify ticket exists and confirm with user
4. Analyze git changes (commits, files, stats)
5. Check for existing PR/merge request
6. Generate client-friendly summary with QA steps
7. Generate technical summary with file categories
8. Present for user review and approval
9. Post to Jira as a structured comment
10. Save local copy

## Configuration

Create a settings file to customize behavior. Settings are loaded in priority order
(later files override earlier ones):

1. `~/.claude/work-summary.md` - User-global (base defaults)
2. `.claude/work-summary.md` - Project-scoped (team defaults, committable)
3. `.claude/work-summary.local.md` - Project-local (personal overrides, gitignored)

Run `/work-summary:setup` for guided configuration, or create the file manually:

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
---
```

All settings are optional — sensible defaults are used when no settings file exists.

| Setting | Default | Description |
|---|---|---|
| `base_branch` | `auto` | Branch to diff against (`auto`, `review`, `main`, etc.) |
| `atlassian_hostname` | `orases.atlassian.net` | Jira instance hostname |
| `mcp_server` | `claude_ai_Atlassian` | MCP server prefix for Atlassian tools |
| `default_post_action` | `ask` | After generation: `post_to_jira`, `save_locally`, `both`, or `ask` |
| `include_client_summary` | `true` | Generate client-friendly summary section |
| `include_technical_summary` | `true` | Generate technical summary section |
| `local_save_path` | `.claude/work-summaries` | Directory for local summary copies |
| `auto_detect_ticket` | `true` | Extract ticket key from branch name |
| `file_categories` | *(built-in)* | Custom file categorization patterns |
| `client_summary_template` | *(built-in)* | Override path for client summary template |
| `technical_summary_template` | *(built-in)* | Override path for technical summary template |
| `review_display_template` | *(built-in)* | Override path for review display template |

**Note:** Add `.claude/*.local.md` to your `.gitignore` for local settings files.

## Components

| Component | Name | Description |
|-----------|------|-------------|
| Skill | `work-summary:work-summary-generator` | Full workflow orchestrator |
| Skill | `work-summary:client-summary-generator` | Client-friendly summary (standalone capable) |
| Skill | `work-summary:technical-summary-generator` | Technical summary (standalone capable) |
| Command | `/work-summary:work-summary` | Generate and post work summary |
| Command | `/work-summary:setup` | Guided settings configuration |
| Command | `/work-summary:help` | Capabilities and configuration help |
