# Orases Claude Code Marketplace

Official Claude Code marketplace for Orases productivity tools and platform integrations.

## About

This marketplace provides a curated collection of Claude Code plugins designed to enhance productivity and streamline workflows with Orases platforms and services. Each plugin extends Claude Code with specialized Skills, scripts, and capabilities that Claude can invoke autonomously or through explicit commands.

## Available Plugins

### [Orases Tools](./orases-tools)

Comprehensive Jira workflow management with direct REST API access.

**Features:**
- **Jira Integration**: View tickets, transition statuses, and manage workflows
- **Skills**: Autonomous Jira operations invoked by Claude based on context
- **Scripts**: Standalone Python utilities for direct API operations
- **Planned**: Confluence integration, custom Orases platform integrations

**Version:** 1.0.0
**Documentation:** [View Plugin README](./orases-tools/README.md)

## Installation

### Install Entire Marketplace

```bash
# Install from GitHub (recommended)
claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git
```

### Install Specific Plugin

```bash
# Clone the repository
git clone git@github.com:OrasesLabs/orases-claude-code-marketplace.git
cd orases-claude-code-marketplace/orases-tools

# Install individual plugin
claude plugin install .
```

## Quick Start

1. **Install the marketplace** using one of the methods above
2. **Configure authentication** - See plugin-specific documentation for setup
3. **Start using** - Ask Claude to perform tasks or use slash commands

For detailed setup instructions, see each plugin's INSTALL.md file.

## Plugin Structure

Each plugin in this marketplace follows Claude Code best practices:

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── skills/                  # Model-invoked capabilities
├── scripts/                 # Standalone utilities
├── docs/                    # Documentation
├── README.md               # Plugin overview
├── INSTALL.md              # Installation guide
├── QUICKSTART.md           # Quick start guide
└── CHANGELOG.md            # Version history
```

## Development

### Adding New Plugins

1. Create plugin directory in marketplace root
2. Add `.claude-plugin/plugin.json` with metadata
3. Update marketplace manifest (`.claude-plugin/marketplace.json`)
4. Add plugin to this README
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
