---
name: docs-management:create-reference
description: Create information-oriented reference documentation following the Diataxis framework. Reference docs provide factual, complete information for lookup.
argument-hint: "[subject]"
allowed-tools: Task, Agent, Skill
---

# Create Reference Documentation

Invoke the **documentation-engineer** subagent to create reference documentation.

## Task

Use the Task or Agent tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the reference skill**: /docs-management:tech-specs-writer
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Create reference documentation** for the subject specified below
4. **Place the document** in the project's `docs/reference/` or `docs/technical/` directory as appropriate

## Subject to Document

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Create reference documentation for: $ARGUMENTS

Use the /docs-management:tech-specs-writer skill for guidelines, template, and checklist.

This documentation type:
- Is austere, factual, descriptive
- Structures consistently (uses tables, lists)
- Prioritizes completeness and accuracy
- Doesn't mix in tutorials or how-tos
- Matches the structure of the thing being documented

Target directory: docs/reference/ or docs/technical/

Report back with:
- File path created
- Summary of what the reference documents
- Checklist verification results
- Whether docs/README.md index was updated
```
