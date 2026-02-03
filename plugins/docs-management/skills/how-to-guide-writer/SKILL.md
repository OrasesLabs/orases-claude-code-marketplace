---
name: how-to-guide-writer
description: Guidelines for creating task-oriented how-to guide documentation. Use when writing content that helps users accomplish specific goals.
allowed-tools: Read, Write, Edit, Glob
---

# How-to Guide Documentation Skill

This skill provides guidelines for creating **how-to guide** documentation - task-oriented content in the Diataxis framework.

## Purpose

How-to guides help users **accomplish a specific task**. The user knows what they want to do and needs practical steps to do it.

## User Need

> "I want to accomplish X."

## Characteristics

| Attribute | Description |
|-----------|-------------|
| **Orientation** | Task completion |
| **Focus** | Practical work |
| **Goal** | Help user achieve a goal |
| **Tone** | Direct, practical |

## Target Directory

Place how-to guides in: `docs/guides/`
- `docs/guides/user/` for end-user guides
- `docs/guides/developer/` for developer guides

## Writing Guidelines

### DO

- Assume the user knows what they want to do
- Focus on practical steps to achieve the goal
- Be flexible and allow for variations
- Include troubleshooting for common issues
- Provide working code examples
- Link to reference docs for details
- Link to explanations for "why" questions

### DON'T

- Explain underlying concepts in depth
- Teach or provide learning experiences
- Assume the reader is a beginner
- Include unnecessary background
- Cover every possible variation

## Examples of Good How-to Guides

- "How to deploy to production"
- "How to configure authentication"
- "How to migrate from v1 to v2"
- "How to set up local development"
- "How to add a new API endpoint"

---

## Template

Use this template when creating how-to guide documentation:

```markdown
# How to [accomplish specific task]

*Last updated: [YYYY-MM-DD]*

## Overview

This guide explains how to [brief description of what this helps you accomplish].

## Prerequisites

Before you begin, ensure you have:

- [Prerequisite 1]
- [Prerequisite 2]

## Steps

### 1. [First action verb phrase]

[Clear, concise instruction]

[Code or command example]

### 2. [Second action verb phrase]

[Clear, concise instruction]

[Code or command example]

### 3. [Third action verb phrase]

[Clear, concise instruction]

> **Note:** [Optional helpful tip or important consideration]

## Verification

To confirm the task completed successfully:

1. [Verification step 1]
2. [Verification step 2]

Expected result:

[What success looks like]

## Troubleshooting

### [Common issue 1]

**Symptom:** [What the user sees or experiences]

**Cause:** [Why this happens]

**Solution:**

[Fix or workaround]

### [Common issue 2]

**Symptom:** [What the user sees]

**Solution:** [How to fix it]

## Related guides

- [Related how-to guide](relative/path.md)
- [Reference documentation](../reference/RELEVANT-REFERENCE.md)
- [Explanation of underlying concept](../architecture/RELEVANT-CONCEPT.md)
```

---

## Quality Checklist

Apply this checklist before finalizing any how-to guide documentation.

### Task Focus

- [ ] Title clearly states what task is accomplished
- [ ] Focuses on practical steps, not learning
- [ ] Assumes user knows what they want to do
- [ ] Does not explain underlying concepts in depth

### Completeness

- [ ] All necessary steps are included
- [ ] Prerequisites are listed
- [ ] Verification steps confirm success
- [ ] Common issues have troubleshooting entries

### Practicality

- [ ] Steps are actionable
- [ ] Code examples work and can be adapted
- [ ] Allows for reasonable variations
- [ ] Links to reference docs for details

### Structure

- [ ] Clear, numbered steps
- [ ] Each step has a verb-phrase heading
- [ ] Logical order of operations
- [ ] Troubleshooting section is organized

### Clarity

- [ ] Instructions are direct and concise
- [ ] No unnecessary background information
- [ ] Technical terms link to definitions
- [ ] Expected results are shown

### Maintainability

- [ ] No hardcoded values that will change
- [ ] Version-specific info is date-stamped
- [ ] Related guides are cross-referenced
- [ ] Easy to update when things change

### Formatting

- [ ] Consistent heading structure
- [ ] Code blocks have language specified
- [ ] Notes/warnings use consistent format
- [ ] No broken links
