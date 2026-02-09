# docs-management

Documentation management plugin for Claude Code with Diátaxis framework support. Create, organize, and maintain project documentation following industry standards.

## Features

- **Diátaxis Framework** - Organize docs into Tutorials, How-to Guides, Reference, and Explanation
- **Compressed Documentation Index** - Generate token-efficient indexes in CLAUDE.md for fast doc discovery
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
| `/docs-management:generate-index` | Generate compressed documentation index in CLAUDE.md |

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

# Generate documentation index (updates CLAUDE.md)
/docs-management:generate-index ./docs

# Preview index without writing
/docs-management:generate-index ./docs --dry-run

# Generate index for a specific section only
/docs-management:generate-index ./docs --quadrant reference
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

## Documentation Index

The plugin can generate a compressed, token-efficient documentation index and embed it in your project's CLAUDE.md. This gives Claude instant context about what documentation exists and where to find it.

### How It Works

1. Scans a `docs/` directory for all `.md` files
2. Extracts description hints from YAML frontmatter or H1 headings
3. Writes a compressed index between `<!-- DOCS-INDEX:START -->` and `<!-- DOCS-INDEX:END -->` markers in CLAUDE.md
4. Auto-detects the project's CLAUDE.md by searching for project root indicators (`.git`, `package.json`, `composer.json`, etc.)

### When to Regenerate

Regenerate the index whenever documentation files or directories are added, moved, or removed. Content-only edits (no path changes) do not require regeneration.

### Compressed Format

The index uses a compact notation to minimize token usage. See [INDEX-FORMAT.md](docs/INDEX-FORMAT.md) for the full format reference.

Example output:

```
root:./docs/|IMPORTANT: Read relevant docs before implementing.

|getting-started/README.md    -> Learning-oriented guides
|reference/api:{AUTH.md,ENDPOINTS.md}
|architecture:OVERVIEW.md     -> System architecture
```

### Scripts

| Script | Description |
|--------|-------------|
| `scripts/generate-docs-index.py` | Scans docs and writes compressed index to CLAUDE.md |
| `scripts/update-docs-index.sh` | Thin bash wrapper for quick regeneration |

```bash
# Generate index (updates CLAUDE.md automatically)
python3 scripts/generate-docs-index.py ./docs

# Preview without writing
python3 scripts/generate-docs-index.py ./docs --dry-run

# Filter to a specific Diataxis section
python3 scripts/generate-docs-index.py ./docs --quadrant reference

# Target a specific CLAUDE.md
python3 scripts/generate-docs-index.py ./docs --output ./CLAUDE.md
```

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
