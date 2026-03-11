# Installation

## Prerequisites

- **Atlassian MCP server** configured for your Jira instance
- **Git** repository with feature branches
- **AWS CLI** configured (for CodeCommit PR detection) or **GitHub CLI** (`gh`) authenticated (for GitHub PR detection) — optional

## Install from Marketplace

```bash
# Add the Orases marketplace (one-time)
/plugin marketplace add OrasesLabs/orases-claude-code-marketplace

# Or with full SSH URL
/plugin marketplace add git@github.com:OrasesLabs/orases-claude-code-marketplace.git
```

You can also use the **interactive plugin manager** inside Claude Code — run `/plugin`
and browse the **Discover** tab to install available plugins.

## Install from Local Clone (Development)

```bash
git clone git@github.com:OrasesLabs/orases-claude-code-marketplace.git
cd orases-claude-code-marketplace
claude plugin install .
```

## Verify Installation

After installation, verify the plugin is loaded:

1. Run `/plugin` to open the interactive plugin manager and check the **Installed** tab
2. Run `/work-summary:help` to see the capabilities overview
3. Run `/work-summary:work-summary` in a git repository with a feature branch checked out
4. The skill should prompt for a Jira ticket key or detect one from the branch name

## Atlassian MCP Configuration

This plugin requires an Atlassian MCP server configured in your Claude Code environment.
It uses Jira tools for fetching ticket details and posting comments. The specific tool names
depend on your MCP server configuration — the plugin adapts automatically.

If your MCP server prefix differs from the default (`claude_ai_Atlassian`), configure it
in your settings file via the `mcp_server` setting.

## Configure Settings

Run the guided setup:

```
/work-summary:setup
```

Or create `.claude/work-summary.local.md` in your project root manually:

```markdown
---
base_branch: auto
atlassian_hostname: orases.atlassian.net
default_post_action: ask
---
```

All settings are optional. See the README for the full settings reference.

Add to `.gitignore`:
```
.claude/*.local.md
```
