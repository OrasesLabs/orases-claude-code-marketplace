# docs-management

Documentation management plugin for Claude Code with Diátaxis framework support. Create, organize, and maintain project documentation following industry standards.

## Features

- **Diátaxis Framework** - Organize docs into Tutorials, How-to Guides, Reference, and Explanation
- **Templates** - Ready-to-use templates for each documentation type
- **Quality Checklists** - Type-specific checklists to ensure documentation quality
- **Project Customization** - Override defaults with project or user-specific settings
- **Git Integration** - Update docs based on recent code changes

## Installation

```bash
claude plugins add docs-management
```

## Commands

| Command | Description |
|---------|-------------|
| `/docs-management:create-tutorial` | Create learning-oriented tutorial documentation |
| `/docs-management:create-how-to` | Create task-oriented how-to guide |
| `/docs-management:create-reference` | Create reference/technical documentation |
| `/docs-management:create-explanation` | Create architectural/conceptual documentation |
| `/docs-management:update-from-changes` | Review git commits and update affected docs |
| `/docs-management:setup-project` | Initialize standard docs structure |
| `/docs-management:migrate-existing` | Reorganize existing docs to standard structure |
| `/docs-management:review-coverage` | Audit documentation and identify gaps |

### Usage Examples

```bash
# Create a how-to guide for deployment
/docs-management:create-how-to deploying to production

# Create reference docs for the API
/docs-management:create-reference the authentication API

# Update docs after implementing a feature
/docs-management:update-from-changes last 5 commits

# Check documentation coverage
/docs-management:review-coverage API documentation
```

## Diátaxis Framework

This plugin organizes documentation using the [Diátaxis framework](https://diataxis.fr/):

| Type | User Need | Directory |
|------|-----------|-----------|
| **Tutorials** | "I want to learn" | `docs/getting-started/` |
| **How-to Guides** | "I want to accomplish X" | `docs/guides/` |
| **Reference** | "I need to look up Y" | `docs/reference/`, `docs/technical/` |
| **Explanation** | "I want to understand why" | `docs/architecture/` |

## Directory Structure

The plugin establishes this standard structure:

```
/
├── README.md                 # Project overview
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # Contribution guide
│
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
    └── assets/               # Images, diagrams
```

## Skills

The plugin provides writer skills with embedded templates and quality checklists:

| Skill | Use For |
|-------|---------|
| `docs-management:tutorial-writer` | Tutorials, quick starts |
| `docs-management:how-to-guide-writer` | Task-oriented guides |
| `docs-management:tech-specs-writer` | API specs, data models |
| `docs-management:research-findings-writer` | Research documentation |
| `docs-management:system-overview-writer` | System architecture |
| `docs-management:adr-writer` | Architecture decisions |
| `docs-management:documentation-standards` | Overall standards |

Each skill includes:
- Writing guidelines (DO/DON'T)
- Ready-to-use templates
- Quality checklists

## Customization

### Project-Specific Settings

Create `.claude/docs-management.md` in your project root:

```markdown
# Project Documentation Config

## Additional Templates
- Use `docs/templates/runbook-template.md` for operational docs

## Project-Specific Rules
- All docs must include "Last reviewed: YYYY-MM-DD" header
- API docs require OpenAPI spec link

## Custom Checklist Items
- [ ] Reviewed by tech writer
- [ ] Added to documentation index
```

### User-Specific Settings

Create `.claude/docs-management.local.md` for personal preferences (gitignored):

```markdown
# Personal Documentation Preferences

## Style Preferences
- Use British English spelling
- Prefer bullet lists over numbered lists for non-sequential items
```

## Agent

The `docs-management:documentation-engineer` agent can be invoked for complex documentation tasks:

- Assessing documentation state
- Identifying gaps
- Coordinating multi-document updates
- Ensuring consistency across documentation

## Standards

Full documentation standards are available in the `docs-management:documentation-standards` skill, covering:

- Project file structure
- Diátaxis framework details
- Naming conventions
- Content standards
- Architecture-agnostic principles
- Quality checklists
- Maintenance practices
- Style guide

## License

MIT
