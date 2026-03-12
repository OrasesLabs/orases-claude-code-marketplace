---
name: work-summary:help
description: "Learn about the work-summary plugin, configure settings, and customize templates"
disable-model-invocation: true
---

# Work Summary Plugin — Help & Setup

Guide the user through understanding, configuring, and customizing the work-summary plugin.

## Instructions

When the user runs this command, present a welcome overview and then ask what they'd like
help with. Walk them through each topic interactively — do not dump everything at once.

### Step 1: Welcome Overview

Display this summary:

> **Work Summary Plugin** generates comprehensive work summaries from git branch changes
> and posts them as structured Jira comments. It produces client-friendly summaries
> (QA steps, testing checklists) and technical summaries (architecture, file categories,
> commits) for stakeholder visibility.
>
> **Commands:**
> - `/work-summary:work-summary [ABC-123]` — Generate and post a work summary
> - `/work-summary:setup` — Configure plugin settings
> - `/work-summary:help` — This help guide
>
> **Skills (also triggered by natural language):**
> - `work-summary:work-summary-generator` — Full workflow orchestrator
> - `work-summary:client-summary-generator` — Client-friendly summary (standalone)
> - `work-summary:technical-summary-generator` — Technical summary (standalone)

### Step 2: Ask What They Need

Use `AskUserQuestion`:

**"What would you like help with?"**
- **Get started** — Set up the plugin for first use
- **How it works** — Learn about the workflow and what gets generated
- **Customize settings** — Change base branch, post action, summary toggles, etc.
- **Customize templates** — Override the summary templates
- **View current settings** — Show what's currently configured

Then follow the appropriate path below.

---

## Path: Get Started

### Step A: Check for Existing Settings

Look for settings files in priority order:
1. `.claude/work-summary.local.md` (project-local)
2. `.claude/work-summary.md` (project-scoped)
3. `~/.claude/work-summary.md` (user-global)

If a settings file is found, show current configuration and offer to modify. If none found,
offer to run `/work-summary:setup` or proceed with defaults.

### Step B: Explain Prerequisites

> **What the plugin needs:**
> - A git repository with feature branches
> - An Atlassian MCP server connection (for fetching Jira tickets and posting comments)
> - A code repository hosting service (CodeCommit, GitHub, etc.) for PR detection (optional)

### Step C: Quick Test

Suggest the user try:
1. Check out a feature branch
2. Run `/work-summary:work-summary` (with or without a ticket key)
3. Follow the interactive prompts

---

## Path: How It Works

Explain the 10-step workflow:

1. **Load Configuration** — Read settings from user, project, and local config files
2. **Identify Ticket** — Parse argument, extract from branch name, or ask
3. **Verify Ticket** — Fetch Jira ticket details and confirm with user
4. **Analyze Git Changes** — Gather commits, modified files, and change statistics
5. **Gather PR Info** — Check for existing pull/merge requests
6. **Generate Client Summary** — Business-level summary with QA steps (uses `work-summary:client-summary-generator` skill)
7. **Generate Technical Summary** — Developer-level summary with file categories (uses `work-summary:technical-summary-generator` skill)
8. **User Review** — Present summaries for approval or editing
9. **Post to Jira** — Add structured comment to the Jira ticket
10. **Save Local Copy** — Store summary locally for audit trail

Explain that steps 6 and 7 can be independently toggled via settings, and the corresponding
skills can be used standalone outside the full workflow.

---

## Path: Customize Settings

### Step A: Show Current Configuration

Read settings from all locations and display the effective (merged) configuration, noting
where each value comes from and which are defaults.

### Step B: Present Available Settings

| Setting | Current | Default | Description |
|---|---|---|---|
| `base_branch` | | `auto` | Branch to diff against |
| `atlassian_hostname` | | `orases.atlassian.net` | Jira instance hostname |
| `mcp_server` | | `claude_ai_Atlassian` | MCP server prefix |
| `default_post_action` | | `ask` | Post behavior after generation |
| `include_client_summary` | | `true` | Generate client-friendly section |
| `include_technical_summary` | | `true` | Generate technical section |
| `local_save_path` | | `.claude/work-summaries` | Local save directory |
| `auto_detect_ticket` | | `true` | Extract ticket from branch name |
| `file_categories` | | *(built-in)* | File categorization patterns |
| `client_summary_template` | | *(built-in)* | Override path for client template |
| `technical_summary_template` | | *(built-in)* | Override path for technical template |
| `review_display_template` | | *(built-in)* | Override path for review template |

### Step C: Modify

Use `AskUserQuestion` to ask which settings to change. For each, present the available
options. Then offer to run `/work-summary:setup` for a guided walkthrough, or edit the
settings file directly.

---

## Path: Customize Templates

### Step A: Explain Template System

> The plugin uses template files to control how summaries are structured:
>
> - **`client-summary-template.md`** — Client-friendly summary structure
> - **`technical-summary-template.md`** — Technical summary structure
> - **`review-display-format.md`** — Combined display format for review and Jira posting
> - **`local-summary-template.md`** — Local file storage structure
>
> Override any template by setting its path in your settings file:
> ```yaml
> client_summary_template: .claude/work-summary-templates/client-summary.md
> technical_summary_template: .claude/work-summary-templates/technical-summary.md
> review_display_template: .claude/work-summary-templates/review-display.md
> ```

### Step B: Show Built-in Templates

Offer to show the contents of any built-in template so the user can copy and customize it.

### Step C: Create Override

If the user wants to override a template:
1. Read the built-in version from `${CLAUDE_PLUGIN_ROOT}/skills/work-summary-generator/templates/`
2. Show the user the current content
3. Ask what they'd like to change
4. Write the customized version to the user's chosen override path
5. Update the settings file to point to the override

---

## Path: View Current Settings

### Step A: Check All Locations

Read settings from all three locations (if they exist):
1. `~/.claude/work-summary.md` (user-global)
2. `.claude/work-summary.md` (project-scoped)
3. `.claude/work-summary.local.md` (project-local)

### Step B: Show Effective Configuration

Display:
- Which settings files were found and their locations
- The effective (merged) configuration, noting where each value comes from
- Any template overrides configured
- Default values for any unset settings

### Step C: Offer Next Steps

Ask if they'd like to modify settings, customize templates, or run a work summary.
