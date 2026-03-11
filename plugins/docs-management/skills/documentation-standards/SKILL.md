---
name: docs-management:documentation-standards
description: Documentation standards and conventions based on Diataxis framework. Use this skill to learn project documentation conventions before creating, reviewing, or updating docs.
allowed-tools: Read, Glob
---

# Documentation Standards

This skill provides the structure, policies, and quality standards for all project documentation. **Any human or agent creating documentation must follow these standards.**

*Based on [ISO/IEC/IEEE 26514:2022](https://www.iso.org/standard/77451.html) and the [Diataxis Framework](https://diataxis.fr/).*

## Customization Check

Before applying these standards, check for project-specific customizations:

1. `.claude/docs-management.md` (project-specific, shared with team) - if it exists
2. `.claude/docs-management.local.md` (user-specific, personal preferences) - if it exists

Apply standards in order: **local overrides > project overrides > plugin defaults**

---

## Project File Structure

### Root-Level Files

Certain files belong in the **project root** for maximum visibility and tooling support:

| File | Location | Purpose |
|------|----------|---------|
| `README.md` | `/` (root) | Project overview - GitHub/GitLab displays on homepage |
| `CHANGELOG.md` | `/` (root) | Version history - tools like `semantic-release` expect this |
| `CONTRIBUTING.md` | `/` (root) | Contribution guide - GitHub links in Community tab |
| `LICENSE` | `/` (root) | License file - package managers detect automatically |
| `CODE_OF_CONDUCT.md` | `/` (root) | Community standards - GitHub surfaces in health score |
| `SECURITY.md` | `/` (root) | Security policy - GitHub displays security information |

### Why Root Level?

- GitHub, GitLab, and npm automatically detect and surface these files
- Tools like `standard-version` and `semantic-release` expect `CHANGELOG.md` at root
- Package managers validate `LICENSE` location
- Improves discoverability for new contributors

---

## Directory Structure

All other documentation lives in `/docs/`:

```
/                                  # Project root
├── README.md                      # Project overview (GitHub displays)
├── CHANGELOG.md                   # Version history (single source of truth)
├── CONTRIBUTING.md                # How to contribute
├── LICENSE                        # License file
│
└── docs/                          # All documentation
    ├── README.md                  # Documentation index & navigation
    │
    ├── getting-started/           # TUTORIALS (Learning-oriented)
    │   ├── QUICK-START.md         # First steps walkthrough
    │   ├── SETUP-GUIDE.md         # Environment setup
    │   └── PREREQUISITES.md       # Required knowledge/tools
    │
    ├── guides/                    # HOW-TO GUIDES (Task-oriented)
    │   ├── user/                  # End-user guides
    │   └── developer/             # Developer guides
    │       ├── CONTRIBUTING.md    # Code contribution guide
    │       ├── TESTING.md         # How to run tests
    │       └── DEPLOYMENT.md      # Deployment procedures
    │
    ├── reference/                 # REFERENCE (Information-oriented)
    │   ├── api/                   # API documentation
    │   │   ├── ENDPOINTS.md       # Endpoint reference
    │   │   ├── AUTHENTICATION.md  # Auth methods
    │   │   └── ERROR-CODES.md     # Error reference
    │   ├── CONFIGURATION.md       # Config options reference
    │   └── CLI-COMMANDS.md        # Command line reference
    │
    ├── architecture/              # EXPLANATION (Understanding-oriented)
    │   ├── OVERVIEW.md            # System architecture
    │   ├── DESIGN-DECISIONS.md    # ADRs (Architecture Decision Records)
    │   ├── DATA-FLOW.md           # How data moves through system
    │   └── SECURITY.md            # Security model explanation
    │
    ├── technical/                 # Technical specifications
    │   ├── API-SPECIFICATION.md   # Complete API spec with schemas
    │   ├── DATA-MODELS.md         # Data structures and relationships
    │   └── DATABASE-SCHEMA.md     # Database design
    │
    ├── research/                  # Discovery & research findings
    │   ├── README.md              # Research index
    │   └── findings/              # Investigation results
    │
    └── assets/                    # Supporting media
        ├── images/                # Screenshots, photos
        └── diagrams/              # Architecture diagrams
```

---

## Diataxis Framework

Documentation is organized into four types based on user needs:

### The Four Documentation Types

| Type | Purpose | User Need | Characteristics |
|------|---------|-----------|-----------------|
| **Tutorials** | Learning | "I want to learn" | Step-by-step, beginner-focused, works every time |
| **How-to Guides** | Goals | "I want to accomplish X" | Task-focused, assumes knowledge, practical |
| **Reference** | Information | "I need to look up Y" | Factual, complete, consistent structure |
| **Explanation** | Understanding | "I want to understand why" | Conceptual, discusses trade-offs, opinionated |

### Where Each Type Lives

| Diataxis Type | Directory | Examples |
|---------------|-----------|----------|
| Tutorials | `getting-started/` | Quick-start, setup guides |
| How-to Guides | `guides/` | Contributing, testing, deployment |
| Reference | `reference/`, `technical/` | API docs, config options, data models |
| Explanation | `architecture/` | Design decisions, data flow, security model |

---

## Documentation Policy

### Where to Create Documentation

| Document Type | Location | Example |
|--------------|----------|---------|
| Project overview | `/README.md` (root) | Main project description |
| Version history | `/CHANGELOG.md` (root) | Release notes |
| API specifications | `docs/technical/` | API-SPECIFICATION.md |
| Data models | `docs/technical/` | DATA-MODELS.md |
| Architecture explanations | `docs/architecture/` | DESIGN-DECISIONS.md |
| Research findings | `docs/research/` | Investigation results |
| Setup/getting started | `docs/getting-started/` | QUICK-START.md |
| User guides | `docs/guides/user/` | Feature guides |
| Developer guides | `docs/guides/developer/` | Contributing, testing |

### Critical Rules

1. **NEVER** create documentation in `.claude/` directory
2. **ALL** new documentation goes in `/docs/` structure (except root-level files)
3. **ALWAYS** prefer editing existing files over creating new ones
4. **NEVER** create README.md files unless explicitly requested
5. **UPDATE** `docs/README.md` index when adding new documents
6. **KEEP** CHANGELOG.md in project root, not in docs/
7. **USE** relative links for cross-references within docs/
8. **REGENERATE** the `docs/INDEX.md` documentation index whenever docs files or directories are added, moved, or removed (see below)

### Documentation Index Maintenance

The project's `docs/` directory may contain an `INDEX.md` file with a compressed documentation index. This file is referenced from CLAUDE.md via `@docs/INDEX.md` so that Claude has fast context about what documentation exists and where.

**When to regenerate the index:**

| Event | Action Required |
|-------|----------------|
| New doc file created | Regenerate index |
| Doc file deleted or removed | Regenerate index |
| Doc file moved or renamed | Regenerate index |
| Doc directory added or removed | Regenerate index |
| Doc file content edited (no path change) | No regeneration needed |

**How to regenerate:**

Run the index generator against the project's docs directory:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py <docs-path>
```

Or use the slash command:

```
/docs-management:generate-index <docs-path>
```

The script writes `INDEX.md` inside the docs directory. Use `--dry-run` to preview changes first.

> **Note:** The docs directory path varies by project. Do not assume `./docs/` -- check the actual project structure or ask the user if unclear.

### Required Documents (Minimum Viable Documentation)

| Document | Priority | Location |
|----------|----------|----------|
| Project README | **Critical** | `/README.md` |
| Quick start guide | **Critical** | `docs/getting-started/QUICK-START.md` |
| API reference (if applicable) | **Critical** | `docs/reference/api/` |
| Architecture overview | **High** | `docs/architecture/OVERVIEW.md` |
| Contributing guide | **High** | `/CONTRIBUTING.md` or `docs/guides/developer/` |
| CHANGELOG | **High** | `/CHANGELOG.md` |

---

## Naming Conventions

### Files

| Convention | Example | Notes |
|------------|---------|-------|
| UPPERCASE with hyphens | `API-REFERENCE.md` | Standard for docs/ |
| Descriptive names | `AUTHENTICATION-FLOW.md` | Not `AUTH.md` |
| Include version where relevant | `MIGRATION-V2-TO-V3.md` | For upgrade guides |
| Match directory patterns | See existing files | Consistency over preference |

### Folders

| Convention | Example | Notes |
|------------|---------|-------|
| lowercase with hyphens | `getting-started/` | Never camelCase or PascalCase |
| Descriptive purpose | `architecture/` | Not `arch/` |
| Group by purpose | `reference/api/` | Not by file format |

### Section Headers

| Convention | Example | Notes |
|------------|---------|-------|
| Sentence case | "Getting started" | Not "Getting Started" |
| Be specific | "Configure authentication" | Not "Configuration" |
| Action-oriented for guides | "Install dependencies" | Imperative mood |

---

## Content Standards

### Writing Principles

1. **Know Your Audience** - Adjust technical depth appropriately
2. **Be Concise** - Respect reader's time
3. **Be Specific** - Avoid vague statements
4. **Be Consistent** - Same terms, same format throughout
5. **Be Current** - Update when things change

### Formatting Standards

| Element | Format | Example |
|---------|--------|---------|
| Code inline | Backticks | `npm install` |
| Code blocks | Triple backticks + language | ```bash |
| File paths | Backticks | `docs/README.md` |
| Commands | Code blocks | `$ npm run build` |
| Key terms | **Bold** first use | **Diataxis** framework |
| Emphasis | *Italics* | *not* recommended |
| Warnings | > **Warning:** | Blockquote with bold prefix |

---

## Architecture-Agnostic Principles

All technical documentation must be architecture-agnostic - it should work regardless of whether the implementation is a PWA, mobile app, desktop application, CLI, or any other platform.

### DO Document

| Topic | Example |
|-------|---------|
| What data is needed | "Player stats require: batting_average, on_base_percentage" |
| API mechanics | "Endpoint returns paginated results with has_next boolean" |
| Data dependencies | "Must fetch team_id before requesting roster" |
| Authentication requirements | "Requires API key in Authorization header" |
| Caching requirements | "Team data should be cached for 5 minutes" |
| Error handling requirements | "401 errors require re-authentication" |
| Business logic | "Season stats aggregate all games for selected year" |

### DON'T Document

| Topic | Why Not |
|-------|---------|
| UI component structure | Architecture-specific |
| Framework-specific code | Changes between implementations |
| Store/state implementation | Varies by framework |
| Component data binding | UI-specific |
| CSS/styling | Presentation layer |
| Route configuration | Framework-specific |

### Test Your Documentation

Ask: **"Could a developer use this to build a CLI tool that does the same thing?"**

- If **yes** → Good, architecture-agnostic
- If **no** → Too implementation-specific

---

## Maintenance Practices

### Review Cycle

| Frequency | Activity |
|-----------|----------|
| **Per-release** | Update affected docs before deployment |
| **Quarterly** | Full documentation accuracy audit |
| **Continuous** | Accept doc updates with code changes |

### When to Update Documentation

| Event | Required Updates |
|-------|-----------------|
| New feature | Add to relevant guides, update reference |
| Bug fix | Update troubleshooting if user-facing |
| API change | Update all API references |
| Breaking change | Add migration guide, update CHANGELOG |
| Deprecation | Add deprecation notices with timeline |

---

## Style Guide

### Key Principles

1. **Active voice** - "The system processes requests" not "Requests are processed"
2. **Present tense** - "The function returns" not "The function will return"
3. **Second person** - "You can configure" not "Users can configure"
4. **Contractions OK** - "Don't use" is friendlier than "Do not use"
5. **Oxford comma** - "A, B, and C" not "A, B and C"

### Cross-Referencing

```markdown
# Good - relative links within docs/
See [API Specification](technical/API-SPECIFICATION.md) for details.

# Good - root-level files
See [CHANGELOG](/CHANGELOG.md) for version history.

# Bad - absolute filesystem paths
See /home/user/project/docs/technical/API-SPECIFICATION.md
```

### Version Information

When documenting versioned or time-sensitive information:

```markdown
## Authentication Flow
*Last verified: 2025-01-15 against v2 API*

[Documentation content...]
```

---

## Customization

Projects can customize these standards by creating configuration files:

### Project-Specific Configuration

Create `.claude/docs-management.md` for project-wide customizations that are shared with the team (committed to version control).

### User-Specific Configuration

Create `.claude/docs-management.local.md` for personal preferences (should be gitignored).

### Configuration File Contents

These files can include:

- Additional templates or template locations
- Custom checklist items
- Project-specific naming conventions
- Additional documentation requirements
- Links to company style guides
- Override instructions for specific situations

**Example:**

```markdown
# Project Documentation Config

## Additional Templates
- Use `docs/templates/runbook-template.md` for operational docs

## Project-Specific Rules
- All docs must include "Last reviewed: YYYY-MM-DD" header
- API docs require OpenAPI spec link

## Custom Checklist Items
- [ ] Checked by tech writer
- [ ] Added to docs index
```

---

## Sources and References

- [ISO/IEC/IEEE 26514:2022](https://www.iso.org/standard/77451.html) - International standard for software user documentation
- [Diataxis Framework](https://diataxis.fr/) - Documentation architecture framework
- [Google Developer Documentation Style Guide](https://developers.google.com/style)

---

*This document is the single source of truth for documentation standards. When in doubt, follow these guidelines.*
