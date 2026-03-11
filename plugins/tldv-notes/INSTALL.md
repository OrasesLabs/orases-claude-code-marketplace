# Installation

## Prerequisites

- **TLDV MCP server** configured in Claude Code
- **Atlassian MCP server** configured for Confluence access

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
2. Run `/tldv-notes:generate-meeting-notes dryrun:true` in Claude Code
3. The plugin should prompt for configuration or fetch your TLDV meetings

## MCP Server Configuration

This plugin requires two MCP servers:

### TLDV MCP Server

Provides access to meeting data:
- `mcp__tldv__list-meetings`
- `mcp__tldv__get-meeting-metadata`
- `mcp__tldv__get-transcript`
- `mcp__tldv__get-highlights`

### Atlassian MCP Server

Provides Confluence page creation:
- `mcp__atlassian__createConfluencePage`
- `mcp__atlassian__getConfluenceSpaces`

Ensure both MCP servers are configured and accessible in your Claude Code environment.

## Configuration

After installation, create a settings file for persistent configuration.
See [QUICKSTART.md](QUICKSTART.md) for setup instructions.
