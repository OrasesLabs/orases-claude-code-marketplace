---
name: docs-management:setup-project
description: Initialize the standard documentation directory structure in a new project following the Diataxis framework and documentation standards.
allowed-tools: Task, Agent, Skill
disable-model-invocation: true
---

# Setup Project Documentation Structure

Invoke the **documentation-engineer** subagent to initialize the standard documentation structure for a new project.

## Task

Use the Task or Agent tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the documentation standards**: /docs-management:documentation-standards
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Check existing structure** to see what documentation already exists
4. **Create the standard directory structure**
5. **Create index files** and root-level files as needed

## Options

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Initialize the standard documentation structure for this project.

Options: $ARGUMENTS

Use the /docs-management:documentation-standards skill to understand the required structure.

Create this directory structure:

/
├── README.md                 # Project overview (if missing)
├── CHANGELOG.md              # Version history (if missing)
├── CONTRIBUTING.md           # Contribution guide (if missing)
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
    └── assets/
        ├── images/
        └── diagrams/

Rules:
- Preserve any existing documentation
- Create .gitkeep files in empty directories
- Create docs/README.md as a navigation index

Report back with:
- Directories created
- Files created with their purposes
- What was preserved unchanged
- Recommendations for initial documentation
```
