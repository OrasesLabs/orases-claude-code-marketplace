---
name: work-summary:work-summary-generator
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
Before processing, check for settings in this order (later files override earlier ones):

1. `~/.claude/work-summary.md` - User-global settings (base defaults across all projects)
2. `.claude/work-summary.md` - Project-scoped settings (committable for team defaults)
3. `.claude/work-summary.local.md` - Project-local settings (not committed, gitignored, highest priority)

Parse YAML frontmatter for: `base_branch`, `atlassian_hostname`, `mcp_server`,
`default_post_action`, `include_client_summary`, `include_technical_summary`,
`local_save_path`, `auto_detect_ticket`, `file_categories`, `client_summary_template`,
`technical_summary_template`, `review_display_template`.

If no settings file exists at the project level (neither `.claude/work-summary.local.md` nor
`.claude/work-summary.md`), prompt the user: "No project settings found. Would you like to
configure the plugin now?" If yes, invoke the `/work-summary:setup` command. If no, proceed
with defaults.

### Settings Reference

| Setting | Default | Description |
|---|---|---|
| `base_branch` | `auto` | Branch to diff against. `auto` checks for a beta/development branch, then falls back to `main` |
| `atlassian_hostname` | `orases.atlassian.net` | Jira instance hostname |
| `mcp_server` | `claude_ai_Atlassian` | MCP server prefix for Atlassian tools |
| `default_post_action` | `ask` | After generation: `post_to_jira`, `save_locally`, `both`, or `ask` |
| `include_client_summary` | `true` | Generate the client-friendly summary section |
| `include_technical_summary` | `true` | Generate the technical summary section |
| `local_save_path` | `.claude/work-summaries` | Directory for local summary copies |
| `auto_detect_ticket` | `true` | Extract ticket key from branch name when no argument given |
| `file_categories` | *(built-in)* | Custom file categorization patterns (see references) |
| `client_summary_template` | *(built-in)* | Path to override client summary template |
| `technical_summary_template` | *(built-in)* | Path to override technical summary template |
| `review_display_template` | *(built-in)* | Path to override review display template |

### Interactive Setup Prompts

When prompting for missing settings, use friendly names:

| Setting key | Friendly prompt | Options / Help |
|---|---|---|
| `base_branch` | "Which branch should changes be compared against?" | "Auto-detect (Recommended)" / "review" / "main" / "develop" / "Other" |
| `atlassian_hostname` | "What is your Jira hostname?" | Default: `orases.atlassian.net` |
| `default_post_action` | "What should happen after generating the summary?" | "Ask me each time (Recommended)" / "Post to Jira and save locally" / "Post to Jira only" / "Save locally only" |
| `include_client_summary` | "Include the client-friendly summary?" | "Yes (Recommended)" / "No" |
| `include_technical_summary` | "Include the technical summary?" | "Yes (Recommended)" / "No" |

## Before Starting

**IMPORTANT**: Before executing any steps, create a ToDo list using `TaskCreate` for all 10
steps in the Execution Process below (Steps 1-10). This ensures progress is always trackable,
even after a context compaction. Mark each task `in_progress` when starting it and `completed`
when done. If a compaction occurs, check `TaskList` to determine the current step and resume
from there.

## Ticket Identification

Parse input to identify a Jira ticket key. Accepted formats:

- **Ticket number**: `ABC-123`
- **Full Jira URL**: `https://{ATLASSIAN_HOSTNAME}/browse/ABC-123`
- **Empty input**: Extract from current git branch name (e.g., `{username}-abc-123-feature` -> `ABC-123`)

Fallback: If no ticket can be determined, ask the user via `AskUserQuestion` with the prompt
"Which Jira ticket should this summary be posted to?" and options for any plausible ticket
extracted from the branch, plus an "Other" freeform option.

## Execution Process

### Step 1: Load Configuration

Read settings files in priority order (see Configuration section above). Parse YAML frontmatter
to extract all setting values. For any missing settings, apply defaults from the Settings
Reference table. Store resolved settings for use in subsequent steps.

If no project-level settings file exists, prompt the user to run `/work-summary:setup` or
continue with defaults.

### Step 2: Identify Ticket and Validate Branch

1. Parse the provided arguments or extract ticket key from current branch name
2. If ambiguous, use `AskUserQuestion` to confirm
3. Check if the current branch is the base branch itself. If so, warn the user via
   `AskUserQuestion`: "Current branch is {branch}. Which feature branch should be
   summarized?" with options for any recent feature branches, plus an "Other" option.
   Do not proceed with git comparison against the same branch.

### Step 3: Verify Ticket with Jira

Fetch the Jira ticket details using available Atlassian MCP tools. The `atlassian_hostname`
from settings identifies the Jira instance. The `mcp_server` setting provides the MCP server
prefix, but tool names may vary depending on the MCP server configuration — use the
appropriate tool for fetching a Jira issue.

Request these fields at minimum: `summary`, `status`, `description`, `comment`, `issuelinks`.
Avoid requesting heavy fields like changelog, worklog, or attachment unless needed. Use
informed judgement to include additional fields (including custom fields) when they appear
relevant to the ticket context.

After receiving the ticket data, present confirmation to the user via `AskUserQuestion`:
- Question: "Generate work summary for {TICKET_KEY}: {Title}?"
- Options: "Yes, proceed" / "No, wrong ticket"
- On rejection: ask for the correct ticket identifier

Retain the ticket description and comments for use in later steps.

### Step 4: Analyze Git Changes

First, determine the base branch for comparison. If the `base_branch` setting is not `auto`,
use that value directly. Otherwise, auto-detect by checking for a beta/development branch
(e.g., `review`, `develop`, `staging`) and falling back to `main`:
- Run `git rev-parse --verify {branch} 2>/dev/null` for candidate branches
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
Otherwise, load the default patterns from `${CLAUDE_PLUGIN_ROOT}/skills/technical-summary-generator/references/file-categories.md`.

Record: branch name, commit count, file count, files-by-category, and change statistics.

### Step 5: Gather PR/Merge Request Information

Check for an existing pull request or merge request. The repository may use CodeCommit,
GitHub, GitLab, or another hosting service:

1. First check if this is an AWS CodeCommit repository: `git remote -v | grep codecommit`
   - If CodeCommit: `aws codecommit list-pull-requests --repository-name {REPO} --pull-request-status OPEN 2>/dev/null` and filter for the current branch
2. If not CodeCommit, try GitHub: `gh pr view --json url,state 2>/dev/null`
3. If neither works, check for other remotes and attempt appropriate CLI tools

If a PR/MR exists: record URL and state. If none found: note absence — the summary can
still be posted without one.

### Step 6: Generate Client-Friendly Summary

Skip this step if `include_client_summary` is `false` in settings.

Load the `work-summary:client-summary-generator` skill and execute it, passing the Jira
ticket context (from Step 3) and git change data (from Step 4).

If a `client_summary_template` path is configured in settings, pass that to the skill as
the template override.

### Step 7: Generate Technical Summary

Skip this step if `include_technical_summary` is `false` in settings.

Load the `work-summary:technical-summary-generator` skill and execute it, passing the git
change data (from Step 4) and file categorization patterns.

If a `technical_summary_template` path is configured in settings, pass that to the skill as
the template override.

### Step 8: User Review & Approval

Present both summaries using the review display format. Load the template from
`${CLAUDE_SKILL_DIR}/templates/review-display-format.md`, or use the
`review_display_template` override path from settings if configured. Include:
- Ticket key, title, branch name, commit count, files modified
- Client-friendly summary (if generated)
- Technical summary (if generated)
- PR/MR link (if available)

If `default_post_action` is `both`, skip the prompt and proceed to Step 9 then Step 10.
If `default_post_action` is `post_to_jira`, skip the prompt and proceed to Step 9 (skip Step 10).
If `default_post_action` is `save_locally`, skip the prompt and proceed to Step 10 (skip Step 9).
Otherwise (default `ask`), ask via `AskUserQuestion`:
- Question: "What would you like to do with this summary?"
- Options: "Post to Jira and save locally" / "Post to Jira only" / "Save locally only" / "Edit first"
- If "Edit first": display summaries and await freeform edit instructions, then re-present

### Step 9: Post to Jira

Post the combined summary as a comment on the Jira ticket. Use available Atlassian MCP tools
to add the comment — the specific tool name may vary depending on the MCP server configuration.
The `atlassian_hostname` from settings identifies the target Jira instance.

Post the combined Markdown content as the comment body. Confirm the comment was posted
successfully and report the result to the user.

If posting fails, refer to the error handling guide and offer to save locally instead.

### Step 10: Save Local Copy

Use the `local_save_path` setting (default: `.claude/work-summaries`) for the save directory.
Check if `{LOCAL_SAVE_PATH}/{TICKET_KEY}.md` (relative to project root) already exists.

**If the file exists**, ask the user via `AskUserQuestion`:
- Question: "A summary for {TICKET_KEY} already exists. How should this be handled?"
- Options:
  - "Append to existing" - Add a timestamped separator and append the new summary below the existing content
  - "Overwrite" - Replace the existing file with the new summary
  - "Create new version" - Save as `{LOCAL_SAVE_PATH}/{TICKET_KEY}-{YYYY-MM-DD}.md`

**If the file does not exist**, create it directly.

Refer to `${CLAUDE_SKILL_DIR}/templates/local-summary-template.md` for the file structure.

## Error Handling

Refer to `${CLAUDE_SKILL_DIR}/references/error-handling-guide.md` for recovery actions for common failure scenarios
including ticket access issues, empty branches, posting failures, and ambiguous branch names.

## Additional Resources

### Templates
- **`${CLAUDE_PLUGIN_ROOT}/skills/client-summary-generator/templates/client-summary-template.md`** - Markdown structure for the client-friendly summary section
- **`${CLAUDE_PLUGIN_ROOT}/skills/technical-summary-generator/templates/technical-summary-template.md`** - Markdown structure for the technical summary section
- **`${CLAUDE_SKILL_DIR}/templates/review-display-format.md`** - Combined display format for user review and Jira posting
- **`${CLAUDE_SKILL_DIR}/templates/local-summary-template.md`** - File structure for local summary storage
- **`${CLAUDE_SKILL_DIR}/templates/settings-template.md`** - Settings file template and field reference

### References
- **`${CLAUDE_SKILL_DIR}/references/error-handling-guide.md`** - Error scenarios and recovery guidance
- **`${CLAUDE_PLUGIN_ROOT}/skills/technical-summary-generator/references/file-categories.md`** - Default file categorization patterns and custom category examples

### Related Skills
- **`work-summary:client-summary-generator`** - Standalone client-friendly summary generation
- **`work-summary:technical-summary-generator`** - Standalone technical summary generation
