---
name: docs-management:create-tutorial
description: Create learning-oriented tutorial documentation following the Diataxis framework. Tutorials help users learn by doing with step-by-step guidance.
argument-hint: "[topic]"
allowed-tools: Task, Skill
---

# Create Tutorial Documentation

Invoke the **documentation-engineer** subagent to create tutorial documentation.

## Task

Use the Task tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the tutorial skill**: /docs-management:tutorial-writer
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Create tutorial documentation** for the topic specified below
4. **Place the document** in the project's `docs/getting-started/` directory

## Topic

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Create tutorial documentation for: $ARGUMENTS

Use the /docs-management:tutorial-writer skill for guidelines, template, and checklist.

This documentation type:
- Focuses on learning, not accomplishing a task
- Must work every time the user follows it
- Shows concrete steps, not abstract concepts
- Gets user to achievement quickly
- Provides only enough explanation to proceed

Target directory: docs/getting-started/

Report back with:
- File path created
- Summary of what the tutorial teaches
- Checklist verification results
- Whether docs/README.md index was updated
```
