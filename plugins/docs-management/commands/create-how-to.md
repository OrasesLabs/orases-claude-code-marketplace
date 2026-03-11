---
name: docs-management:create-how-to
description: Create task-oriented how-to guide documentation following the Diataxis framework. How-to guides help users accomplish specific goals.
argument-hint: "[task]"
allowed-tools: Task, Agent, Skill
---

# Create How-to Guide Documentation

Invoke the **documentation-engineer** subagent to create how-to guide documentation.

## Task

Use the Task or Agent tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the how-to-guide skill**: /docs-management:how-to-guide-writer
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Create how-to guide documentation** for the task specified below
4. **Place the document** in the project's `docs/guides/` directory (user/ or developer/ as appropriate)

## Task to Document

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Create how-to guide documentation for: $ARGUMENTS

Use the /docs-management:how-to-guide-writer skill for guidelines, template, and checklist.

This documentation type:
- Assumes user knows what they want to do
- Focuses on practical steps to achieve a goal
- Doesn't explain underlying concepts (links to explanations)
- Is flexible, allows for variations
- Includes troubleshooting for common issues

Target directory: docs/guides/

Report back with:
- File path created
- Summary of what task the guide helps accomplish
- Checklist verification results
- Whether docs/README.md index was updated
```
