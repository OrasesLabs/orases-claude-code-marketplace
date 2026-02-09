---
name: tech-specs-writer
description: Guidelines for creating technical specification and API reference documentation. Use when writing factual, complete content about data models, API contracts, and configuration options.
allowed-tools: Read, Write, Edit, Glob
---

# Reference Documentation Skill

This skill provides guidelines for creating **reference** documentation - information-oriented technical specifications in the Diataxis framework.

## Purpose

Reference documentation provides **factual information** for lookup. Users consult it when they need specific details about APIs, configuration, data models, etc.

## User Need

> "I need to look up Y."

## Characteristics

| Attribute | Description |
|-----------|-------------|
| **Orientation** | Information |
| **Focus** | Accuracy and completeness |
| **Goal** | Provide facts for lookup |
| **Tone** | Austere, precise, neutral |

## Target Directories

- `docs/reference/` - General reference (API, CLI, config)
- `docs/reference/api/` - API documentation
- `docs/technical/` - Technical specifications, data models

## Writing Guidelines

### DO

- Be factual and descriptive
- Structure consistently (tables, lists)
- Prioritize completeness and accuracy
- Match the structure of what you're documenting
- Use consistent formatting throughout
- Include all parameters, options, return values
- Provide type information

### DON'T

- Mix in tutorials or how-tos
- Explain concepts (link to explanations)
- Include opinions or recommendations
- Skip edge cases or error states
- Assume context (be explicit)

## Architecture-Agnostic Principles

Reference docs should work regardless of implementation. Focus on:

| DO Document | DON'T Document |
|-------------|----------------|
| Data requirements | UI components |
| API contracts | Framework-specific code |
| Validation rules | State management |
| Error codes | CSS/styling |
| Business logic | Route configuration |

**Test:** "Could a developer use this to build a CLI that does the same thing?"

## Examples of Good Reference Docs

- "API Endpoints Reference"
- "Configuration Options"
- "CLI Commands"
- "Data Models"
- "Error Codes"

---

## Template

Use this template when creating technical specification documentation:

```markdown
# [Feature/Component] Specification

*Last updated: [YYYY-MM-DD]*
*Version: [X.Y.Z]*

## Overview

[1-2 sentences describing what this document specifies]

## Requirements

### Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| FR-1 | [Requirement description] | [Must/Should/Could] |
| FR-2 | [Requirement description] | [Must/Should/Could] |

### Non-Functional Requirements

| ID | Requirement | Metric |
|----|-------------|--------|
| NFR-1 | [Performance/Security/etc.] | [Measurable target] |

## Data Model

### [Entity Name]

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | Yes | Unique identifier |
| [field] | [type] | [Yes/No] | [Description] |
| [field] | [type] | [Yes/No] | [Description] |

### Relationships

[Entity A] 1──────* [Entity B]
     │
     └──────1 [Entity C]

## API Contract

### [Endpoint/Method Name]

**Endpoint:** `[METHOD] /path/to/resource`

**Request:**

{
  "[field]": "[type] - [description]"
}

**Response:**

{
  "[field]": "[type] - [description]"
}

**Errors:**

| Status | Code | Description |
|--------|------|-------------|
| 400 | INVALID_INPUT | [When this occurs] |
| 404 | NOT_FOUND | [When this occurs] |

## Validation Rules

| Field | Rule | Error Message |
|-------|------|---------------|
| [field] | [validation rule] | [user-facing message] |

## Constraints

- [Constraint 1 - e.g., Maximum 100 items per request]
- [Constraint 2 - e.g., Field X must be unique per user]

## Dependencies

| Dependency | Type | Purpose |
|------------|------|---------|
| [Service/Component] | [Internal/External] | [Why needed] |

## Security Considerations

- [Security requirement 1]
- [Security requirement 2]

## Related Documents

- [Architecture Decision Record](../architecture/ADR-XXX.md)
- [API Reference](../reference/api/ENDPOINT.md)
```

---

## Quality Checklist

Apply this checklist before finalizing any reference documentation.

### Completeness

- [ ] All parameters/options are documented
- [ ] All return values/responses are documented
- [ ] All error codes/states are documented
- [ ] All edge cases are covered
- [ ] No TODO or TBD sections remain

### Accuracy

- [ ] Information matches current implementation
- [ ] Code examples have been tested
- [ ] Type information is correct
- [ ] Default values are accurate
- [ ] Constraints are verified

### Structure

- [ ] Consistent format throughout
- [ ] Tables used for structured data
- [ ] Matches the structure of what's documented
- [ ] Logical organization

### Architecture-Agnostic

- [ ] Documents data requirements, not UI
- [ ] Documents API contracts, not framework code
- [ ] Could be used to build a CLI equivalent
- [ ] No implementation-specific details

### Clarity

- [ ] Descriptions are factual and precise
- [ ] No ambiguous language
- [ ] Technical terms are consistent
- [ ] Required vs optional is clear

### Neutrality

- [ ] No opinions or recommendations
- [ ] No tutorial-style instructions
- [ ] No how-to content mixed in
- [ ] Tone is austere and professional

### Maintainability

- [ ] Single source of truth (no duplicates)
- [ ] Version/date stamp if time-sensitive
- [ ] Cross-references use relative links
- [ ] Easy to update when API changes

### Formatting

- [ ] Consistent table structure
- [ ] Code blocks have language specified
- [ ] Proper use of inline code for values
- [ ] No broken links

### Documentation Index

- [ ] If a new file was created, moved, or removed: regenerate the CLAUDE.md documentation index via `/docs-management:generate-index`
