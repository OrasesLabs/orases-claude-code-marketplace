---
name: docs-management:help
description: Display help and usage information for the docs-management plugin. Optionally specify a command or skill name for detailed help.
argument-hint: "[command or skill]"
allowed-tools: Read
disable-model-invocation: true
---

# docs-management Plugin Help

Explain how the docs-management plugin works and provide help to the user.

## Arguments

$ARGUMENTS

## Instructions

**If arguments are provided:** The user wants help on a specific command or skill.

1. Identify the requested item from the arguments (strip `docs-management:` prefix if present)
2. Read the corresponding file from the plugin:
   - Commands: `${CLAUDE_PLUGIN_ROOT}/commands/<name>.md`
   - Skills: `${CLAUDE_PLUGIN_ROOT}/skills/<name>/SKILL.md`
3. Provide a helpful summary including:
   - What it does and when to use it
   - How to invoke it with examples
   - Key options or features
   - Answer any specific questions included in the arguments
4. If not found, suggest the closest match from available commands/skills listed below.

**If no arguments provided:** Display the general help content below.

---

## Overview

The docs-management plugin helps you create, organize, and maintain project documentation using the Diataxis framework. It provides commands for common documentation tasks and writer skills with embedded templates and quality checklists.

## How It Works

### 1. Diataxis Framework

Documentation is organized into four types based on user needs:

| Type | User Need | Directory |
|------|-----------|-----------|
| **Tutorials** | "I want to learn" | `docs/getting-started/` |
| **How-to Guides** | "I want to accomplish X" | `docs/guides/` |
| **Reference** | "I need to look up Y" | `docs/reference/`, `docs/technical/` |
| **Explanation** | "I want to understand why" | `docs/architecture/` |

### 2. Standard Directory Structure

```
/
├── README.md                 # Project overview
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # Contribution guide
└── docs/
    ├── README.md             # Documentation index
    ├── getting-started/      # Tutorials
    ├── guides/               # How-to guides
    │   ├── user/
    │   └── developer/
    ├── reference/            # Reference docs
    │   └── api/
    ├── architecture/         # Explanations
    ├── technical/            # Technical specs
    └── assets/
        ├── images/
        └── diagrams/
```

## Available Commands

| Command | Description |
|---------|-------------|
| `/docs-management:help` | Show this help (or help for a specific command/skill) |
| `/docs-management:setup-project` | Initialize standard docs directory structure |
| `/docs-management:review-coverage` | Audit docs and identify gaps |
| `/docs-management:create-tutorial` | Create learning-oriented tutorial |
| `/docs-management:create-how-to` | Create task-oriented how-to guide |
| `/docs-management:create-reference` | Create technical reference docs |
| `/docs-management:create-explanation` | Create architectural/conceptual docs |
| `/docs-management:update-from-changes` | Update docs based on recent git commits |
| `/docs-management:migrate-existing` | Reorganize existing docs to standard structure |

## Writer Skills

These skills provide templates, guidelines, and quality checklists. They are loaded automatically by commands or can be referenced directly:

| Skill | Use For |
|-------|---------|
| `docs-management:documentation-standards` | Overall standards and conventions |
| `docs-management:tutorial-writer` | Step-by-step learning tutorials |
| `docs-management:how-to-guide-writer` | Task-oriented guides |
| `docs-management:tech-specs-writer` | API specs, data models, config reference |
| `docs-management:system-overview-writer` | Architecture and system design |
| `docs-management:adr-writer` | Architecture Decision Records |
| `docs-management:research-findings-writer` | Research and investigation results |

## Example Use Cases

**Set up a new project:**
```
/docs-management:setup-project
```
Creates the standard directory structure with placeholder files.

**Check documentation health:**
```
/docs-management:review-coverage
```
Audits existing docs and identifies gaps, stale content, and missing required documents.

**Create documentation:**
```
/docs-management:create-how-to deploying to production
/docs-management:create-reference the authentication API
/docs-management:create-tutorial getting started with the SDK
```

**Keep docs in sync with code:**
```
/docs-management:update-from-changes last 5 commits
```
Reviews recent git changes and updates affected documentation.

**Reorganize existing docs:**
```
/docs-management:migrate-existing
```
Analyzes current docs and migrates them to the standard Diataxis structure.

## Customization

Create these files in your project to customize behavior:

- `.claude/docs-management.md` - Project-specific rules and templates
- `.claude/docs-management.local.md` - Personal preferences (gitignored)

Example project config:
```markdown
# Project Documentation Config

## Additional Templates
- Use `docs/templates/runbook-template.md` for operational docs

## Project-Specific Rules
- All docs must include "Last reviewed: YYYY-MM-DD" header
- API docs require OpenAPI spec link
```

## Getting Started

1. Run `/docs-management:setup-project` to create the directory structure
2. Run `/docs-management:review-coverage` to see what documentation is needed
3. Use the create commands to build out documentation
4. Run `/docs-management:update-from-changes` after implementing features

## Getting Help on Specific Items

For detailed help on any command or skill:
```
/docs-management:help setup-project
/docs-management:help tutorial-writer
/docs-management:help create-how-to
```
