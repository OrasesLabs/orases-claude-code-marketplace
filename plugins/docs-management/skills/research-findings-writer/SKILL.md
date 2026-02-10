---
name: research-findings-writer
description: Guidelines for documenting research findings and investigation results. Use when writing content about discoveries, analysis, and recommendations from code analysis, API testing, or other research.
allowed-tools: Read, Write, Edit, Glob
---

# Research Documentation Skill

This skill provides guidelines for creating **research** documentation - investigative findings and discovery results.

## Purpose

Research documentation captures **findings from investigations** - what was discovered, how it was discovered, and what it means. Users consult it to understand past research and build on existing knowledge.

## User Need

> "What did we learn about X?"

## Characteristics

| Attribute | Description |
|-----------|-------------|
| **Orientation** | Discovery |
| **Focus** | Findings and recommendations |
| **Goal** | Capture and share knowledge |
| **Tone** | Objective, analytical |

## Target Directory

Place research documentation in: `docs/research/findings/`

## Writing Guidelines

### DO

- State the research question clearly
- Document methodology transparently
- Provide evidence for each finding
- Include confidence levels
- Acknowledge limitations
- Make actionable recommendations
- Date-stamp for temporal context

### DON'T

- Present opinions as facts
- Skip the methodology section
- Omit limitations or gaps
- Make recommendations without evidence
- Assume findings are permanent (they may become outdated)

## Examples of Good Research Docs

- "Authentication Flow Analysis"
- "Performance Bottleneck Investigation"
- "Third-Party API Capabilities Research"
- "Security Vulnerability Assessment"
- "Technology Comparison Study"

---

## Template

Use this template when documenting research findings:

```markdown
# [Topic] Research

*Research date: [YYYY-MM-DD]*
*Researcher: [Name/Agent]*
*Confidence: [High | Medium | Low]*

## Summary

[2-3 sentences summarizing the key findings]

## Background

[Why this research was conducted - what question were we trying to answer?]

## Methodology

[How the research was conducted]

- [Method 1 - e.g., Code analysis of repository X]
- [Method 2 - e.g., API testing with tool Y]
- [Method 3 - e.g., Documentation review]

## Findings

### Finding 1: [Title]

[Detailed description of what was discovered]

**Evidence:**

[Code, logs, or data supporting this finding]

### Finding 2: [Title]

[Detailed description]

**Evidence:**

[Supporting data]

### Finding 3: [Title]

[Detailed description]

## Analysis

[Interpretation of the findings - what do they mean?]

## Limitations

- [What we couldn't verify or access]
- [Assumptions made]
- [Potential gaps in the research]

## Recommendations

Based on these findings:

1. [Actionable recommendation]
2. [Actionable recommendation]
3. [Actionable recommendation]

## Next Steps

- [ ] [Follow-up action 1]
- [ ] [Follow-up action 2]

## References

- [Link to relevant documentation]
- [Link to source code analyzed]
- [Link to related research]

---

*This research may become outdated. Verify findings before making critical decisions.*
```

---

## Quality Checklist

Apply this checklist before finalizing any research documentation.

### Research Question

- [ ] Research question/goal is clearly stated
- [ ] Background explains why research was needed
- [ ] Scope is defined

### Methodology

- [ ] Methods are documented transparently
- [ ] Tools and techniques are specified
- [ ] Process is reproducible

### Findings

- [ ] Each finding is clearly stated
- [ ] Evidence supports each finding
- [ ] Confidence level is appropriate
- [ ] Findings answer the research question

### Analysis

- [ ] Interpretation is logical
- [ ] Analysis follows from evidence
- [ ] Alternative explanations considered

### Limitations

- [ ] Gaps are acknowledged
- [ ] Assumptions are stated
- [ ] Scope limitations are clear

### Recommendations

- [ ] Recommendations are actionable
- [ ] Recommendations follow from findings
- [ ] Next steps are clear

### Temporal Context

- [ ] Date-stamped
- [ ] Time-sensitive findings are marked
- [ ] Outdating risk is acknowledged

### Formatting

- [ ] Consistent heading structure
- [ ] Evidence is properly formatted
- [ ] Links are functional
- [ ] No broken references

### Documentation Index

- [ ] If a new file was created, moved, or removed: regenerate the CLAUDE.md documentation index via `/docs-management:generate-index`
