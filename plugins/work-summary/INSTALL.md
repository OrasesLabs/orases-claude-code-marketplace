# Installation

## Prerequisites

- **Atlassian MCP server** configured for `orases.atlassian.net`
- **Git** repository with feature branches
- **GitHub CLI** (`gh`) installed and authenticated (optional, for PR detection)

## Install from Marketplace

```bash
# Install the entire marketplace (includes this plugin)
claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git
```

## Install Standalone

```bash
# From the plugin directory
cd plugins/work-summary
claude plugin install .
```

## Verify Installation

After installation, verify the plugin is loaded:

1. Run `/work-summary:work-summary` in a git repository with a feature branch checked out
2. The skill should prompt for a Jira ticket key or detect one from the branch name

## Atlassian MCP Configuration

This plugin requires the Atlassian MCP server to be configured in your Claude Code environment.
It uses `getJiraIssue` and `addCommentToJiraIssue` tools via the configured MCP server prefix.
Ensure your MCP server has access to the target Jira project.

If your MCP server prefix differs from the default (`claude_ai_Atlassian`), configure it
in your settings file.

## Configure Settings (Optional)

Create `.claude/work-summary.local.md` in your project root:

```markdown
---
base_branch: auto
atlassian_hostname: orases.atlassian.net
mcp_server: claude_ai_Atlassian
default_post_action: ask
---
```

All settings are optional. See the README for the full settings reference.

Add to `.gitignore`:
```
.claude/*.local.md
```
