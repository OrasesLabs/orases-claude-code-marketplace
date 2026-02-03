---
name: docs-management:create-explanation
description: Create understanding-oriented explanation documentation following the Diataxis framework. Explanations clarify concepts, architecture, and design decisions.
argument-hint: "[topic]"
allowed-tools: Task, Skill
---

# Create Explanation Documentation

Invoke the **documentation-engineer** subagent to create explanation documentation.

## Task

Use the Task tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the explanation skill**: /docs-management:system-overview-writer
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Create explanation documentation** for the topic specified below
4. **Place the document** in the project's `docs/architecture/` directory

## Topic

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Create explanation documentation for: $ARGUMENTS

Use the /docs-management:system-overview-writer skill for guidelines, template, and checklist.

This documentation type:
- Clarifies and illuminates understanding
- Discusses alternatives and trade-offs
- Provides context and background
- Can be opinionated
- Connects concepts to each other

Target directory: docs/architecture/

Report back with:
- File path created
- Summary of what was documented
- Checklist verification results
- Whether docs/README.md index was updated
```
