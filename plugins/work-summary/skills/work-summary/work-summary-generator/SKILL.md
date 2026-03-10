---
name: work-summary-generator
description: >-
  This skill should be used when the user invokes "/work-summary", asks to
  "generate a work summary", "post a work summary to Jira", "summarize my
  changes", "summarize this branch", "write up my work for Jira", or
  "create a Jira comment from my branch". Generates client-friendly and
  technical summaries from git branch changes and posts them as structured
  Jira comments.
---

# Work Summary

Generate comprehensive work summaries from git branch changes and post to Jira as structured
comments. Produces both a client-friendly summary (business impact, QA steps) and a technical
summary (architecture, files, commits) for stakeholder visibility.

## Configuration

This plugin supports per-user and per-project configuration via settings files.
Before processing, check for settings in this order:

1. `.claude/work-summary.local.md` - Project-local settings (not committed, gitignored)
2. `.claude/work-summary.md` - Project-scoped settings (can be committed for team defaults)
3. `~/.claude/work-summary.md` - User-global settings (applies across all projects)

Parse YAML frontmatter for: `base_branch`, `atlassian_hostname`, `mcp_server`, `default_post_action`, `include_client_summary`, `include_technical_summary`, `local_save_path`, `auto_detect_ticket`, `file_categories`.

If no settings file exists, use the defaults below and proceed. When a required value
cannot be determined (e.g., base branch detection fails), ask the user and offer to save
the value to a settings file for future runs.

### Settings Reference

| Setting | Default | Description |
|---|---|---|
| `base_branch` | `auto` | Branch to diff against. `auto` checks for `review` then `main` |
| `atlassian_hostname` | `orases.atlassian.net` | Jira instance hostname |
| `mcp_server` | `claude_ai_Atlassian` | MCP server prefix for Atlassian tools |
| `default_post_action` | `ask` | After generation: `post_to_jira`, `save_locally`, or `ask` |
| `include_client_summary` | `true` | Generate the client-friendly summary section |
| `include_technical_summary` | `true` | Generate the technical summary section |
| `local_save_path` | `.claude/work-summaries` | Directory for local summary copies |
| `auto_detect_ticket` | `true` | Extract ticket key from branch name when no argument given |
| `file_categories` | *(built-in)* | Custom file categorization patterns (see Step 3) |

### Interactive Setup Prompts

When prompting for missing settings, use friendly names:

| Setting key | Friendly prompt | Options / Help |
|---|---|---|
| `base_branch` | "Which branch should changes be compared against?" | "Auto-detect (Recommended)" / "review" / "main" / "Other" |
| `atlassian_hostname` | "What is your Jira hostname?" | Default: `orases.atlassian.net` |
| `default_post_action` | "What should happen after generating the summary?" | "Ask me each time (Recommended)" / "Always post to Jira" / "Save locally only" |
| `include_client_summary` | "Include the client-friendly summary?" | "Yes (Recommended)" / "No" |
| `include_technical_summary` | "Include the technical summary?" | "Yes (Recommended)" / "No" |

## Before Starting

**IMPORTANT**: Before executing any steps, create a ToDo list using `TaskCreate` for all 10
steps in the Execution Process below (Steps 0-9). This ensures progress is always trackable,
even after a context compaction. Mark each task `in_progress` when starting it and `completed`
when done. If a compaction occurs, check `TaskList` to determine the current step and resume
from there.

## Ticket Identification

Parse input to identify a Jira ticket key. Accepted formats:

- **Ticket number**: `ABC-123`
- **Full Jira URL**: `https://orases.atlassian.net/browse/ABC-123`
- **Empty input**: Extract from current git branch name (e.g., `{username}-abc-123-feature` -> `ABC-123`)

Fallback: If no ticket can be determined, ask the user via `AskUserQuestion` with the prompt
"Which Jira ticket should this summary be posted to?" and options for any plausible ticket
extracted from the branch, plus an "Other" freeform option.

## Execution Process

### Step 0: Load Configuration

Read settings files in priority order (see Configuration section above). Parse YAML frontmatter
to extract all setting values. For any missing settings, apply defaults from the Settings
Reference table. Store resolved settings for use in subsequent steps.

### Step 1: Identify Ticket and Validate Branch

1. Parse the provided arguments or extract ticket key from current branch name
2. If ambiguous, use `AskUserQuestion` to confirm
3. Check if the current branch is the base branch itself (`review` or `main`). If so, warn
   the user via `AskUserQuestion`: "Current branch is {branch}. Which feature branch should
   be summarized?" with options for any recent feature branches, plus an "Other" option.
   Do not proceed with git comparison against the same branch.

### Step 2: Verify Ticket with Jira

Use the `Agent` tool with `subagent_type: "general-purpose"` to fetch ticket details from Jira. Agent instructions:

> Fetch Jira issue {TICKET_KEY} using the Atlassian MCP tool `mcp__{MCP_SERVER}__getJiraIssue`.
> The Atlassian hostname is `{ATLASSIAN_HOSTNAME}`.
> Request only these fields: `summary`, `status`, `description`, `comment`, `issuelinks`.
> Do NOT request: changelog, worklog, attachment, subtasks, watches, votes, or any
> customfield_* fields - these are heavy and irrelevant.
> Return: ticket title, current status, description text, all comment bodies (with author
> and date), and any linked issue keys with their link type (e.g., "blocks ABC-456",
> "is related to ABC-789").

Replace `{MCP_SERVER}` with the `mcp_server` setting value (default: `claude_ai_Atlassian`)
and `{ATLASSIAN_HOSTNAME}` with the `atlassian_hostname` setting value (default: `orases.atlassian.net`).

After receiving the ticket data, present confirmation to the user via `AskUserQuestion`:
- Question: "Generate work summary for {TICKET_KEY}: {Title}?"
- Options: "Yes, proceed" / "No, wrong ticket"
- On rejection: ask for the correct ticket identifier

Retain the ticket description and comments for use in Step 5.

### Step 3: Analyze Git Changes

First, determine the base branch for comparison. If the `base_branch` setting is not `auto`,
use that value directly. Otherwise, auto-detect:
- Run `git rev-parse --verify review 2>/dev/null` and `git rev-parse --verify main 2>/dev/null`
- Use `review` if it exists, otherwise fall back to `main`
- Store the result as `{BASE_BRANCH}` for all subsequent commands

If the current branch IS the base branch (i.e., the feature was already merged), locate the
relevant commits using `git log --all --oneline --grep="{TICKET_KEY}"`. Use the most recent
matching commit hash to gather changes via:

- `git show {COMMIT_HASH} --format="%h: %s%n%b"` - commit message and body
- `git diff {COMMIT_HASH}^..{COMMIT_HASH} --name-only` - modified files
- `git diff {COMMIT_HASH}^..{COMMIT_HASH} --stat` - change statistics

For squash commits, the body typically contains the original individual commit messages.
Extract those as the commit list.

If on a feature branch (not the base branch), run these bash commands to gather branch
change data:

- `git branch --show-current` - current branch name
- `git log {BASE_BRANCH}...HEAD --pretty=format:"%h: %s"` - commit messages with short hashes
- `git diff {BASE_BRANCH}...HEAD --name-only` - list of all modified files
- `git diff {BASE_BRANCH}...HEAD --stat` - additions/deletions statistics

Categorize modified files by type. If `file_categories` is set in settings, use those patterns.
Otherwise, load the default patterns from `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/references/file-categories.md`.

Record: branch name, commit count, file count, files-by-category, and change statistics.

### Step 4: Gather PR/Deployment Information

1. Check for an existing PR: `gh pr view --json url,state 2>/dev/null`
2. If PR exists: record URL and state (Open/Merged/etc.)
3. If no PR: note absence - the summary can still be posted without one

### Step 5: Generate Client-Friendly Summary

Skip this step if `include_client_summary` is `false` in settings.

This summary targets non-technical stakeholders. Every claim must be grounded in actual code
changes or ticket data - never assume or fabricate QA steps.

**Process:**

1. Review the Jira ticket description and comments (from Step 2) for acceptance criteria,
   scope decisions, and context added after ticket creation
2. Read modified controller and template files to understand user-facing behavior changes
3. If acceptance criteria exist, cross-reference each against actual code changes
4. Build QA steps only from verified, observable behavior changes
5. Flag any acceptance criteria that could not be mapped to code changes

**Sections to produce:**
- **What Changed**: Business-level description of modifications
- **QA Steps**: Numbered validation steps derived from code inspection, not guessed
- **Related Tasks**: Links to related tickets from issue links (Step 2) and mentions in comments
- **Testing Checklist**: Acceptance criteria checkboxes, each verified against code

After generating, display the QA Steps and Testing Checklist as plain text output so the user
can read them. Then ask via `AskUserQuestion`:
- Question: "Are these QA steps and testing items accurate?"
- Options: "Yes, looks good" / "Needs changes"
- If "Needs changes": await freeform feedback with corrections

Refer to `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/client-summary-template.md` for the complete Markdown structure.

### Step 6: Generate Technical Summary

Skip this step if `include_technical_summary` is `false` in settings.

This summary targets developers and maintainers. Build from git data gathered in Step 3.

**Sections to produce:**
- **Architecture & Implementation**: Pattern changes, new abstractions, integration points
- **Modified Files**: Categorized list with per-category file counts and line change totals
- **Commits**: All commit hashes and messages from the branch
- **Testing Coverage**: Unit/integration test files added or modified
- **Code Quality**: Standards compliance, deprecations addressed
- **Performance Notes**: Query changes, caching impact (only if applicable)

Refer to `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/technical-summary-template.md` for the complete Markdown structure.

### Step 7: User Review & Approval

Present both summaries using the format in `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/review-display-format.md`. Include:
- Ticket key, title, branch name, commit count, files modified
- Client-friendly summary
- Technical summary
- PR link (if available)

If `default_post_action` is `post_to_jira`, skip the prompt and proceed to Step 8.
If `default_post_action` is `save_locally`, skip the prompt and proceed to Step 9.
Otherwise (default `ask`), ask via `AskUserQuestion`:
- Question: "Post this summary to Jira?"
- Options: "Yes, post to Jira" / "Edit first" / "Save locally only"
- If "Edit first": display summaries and await freeform edit instructions, then re-present

### Step 8: Post to Jira

Use the `Agent` tool with `subagent_type: "general-purpose"` to post the comment. Agent instructions:

> Add a comment to Jira issue {TICKET_KEY} using the Atlassian MCP tool
> `mcp__{MCP_SERVER}__addCommentToJiraIssue`. The Atlassian hostname is `{ATLASSIAN_HOSTNAME}`.
> Post the following Markdown content as the comment body:
> {COMBINED_SUMMARY_MARKDOWN}
> Confirm the comment was posted successfully and return the comment URL if available.

Replace `{MCP_SERVER}` and `{ATLASSIAN_HOSTNAME}` with values from settings.

Report success or failure to the user.

### Step 9: Save Local Copy

Use the `local_save_path` setting (default: `.claude/work-summaries`) for the save directory.
Check if `{LOCAL_SAVE_PATH}/{TICKET_KEY}.md` (relative to project root) already exists.

**If the file exists**, ask the user via `AskUserQuestion`:
- Question: "A summary for {TICKET_KEY} already exists. How should this be handled?"
- Options:
  - "Append to existing" - Add a timestamped separator and append the new summary below the existing content
  - "Overwrite" - Replace the existing file with the new summary
  - "Create new version" - Save as `{LOCAL_SAVE_PATH}/{TICKET_KEY}-{YYYY-MM-DD}.md`

**If the file does not exist**, create it directly.

Refer to `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/local-summary-template.md` for the file structure.

## Error Handling

Refer to `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/references/error-handling-guide.md` for recovery actions for common failure scenarios
including ticket access issues, empty branches, posting failures, and ambiguous branch names.

## Additional Resources

### Templates
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/client-summary-template.md`** - Markdown structure for the client-friendly summary section
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/technical-summary-template.md`** - Markdown structure for the technical summary section
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/review-display-format.md`** - Combined display format for user review and Jira posting
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/local-summary-template.md`** - File structure for local summary storage
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/settings-template.md`** - Settings file template and field reference

### References
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/references/error-handling-guide.md`** - Error scenarios and recovery guidance
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/references/file-categories.md`** - Default file categorization patterns and custom category examples
