# Orases Claude Code Marketplace

Official Claude Code marketplace for Orases productivity tools and platform integrations.

## About

This marketplace provides a curated collection of Claude Code plugins designed to enhance productivity and streamline workflows with Orases platforms and services. Each plugin extends Claude Code with specialized Skills, scripts, and capabilities that Claude can invoke autonomously or through explicit commands.

## Available Plugins

### [Jira Tools](./plugins/jira-tools) (v1.1.0)

Comprehensive Jira workflow management with direct REST API access.

**Features:**
- **Jira Integration**: View tickets, transition statuses, link issues, and manage workflows
- **Skills**: Autonomous Jira operations invoked by Claude based on context
- **Scripts**: Standalone Python utilities for direct API operations
- **Planned**: Confluence integration, custom Orases platform integrations

**Category:** Productivity
**Documentation:** [View Plugin README](./plugins/jira-tools/README.md)

---

### [Workflow Analyzer](./plugins/workflow-analyzer) (v0.1.0)

Advanced workflow analysis and optimization tools for Claude Code development sessions.

**Features:**
- **Session Discovery**: Find and list all Claude Code sessions from logs
- **Transcript Condensing**: Compress large session transcripts for efficient review
- **Workflow Analysis**: Comprehensive session analysis via specialized agent
- **Event Hooks**: Automatic session tracking and transcript backups
- **Slash Command**: `/analyze-workflow` for quick workflow analysis

**Category:** Analysis
**Documentation:** [View Plugin README](./plugins/workflow-analyzer/README.md)

---

### [BA Toolkit](./plugins/ba-toolkit) (v0.1.0)

Business analysis toolkit that transforms written workflow descriptions into visual process flow diagrams.

**Features:**
- **Process Visualization**: Convert text-based workflow steps into interactive diagrams
- **Browser-Based**: Generates HTML diagrams viewable in any web browser
- **Clickable Elements**: Interactive nodes for exploring workflow details
- **Export Ready**: Diagrams suitable for documentation and presentations

**Category:** Visualization
**Documentation:** [View Plugin README](./plugins/ba-toolkit/README.md)

---

## Installation

### Prerequisites

- [Claude Code CLI](https://docs.claude.com/en/docs/claude-code) installed and configured
- Git (for cloning the repository)
- Python 3.6+ (for jira-tools scripts)

### Option 1: Install Entire Marketplace (Recommended)

This installs all plugins at once from the GitHub repository.

```bash
# Install marketplace directly from GitHub
claude plugin marketplace add git@github.com:OrasesLabs/orases-claude-code-marketplace.git
```

### Option 2: Install from Local Clone

Clone the repository first, then install locally.

```bash
# Clone the repository
git clone git@github.com:OrasesLabs/orases-claude-code-marketplace.git
cd orases-claude-code-marketplace

# Install all plugins from the marketplace root
claude plugin install .
```

### Option 3: Install Individual Plugins

Install only the plugins you need.

```bash
# Clone the repository
git clone git@github.com:OrasesLabs/orases-claude-code-marketplace.git

# Install jira-tools only
cd orases-claude-code-marketplace/plugins/jira-tools
claude plugin install .

# Or install workflow-analyzer only
cd orases-claude-code-marketplace/plugins/workflow-analyzer
claude plugin install .

# Or install ba-toolkit only
cd orases-claude-code-marketplace/plugins/ba-toolkit
claude plugin install .
```

### Verifying Installation

After installation, verify the plugins are loaded:

```bash
# List installed plugins
claude plugin list

# You should see the installed plugins listed
```

### Plugin-Specific Configuration

Some plugins require additional configuration:

**Jira Tools** - Requires Atlassian API credentials:
```bash
# Set environment variables (add to your shell profile)
export ATLASSIAN_EMAIL="your-email@company.com"
export ATLASSIAN_API_TOKEN="your-api-token"
export ATLASSIAN_SITE="yoursite.atlassian.net"

# Test the connection
python3 plugins/jira-tools/scripts/test_connection.py
```

See [Jira Tools INSTALL.md](./plugins/jira-tools/INSTALL.md) for detailed setup instructions.

### Updating Plugins

To update to the latest version:

```bash
# If installed from GitHub marketplace
claude plugin marketplace update orases-marketplace

# If installed locally, pull latest and reinstall
cd orases-claude-code-marketplace
git pull
claude plugin install .
```

## Quick Start

1. **Install the marketplace** using one of the methods above
2. **Configure authentication** - See plugin-specific documentation for setup
3. **Start using** - Ask Claude to perform tasks or use slash commands

**Example Commands:**
- "Show me PROJ-123" (Jira Tools)
- "Transition PROJ-123 to In Progress" (Jira Tools)
- `/analyze-workflow` (Workflow Analyzer)
- "Create a process flow diagram for this workflow" (BA Toolkit)

For detailed setup instructions, see each plugin's README.md file.

## Plugin Structure

Each plugin in this marketplace follows Claude Code best practices:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── skills/                  # Model-invoked capabilities
├── agents/                  # Specialized AI agents (optional)
├── hooks/                   # Event-driven automation (optional)
├── commands/                # Slash commands (optional)
├── scripts/                 # Standalone utilities (optional)
├── README.md               # Complete documentation
└── CHANGELOG.md            # Version history
```

## Development

### Adding New Plugins

1. Create plugin directory under `plugins/`
2. Add `.claude-plugin/plugin.json` with metadata
3. Update marketplace manifest (`.claude-plugin/marketplace.json`)
4. Add plugin section to this README
5. Follow Claude Code plugin best practices

### Contributing

Contributions are welcome! Please:

1. Create a new branch for your feature
2. Follow existing structure and conventions
3. Test thoroughly before submitting
4. Update documentation and changelogs
5. Submit pull request with clear description

## Support

- **Repository**: https://github.com/OrasesLabs/orases-claude-code-marketplace
- **Issues**: https://github.com/OrasesLabs/orases-claude-code-marketplace/issues
- **Documentation**: See individual plugin READMEs

## Resources

- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
- [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
- [Claude Code Plugins Guide](https://docs.claude.com/en/docs/claude-code/plugins)

## License

MIT License - See individual plugin LICENSE files for details.

---

**Maintained by:** Orases
**Repository:** https://github.com/OrasesLabs/orases-claude-code-marketplace
