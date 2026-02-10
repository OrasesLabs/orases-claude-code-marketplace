---
name: tutorial-writer
description: Guidelines for creating learning-oriented tutorial documentation. Use when writing step-by-step content that helps users learn by doing.
allowed-tools: Read, Write, Edit, Glob
---

# Tutorial Documentation Skill

This skill provides guidelines for creating **tutorial** documentation - learning-oriented content in the Diataxis framework.

## Purpose

Tutorials help users **learn** by guiding them through a series of steps. The user follows along to gain knowledge and skills.

## User Need

> "I want to learn how to use this."

## Characteristics

| Attribute | Description |
|-----------|-------------|
| **Orientation** | Learning |
| **Focus** | Study, not work |
| **Goal** | Help user acquire skills |
| **Tone** | Encouraging, supportive |

## Target Directory

Place tutorials in: `docs/getting-started/`

## Writing Guidelines

### DO

- Focus on learning, not accomplishing a practical task
- Ensure the tutorial works every time the user follows it
- Show concrete steps, not abstract concepts
- Get the user to a meaningful achievement quickly
- Provide only enough explanation to proceed
- Use consistent formatting and structure
- Test the tutorial yourself before publishing

### DON'T

- Assume prior knowledge (explain everything needed)
- Offer choices or alternatives (provide one clear path)
- Explain concepts in depth (link to explanations instead)
- Include troubleshooting (the tutorial should just work)
- Cover edge cases (keep the happy path)

## Examples of Good Tutorials

- "Getting started with [Project]"
- "Your first [Feature]"
- "Building a [Simple Thing] in 10 minutes"
- "Introduction to [Concept] with hands-on exercises"

---

## Template

Use this template when creating tutorial documentation:

```markdown
# [Tutorial Title]

*Estimated time: [X minutes]*

## What you'll learn

By the end of this tutorial, you will:

- [Learning outcome 1]
- [Learning outcome 2]
- [Learning outcome 3]

## Prerequisites

Before starting, ensure you have:

- [Requirement 1 - e.g., Node.js 18+ installed]
- [Requirement 2 - e.g., Basic familiarity with JavaScript]
- [Requirement 3 - e.g., A code editor]

## Step 1: [Set up your environment]

[Clear instruction for what to do first]

[Command or code example]

You should see:

[Expected output]

## Step 2: [Create your first [thing]]

[Clear instruction]

[Code example]

[Brief explanation of what this does - just enough to proceed]

## Step 3: [Add [feature]]

[Clear instruction]

[Code example]

## Step 4: [Run and verify]

[Instruction to run/test what was built]

[Command]

You should see:

[Expected output showing success]

## What you've accomplished

Congratulations! You've successfully:

- [Achievement 1]
- [Achievement 2]
- [Achievement 3]

## Next steps

Now that you've completed this tutorial, you can:

- [Link to next tutorial in series]
- [Link to how-to guide for practical application]
- [Link to reference docs for deeper understanding]

---

*Having trouble? Check the [troubleshooting guide](../guides/TROUBLESHOOTING.md) or [open an issue](link-to-issues).*
```

---

## Quality Checklist

Apply this checklist before finalizing any tutorial documentation.

### Learning Focus

- [ ] Focuses on learning, not accomplishing a practical task
- [ ] Gets the user to a meaningful achievement
- [ ] Provides only enough explanation to proceed
- [ ] Does not overwhelm with information

### Reliability

- [ ] Tutorial has been tested end-to-end
- [ ] All commands and code examples work
- [ ] Expected outputs match actual outputs
- [ ] Prerequisites are accurate and complete

### Structure

- [ ] Clear, numbered steps
- [ ] Each step has one clear action
- [ ] Steps build on each other logically
- [ ] Estimated time is realistic

### Clarity

- [ ] No unexplained jargon
- [ ] Instructions are unambiguous
- [ ] One clear path (no choices or alternatives)
- [ ] Code examples can be copy-pasted

### Beginner-Friendly

- [ ] Assumes no prior knowledge of this specific topic
- [ ] Explains any necessary context
- [ ] Does not skip "obvious" steps
- [ ] Encouraging tone

### Completeness

- [ ] "What you'll learn" section is accurate
- [ ] Prerequisites are listed
- [ ] "What you've accomplished" summarizes outcomes
- [ ] Next steps point to relevant resources

### Formatting

- [ ] Consistent heading structure
- [ ] Code blocks have language specified
- [ ] Expected output is shown after commands
- [ ] No broken links

### Documentation Index

- [ ] If a new file was created, moved, or removed: regenerate the CLAUDE.md documentation index via `/docs-management:generate-index`
