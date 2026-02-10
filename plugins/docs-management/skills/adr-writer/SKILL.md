---
name: adr-writer
description: Guidelines for creating Architecture Decision Records (ADRs). Use when documenting significant architectural decisions, their context, alternatives considered, and consequences.
allowed-tools: Read, Write, Edit, Glob
---

# Architecture Decision Record (ADR) Skill

This skill provides guidelines for creating **Architecture Decision Records** - structured documentation of significant architectural decisions.

## Purpose

ADRs capture **important architectural decisions** along with their context, alternatives considered, and consequences. They create a historical record of why things are built the way they are.

## User Need

> "Why did we decide to do it this way?"

## Characteristics

| Attribute | Description |
|-----------|-------------|
| **Orientation** | Decision documentation |
| **Focus** | Context, decision, consequences |
| **Goal** | Record rationale for future reference |
| **Tone** | Objective, comprehensive |

## Target Directory

Place ADRs in: `docs/architecture/` with naming convention `ADR-NNN-short-title.md`

## Writing Guidelines

### DO

- State the context and problem clearly
- Document all alternatives considered
- Explain why alternatives were rejected
- List both benefits and drawbacks
- Include implementation notes
- Use consistent status labels
- Number ADRs sequentially

### DON'T

- Skip the context section
- Omit alternatives that were considered
- Hide drawbacks of the chosen approach
- Forget to update status when decisions change
- Write ADRs for trivial decisions

## When to Write an ADR

- Choosing between competing technologies
- Establishing patterns that will be reused
- Making breaking changes to existing systems
- Decisions that are costly to reverse
- Decisions that affect multiple teams or components

## Examples of Good ADRs

- "ADR-001: Use PostgreSQL for primary database"
- "ADR-002: Adopt microservices architecture"
- "ADR-003: Implement event sourcing for audit log"
- "ADR-004: Choose React for frontend framework"
- "ADR-005: Use JWT for API authentication"

## ADR Status Values

| Status | Meaning |
|--------|---------|
| **Proposed** | Under discussion, not yet decided |
| **Accepted** | Decision made and in effect |
| **Deprecated** | No longer applies, but kept for history |
| **Superseded** | Replaced by another ADR (link to it) |

---

## Template

Use this template when creating an Architecture Decision Record:

```markdown
# ADR-[Number]: [Short Title]

*Date: [YYYY-MM-DD]*
*Status: [Proposed | Accepted | Deprecated | Superseded by ADR-XXX]*
*Deciders: [List of people involved in the decision]*

## Context

[Describe the issue motivating this decision. What is the problem we're facing? What constraints exist? What forces are at play?]

[Include relevant technical, business, and organizational context.]

## Decision

[State the decision that was made. Use active voice: "We will..." or "The system will..."]

[Be specific about what changes will be made and what approach will be taken.]

## Consequences

### Benefits

- [Positive outcome 1]
- [Positive outcome 2]
- [Positive outcome 3]

### Drawbacks

- [Negative outcome or trade-off 1]
- [Negative outcome or trade-off 2]

### Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk] | [Low/Med/High] | [Low/Med/High] | [How to address] |

## Alternatives Considered

### Alternative 1: [Name]

[Description of this alternative]

**Pros:**
- [Advantage]

**Cons:**
- [Disadvantage]

**Why rejected:** [Reason this wasn't chosen]

### Alternative 2: [Name]

[Description]

**Pros:**
- [Advantage]

**Cons:**
- [Disadvantage]

**Why rejected:** [Reason]

## Implementation Notes

[Any notes relevant to implementing this decision]

- [Implementation detail 1]
- [Implementation detail 2]

## References

- [Link to relevant documentation]
- [Link to discussion/RFC]
- [Link to related ADRs]

---

## Change Log

| Date | Author | Change |
|------|--------|--------|
| [Date] | [Name] | Initial draft |
```

---

## Quality Checklist

Apply this checklist before finalizing any ADR.

### Context

- [ ] Problem is clearly stated
- [ ] Constraints are documented
- [ ] Business and technical context included
- [ ] Scope is defined

### Decision

- [ ] Decision is explicitly stated
- [ ] Active voice used ("We will...")
- [ ] Specific about what changes
- [ ] Approach is clear

### Consequences

- [ ] Benefits are documented
- [ ] Drawbacks are honestly stated
- [ ] Risks are identified with mitigations
- [ ] Both short and long-term impacts considered

### Alternatives

- [ ] Multiple alternatives considered
- [ ] Each alternative fairly evaluated
- [ ] Rejection reasons are clear
- [ ] Pros and cons for each

### Metadata

- [ ] Status is current
- [ ] Date is accurate
- [ ] Deciders are listed
- [ ] ADR number is sequential

### ADR-Specific

- [ ] Appropriate for an ADR (not trivial)
- [ ] Self-contained and understandable
- [ ] Links to related ADRs if any
- [ ] Implementation notes if needed

### Maintainability

- [ ] References are linked
- [ ] Change log started
- [ ] Easy to update status later
- [ ] No broken links

### Formatting

- [ ] Consistent heading structure
- [ ] Tables properly formatted
- [ ] Lists are clear
- [ ] Readable and scannable

### Documentation Index

- [ ] If a new file was created, moved, or removed: regenerate the CLAUDE.md documentation index via `/docs-management:generate-index`
