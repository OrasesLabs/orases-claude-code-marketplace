# Orases Claude Code Marketplace

Official Claude Code marketplace for Orases productivity tools and platform integrations.

## About

This marketplace provides a curated collection of Claude Code plugins designed to enhance productivity and streamline workflows with Orases platforms and services. Each plugin extends Claude Code with specialized Skills, scripts, and capabilities that Claude can invoke autonomously or through explicit commands.

## Available Plugins

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

### [Docs Management](./plugins/docs-management) (v1.0.0)

Documentation management plugin with Diátaxis framework support for creating, organizing, and maintaining project documentation following industry standards.

**Features:**
- **Diátaxis Framework**: Organize docs into Tutorials, How-to Guides, Reference, and Explanation
- **Templates & Standards**: Ready-to-use templates with type-specific quality checklists
- **Writer Skills**: Specialized skills for tutorials, how-to guides, tech specs, ADRs, and more
- **Git Integration**: Update documentation based on recent code changes
- **Coverage Auditing**: Identify documentation gaps and outdated content
- **Project Setup**: Initialize standard documentation structure for new projects

**Category:** Documentation
**Documentation:** [View Plugin README](./plugins/docs-management/README.md)

---

### [TLDV Notes](./plugins/tldv-notes) (v1.2.1)

Create Confluence pages from TLDV meeting recordings with structured notes, discussion topics, and action items.

**Features:**
- **Meeting Processing**: Fetches meetings from TLDV where you participated
- **Structured Notes**: Generates summaries, discussion notes, and action items
- **Confluence Publishing**: Creates formatted pages automatically
- **Configurable Formatting**: Customize duration rounding, summary style, action item grouping, and more
- **Template Overrides**: Customize page layout and section templates
- **Dry Run Mode**: Preview notes before publishing

**Category:** Productivity
**Documentation:** [View Plugin README](./plugins/tldv-notes/README.md)

---

## Installation

### Prerequisites

- [Claude Code CLI](https://docs.claude.com/en/docs/claude-code) installed and configured
- Git (for cloning the repository)
- Python 3.6+ (for script-based plugins)

### Option 1: Install Entire Marketplace (Recommended)

This installs all plugins at once from the GitHub repository.

```bash
# Install marketplace directly from GitHub (shorthand)
claude plugin marketplace add OrasesLabs/orases-claude-code-marketplace

# Or with full SSH URL
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

### Verifying Installation

After installation, verify the plugins are loaded:

```bash
# Open the plugin manager (interactive interface)
/plugin

# Or list configured marketplaces
/plugin marketplace list
```

The `/plugin` command opens an interactive interface with tabs for **Discover**, **Installed**, **Marketplaces**, and **Errors**.

### Plugin-Specific Configuration

Some plugins require additional configuration after installation. See each plugin's README and INSTALL.md for setup instructions.

### Updating Plugins

To update to the latest version:

```bash
# Update the marketplace
/plugin marketplace update orases-claude-code-marketplace

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
- `/tldv-notes:generate-meeting-notes` (TLDV Notes)
- "Summarize my meetings to Confluence" (TLDV Notes)
- `/analyze-workflow` (Workflow Analyzer)
- "Create a process flow diagram for this workflow" (BA Toolkit)
- `/docs-management:create-how-to deploying to production` (Docs Management)
- `/docs-management:review-coverage` (Docs Management)

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
