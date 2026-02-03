---
name: docs-management:review-coverage
description: Audit current project documentation to identify gaps, outdated content, and areas needing improvement. Provides a coverage report with recommendations.
argument-hint: "[focus area]"
allowed-tools: Task, Skill
---

# Review Documentation Coverage

Invoke the **documentation-engineer** subagent to audit documentation and identify gaps.

## Task

Use the Task tool to spawn the `docs-management:documentation-engineer` agent with the following instructions:

1. **Load the documentation standards**: /docs-management:documentation-standards
2. **Check for project customizations**:
   - `.claude/docs-management.md` (project-specific)
   - `.claude/docs-management.local.md` (user-specific)
3. **Inventory all documentation** in the project
4. **Check for required documents**
5. **Analyze coverage** by Diataxis type
6. **Check for quality issues** (staleness, TODOs, broken links)
7. **Generate coverage report**

## Focus Area

$ARGUMENTS

## Agent Instructions

Pass these instructions to the documentation-engineer agent:

```
Audit project documentation and identify gaps.

Focus area: $ARGUMENTS

Use the /docs-management:documentation-standards skill to understand requirements.

Check for required documents:
| Document | Priority | Location |
|----------|----------|----------|
| Project README | Critical | /README.md |
| Quick start guide | Critical | docs/getting-started/QUICK-START.md |
| API reference (if applicable) | Critical | docs/reference/api/ |
| Architecture overview | High | docs/architecture/OVERVIEW.md |
| Contributing guide | High | /CONTRIBUTING.md |
| CHANGELOG | High | /CHANGELOG.md |

Analyze:
- Missing required documents
- Diataxis categories with no content
- Documents with TODO/TBD markers
- Documents not updated in >6 months
- Broken internal links
- Missing code examples in technical docs

Generate this report format:

## Documentation Coverage Report

### Summary
| Metric | Value |
|--------|-------|
| Total Documents | [count] |
| Required Present | [x/y] |
| With TODOs | [count] |
| Potentially Stale | [count] |

### Coverage by Type
| Type | Documents | Status |
|------|-----------|--------|
| Tutorials | [count] | [assessment] |
| How-to Guides | [count] | [assessment] |
| Reference | [count] | [assessment] |
| Explanation | [count] | [assessment] |

### Critical Gaps
[List with priorities]

### Recommendations
[Actionable items]

### Quality Issues
[Table of documents with problems]
```
