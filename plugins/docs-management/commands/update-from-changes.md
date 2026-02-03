---
name: docs-management:update-from-changes
description: Review recent git commits and update project documentation based on new features, bug fixes, or changes. Automatically determines which doc types need updating.
argument-hint: "[scope]"
allowed-tools: Task, Skill
---

# Update Documentation from Recent Changes

Invoke the **documentation-engineer** subagent to review recent code changes and update documentation accordingly.

## Task

Use the Task tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the documentation standards**: /docs-management:documentation-standards
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Review recent git changes** using git log and git diff
4. **Determine which documentation needs updating** based on the changes
5. **Load relevant skills** for each doc type that needs updating
6. **Update affected documentation**

## Scope

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Update documentation based on recent code changes.

Scope: $ARGUMENTS

Steps:
1. Review recent changes:
   - Run: git log --oneline -10
   - Run: git diff HEAD~5..HEAD --stat

2. Analyze impact - for each change consider:
   | Change Type | Documentation Impact |
   |-------------|---------------------|
   | New feature | How-to guide, Reference, possibly Tutorial |
   | API change | Reference (API docs), possibly How-to |
   | Bug fix | Troubleshooting sections, CHANGELOG |
   | Config change | Reference (configuration docs) |
   | Architecture change | Explanation (ADR), Overview |
   | Breaking change | Migration guide, CHANGELOG (highlighted) |

3. Load relevant skills for each doc type needing updates:
   - /docs-management:tutorial-writer
   - /docs-management:how-to-guide-writer
   - /docs-management:tech-specs-writer
   - /docs-management:system-overview-writer
   - /docs-management:adr-writer

4. Update CHANGELOG.md (in project root) if significant changes

Report back with:
- Summary of git changes analyzed
- List of documents updated with explanations
- Whether CHANGELOG was updated and what was added
- Any documentation still needing attention
```
