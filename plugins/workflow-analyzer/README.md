# Workflow Analyzer - Claude Code Plugin

Advanced workflow analysis and optimization tools for Claude Code. Analyzes development patterns, tracks session transcripts, and provides intelligent recommendations to optimize your development workflow.

## Features

### 🔍 Analysis Tools
- **Session Discovery** - Find and list all Claude Code sessions from logs
- **Transcript Condensing** - Compress large session transcripts for efficient review
- **Workflow Analysis** - Comprehensive session analysis via specialized agent
- **Pattern Detection** - Identify recurring issues and automation opportunities (planned)

### 🤖 Components

**Skills** (Model-invoked):
- `session-analyzer` - Discovers and lists Claude Code session transcripts
- `transcript-condenser` - Condenses verbose transcripts into readable summaries
- `workflow-analysis`, `pattern-detection`, `optimization-suggestions` (stubs for future)

**Agent**:
- `workflow-analyzer` - Specialized agent for comprehensive session analysis

**Hooks** (Event-driven):
- `pre_compact.py` - Creates transcript backups before compaction
- `session_end.py` - Captures session completion data
- `subagent_stop.py` - Tracks subagent lifecycle events

**Commands**:
- `/analyze-workflow [date] [instructions]` - Analyze sessions from specific dates

## Installation

### Prerequisites
- Claude Code >=1.0.0
- Python 3.8+ (for hooks)
- Node.js 14+ (for JavaScript skills)

### Install from GitHub

```bash
# Install entire marketplace (includes workflow-analyzer)
claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git
```

### Install Locally (Development)

```bash
# Clone and install
git clone git@github.com:OrasesLabs/orases-claude-code-marketplace.git
cd orases-claude-code-marketplace/workflow-analyzer
claude plugin install .
```

### Verify Installation

```bash
# Check plugin is installed
claude plugin list

# Start Claude and test
# Ask: "What sessions do I have?"
```

## Quick Start

### Discover Sessions

**Using natural language:**
```
"What sessions do I have?"
"Show me my recent Claude Code sessions"
```

**Using slash command:**
```bash
# List available session dates
/analyze-workflow
```

### Analyze a Session

**Using slash command:**
```bash
# Analyze specific date (YYYYMMDD format)
/analyze-workflow 20251114

# Analyze with custom focus
/analyze-workflow 20251114 focus on error patterns
/analyze-workflow 20251114 Why did we encounter so many errors?
```

### Condense Transcripts

**Using natural language:**
```
"Condense this transcript for me"
"Summarize my workflow session"
```

## Configuration

### Optional: Custom Project Root

By default, the plugin auto-detects the project root by finding the `.claude` directory. To override:

```bash
# Add to ~/.bashrc or ~/.zshrc
export CLAUDE_PROJECT_ROOT="/path/to/your/project"
```

### Log Files

Hooks automatically create logs in `.claude/logs/`:
- `pre_compact.json` - Compaction events
- `session_end.json` - Session tracking
- `subagent_stop.json` - Subagent tracking
- `YYYYMMDD/` - Dated transcript directories

## Plugin Structure

```
workflow-analyzer/
├── .claude-plugin/
│   └── plugin.json          # Plugin manifest
├── skills/                  # Model-invoked capabilities
│   ├── session-analyzer/
│   ├── transcript-condenser/
│   └── [stubs for future skills]
├── agents/
│   └── workflow-analyzer.md # Analysis specialist
├── hooks/                   # Event-driven automation
│   ├── hooks.json
│   ├── pre_compact.py
│   ├── session_end.py
│   └── subagent_stop.py
├── commands/
│   └── analyze-workflow.md  # Slash command
├── scripts/                 # Standalone utilities (stubs)
└── docs/                    # Documentation
```

## Troubleshooting

### Plugin Not Found
- Verify installation: `claude plugin list`
- Restart Claude Code
- Try local installation method

### Skills Not Working
- Restart Claude Code to reload skills
- Run debug mode: `claude --debug`
- Check skill files: `ls ~/.claude/plugins/workflow-analyzer/skills/`

### Hooks Not Running
- Verify Python 3.8+: `python3 --version`
- Check hooks are executable: `ls -la ~/.claude/plugins/workflow-analyzer/hooks/`
- Check error log: `cat .claude/logs/hook_errors.log`

### No Sessions Found
- Verify `.claude/logs/` directory exists
- Run at least one Claude Code session first
- Check logs directory: `ls -la .claude/logs/`

### Permission Errors
```bash
# Create logs directory with proper permissions
mkdir -p .claude/logs
chmod 755 .claude/logs
```

## Usage Examples

### Example 1: Weekly Review
```bash
# List available sessions
/analyze-workflow

# Analyze specific week
/analyze-workflow 20251107
/analyze-workflow 20251114
```

### Example 2: Custom Analysis
```bash
# Focus on specific aspects
/analyze-workflow 20251114 analyze error handling patterns
/analyze-workflow 20251114 review subagent usage
/analyze-workflow 20251114 identify optimization opportunities
```

### Example 3: Natural Language
```
"Show me sessions from last week"
"Analyze my workflow from today"
"Condense the large transcript"
"What patterns do you see in my sessions?"
```

## Development

### Creating Custom Skills

1. Create directory under `skills/`
2. Write `SKILL.md` with YAML frontmatter:

```yaml
---
name: my-skill
description: What the skill does and when to use it
allowed-tools: [Bash, Read, Write]
---

# Skill instructions for Claude
```

3. Test with natural language requests

### Extending Hooks

Edit hook files to customize behavior:

```bash
# Customize session tracking
vim ~/.claude/plugins/workflow-analyzer/hooks/session_end.py
```

## Architecture

This plugin uses a **comprehensive workflow tracking strategy**:
- **Hooks** capture session events automatically
- **Skills** provide autonomous analysis capabilities
- **Agents** handle complex multi-step analysis tasks
- **Commands** enable user-initiated workflows
- **Scripts** offer standalone analysis tools (planned)

## Planned Features

- Commit pattern analysis
- Code pattern and anti-pattern detection
- Automated optimization recommendations
- Historical trend analysis
- Team-wide analytics
- Integration with issue trackers
- Export to multiple formats (HTML, PDF)

## Support

- **Issues**: https://github.com/OrasesLabs/orases-claude-code-marketplace/issues
- **Documentation**: See individual component directories
- **Resources**:
  - [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code)
  - [Claude Code Plugins Guide](https://docs.claude.com/en/docs/claude-code/plugins)
  - [Claude Code Skills Guide](https://docs.claude.com/en/docs/claude-code/skills)
  - [Claude Code Hooks Guide](https://docs.claude.com/en/docs/claude-code/hooks)

## Contributing

Contributions welcome! Please:
1. Create a feature branch
2. Follow existing structure and conventions
3. Test thoroughly
4. Update documentation and CHANGELOG.md
5. Submit pull request with clear description

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Version:** 0.1.0
**Author:** Orases
**Repository:** https://github.com/OrasesLabs/orases-claude-code-marketplace
