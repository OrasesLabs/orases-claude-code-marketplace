# Installation

## Prerequisites

- **TLDV MCP server** configured in Claude Code
- **Atlassian MCP server** configured for Confluence access

## Install from Marketplace

```bash
# Install the entire marketplace (includes this plugin)
claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git
```

## Install Standalone

```bash
# From the plugin directory
cd plugins/tldv-notes
claude plugin install .
```

## Verify Installation

After installation, verify the plugin is loaded:

1. Run `/tldv-notes:meeting-notes dryrun:true` in Claude Code
2. The plugin should prompt for configuration or fetch your TLDV meetings

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
