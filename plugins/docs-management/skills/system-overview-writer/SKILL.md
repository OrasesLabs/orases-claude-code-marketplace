---
name: system-overview-writer
description: Guidelines for creating architecture overview and system explanation documentation. Use when writing content that clarifies system design, data flow, and architectural concepts.
allowed-tools: Read, Write, Edit, Glob
---

# Explanation Documentation Skill

This skill provides guidelines for creating **explanation** documentation - understanding-oriented content about system architecture in the Diataxis framework.

## Purpose

Explanations help users **understand** concepts, architecture, and system design. They provide context and illuminate the "why" behind how things work.

## User Need

> "I want to understand how this system works."

## Characteristics

| Attribute | Description |
|-----------|-------------|
| **Orientation** | Understanding |
| **Focus** | Concepts and context |
| **Goal** | Illuminate and clarify |
| **Tone** | Thoughtful, discursive |

## Target Directory

Place explanations in: `docs/architecture/`

## Writing Guidelines

### DO

- Clarify and illuminate understanding
- Discuss alternatives and trade-offs
- Provide context and background
- Connect concepts to each other
- Explain the reasoning behind designs
- Be opinionated when appropriate
- Use diagrams to illustrate concepts

### DON'T

- Provide step-by-step instructions
- Focus on specific tasks
- Include code that needs to be copied
- Skip the "why" in favor of "what"
- Avoid taking positions

## Examples of Good Explanations

- "System Architecture Overview"
- "Authentication Architecture"
- "Data Flow in the Application"
- "Security Model"
- "Why We Chose PostgreSQL"

---

## Template

Use this template when creating architecture overview documentation:

```markdown
# [System/Component] Architecture

*Last updated: [YYYY-MM-DD]*

## Overview

[2-3 paragraphs providing a high-level description of the system, its purpose, and its place in the broader context]

## Key Concepts

### [Concept 1]

[Explanation of the concept, why it exists, and how it relates to the system]

### [Concept 2]

[Explanation]

### [Concept 3]

[Explanation]

## System Components

┌─────────────────────────────────────────────────────────┐
│                    [System Name]                         │
├─────────────┬─────────────────────┬─────────────────────┤
│ [Component] │    [Component]      │    [Component]      │
│             │                     │                     │
└─────────────┴─────────────────────┴─────────────────────┘
        │                 │                    │
        ▼                 ▼                    ▼
   [External]        [External]          [External]

### [Component 1]

**Purpose:** [What this component does]

**Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]

### [Component 2]

**Purpose:** [What this component does]

**Responsibilities:**
- [Responsibility 1]
- [Responsibility 2]

## Data Flow

[Description of how data moves through the system]

[User] → [Component A] → [Component B] → [Storage]
              ↓
         [Component C]

1. [Step 1 in the data flow]
2. [Step 2]
3. [Step 3]

## Design Principles

The architecture follows these guiding principles:

1. **[Principle 1]**: [Explanation of how this principle is applied]
2. **[Principle 2]**: [Explanation]
3. **[Principle 3]**: [Explanation]

## Trade-offs

| Decision | Benefit | Cost |
|----------|---------|------|
| [Decision made] | [What we gained] | [What we sacrificed] |
| [Decision made] | [What we gained] | [What we sacrificed] |

## Boundaries and Interfaces

### External Interfaces

| Interface | Protocol | Purpose |
|-----------|----------|---------|
| [Interface] | [HTTP/gRPC/etc.] | [What it's used for] |

### Internal Boundaries

[Description of how components are separated and communicate]

## Evolution

[How the architecture has evolved or is expected to evolve]

## Related Documents

- [ADR for key decisions](ADR-XXX.md)
- [Technical specification](../technical/SPEC.md)
- [API reference](../reference/api/API.md)
```

---

## Quality Checklist

Apply this checklist before finalizing any explanation documentation.

### Understanding Focus

- [ ] Clarifies concepts and provides context
- [ ] Explains "why," not just "what"
- [ ] Discusses alternatives and trade-offs
- [ ] Connects concepts to each other

### Depth

- [ ] Provides sufficient background
- [ ] Addresses the reasoning behind decisions
- [ ] Acknowledges complexity where it exists
- [ ] Does not oversimplify important nuances

### Structure

- [ ] Logical flow of ideas
- [ ] Clear section organization
- [ ] Diagrams where they aid understanding
- [ ] Appropriate level of detail

### Architecture-Specific

- [ ] Key concepts are defined
- [ ] System components are explained
- [ ] Data flow is described
- [ ] Design principles are articulated
- [ ] Trade-offs are acknowledged

### Clarity

- [ ] Concepts build on each other
- [ ] Jargon is explained or linked
- [ ] Assumptions are stated
- [ ] Examples illuminate abstract concepts

### Objectivity

- [ ] Opinions are clearly marked as such
- [ ] Multiple perspectives are considered
- [ ] Limitations are acknowledged
- [ ] Sources are referenced where appropriate

### Maintainability

- [ ] Date-stamped for time-sensitive content
- [ ] Related documents are cross-referenced
- [ ] Easy to update when understanding evolves
- [ ] No broken links

### Formatting

- [ ] Consistent heading structure
- [ ] Diagrams have alt text/descriptions
- [ ] Code examples support understanding
- [ ] Readable paragraph length

### Documentation Index

- [ ] If a new file was created, moved, or removed: regenerate the CLAUDE.md documentation index via `/docs-management:generate-index`
