---
name: docs-management:migrate-existing
description: Analyze existing project documentation and migrate it to the standard Diataxis-based structure. Creates a migration plan before making changes.
argument-hint: "[path]"
allowed-tools: Task, Skill
---

# Migrate Existing Documentation

Invoke the **documentation-engineer** subagent to analyze existing documentation and migrate it to the standard structure.

## Task

Use the Task tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the documentation standards**: /docs-management:documentation-standards
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Inventory existing documentation**
4. **Classify each document** by Diataxis type
5. **Create migration plan** and present for approval
6. **Execute migration** after approval
7. **Update cross-references** to fix broken links

## Path/Options

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Analyze and migrate existing documentation to the standard structure.

Path/Options: $ARGUMENTS

Use the /docs-management:documentation-standards skill to understand the target structure.

Steps:
1. Find all .md files in the project
2. Classify each document:
   | Document Contains | Diataxis Type | Target Directory |
   |-------------------|---------------|------------------|
   | Step-by-step learning | Tutorial | getting-started/ |
   | Task completion steps | How-to | guides/ |
   | API specs, data models | Reference | reference/, technical/ |
   | Design decisions, architecture | Explanation | architecture/ |

3. Create migration plan:
   - Files to move (with current and new locations)
   - Files to merge (if duplicates exist)
   - Files to keep in place
   - New files to create (indexes, etc.)

4. IMPORTANT: Present the plan and ask for user approval before executing

5. After approval:
   - Execute the migration
   - Update all cross-references
   - Create/update docs/README.md index

Report back with:
- Documents analyzed (count and summary)
- Migration actions taken
- Links updated
- Any items requiring manual review
```
