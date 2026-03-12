---
name: work-summary:setup
description: "Configure work-summary plugin settings for this project"
disable-model-invocation: true
---

# Work Summary Plugin — Setup

Guide the user through configuring the work-summary plugin for this project.

## Instructions

Walk the user through each setting interactively. Do not dump all options at once.

### Step 1: Check for Existing Settings

Look for settings files in priority order:
1. `.claude/work-summary.local.md` (project-local)
2. `.claude/work-summary.md` (project-scoped)
3. `~/.claude/work-summary.md` (user-global)

If a settings file is found, show the user their current effective configuration and ask
if they want to modify it. If none found, continue to Step 2.

### Step 2: Gather Settings

Walk through each setting interactively using `AskUserQuestion`:

1. **Base Branch** — "Which branch should changes be compared against?"
   - Options: "Auto-detect (Recommended)" / "review" / "main" / "develop" / "Other"
   - Default: `auto`

2. **Atlassian Hostname** — "What is your Jira hostname?"
   - Default: `orases.atlassian.net`
   - Help: This is the hostname in your Jira URLs (e.g., `yourcompany.atlassian.net`)

3. **Post Action** — "What should happen after generating a summary?"
   - Options: "Ask me each time (Recommended)" / "Always post to Jira" / "Save locally only" / "Post to Jira and save locally"
   - Default: `ask`

4. **Client Summary** — "Include client-friendly summary with QA steps?"
   - Options: "Yes (Recommended)" / "No"
   - Default: `true`

5. **Technical Summary** — "Include technical summary with file categories?"
   - Options: "Yes (Recommended)" / "No"
   - Default: `true`

6. **Local Save Path** — "Where should local summary copies be saved?"
   - Default: `.claude/work-summaries`
   - Help: Relative to project root

7. **Auto-detect Ticket** — "Auto-detect Jira ticket from branch name?"
   - Options: "Yes (Recommended)" / "No"
   - Default: `true`

Only ask about `mcp_server` and `file_categories` if the user indicates they need
non-default values. For most users, the defaults work fine.

### Step 3: Ask Where to Save

Use `AskUserQuestion`:

**"Where should these settings be saved?"**
- **Project-local** (`.claude/work-summary.local.md`) — Only for you, not committed to git
- **Project-shared** (`.claude/work-summary.md`) — Shared with team via git
- **User-global** (`~/.claude/work-summary.md`) — Applies across all your projects

### Step 4: Write Settings File

Create the settings file at the chosen location with YAML frontmatter. Only include settings
that differ from defaults to keep the file clean. Use HTML comments to document available
settings that were left at defaults.

Refer to `${CLAUDE_PLUGIN_ROOT}/skills/work-summary-generator/templates/settings-template.md` for the
complete template and field reference.

### Step 5: Confirm

Confirm success and suggest:
- Run `/work-summary:work-summary` to try it out
- Run `/work-summary:help` for more information about capabilities
- If project-local, remind to add `.claude/*.local.md` to `.gitignore`
