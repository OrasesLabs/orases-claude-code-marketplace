# Client-Friendly Summary Template

Markdown structure for the client-friendly summary section. This targets non-technical
stakeholders. Adapt section content based on actual changes - omit sections that do not apply.

```markdown
### Client-Friendly Summary

#### What Changed
- Brief description of modifications in business terms
- User-facing impacts or improvements
- Integration points with existing features

#### QA Steps
1. {Step derived from code inspection}
2. {Step to confirm no regressions}
3. {Step to validate related functionality}

#### Related Tasks
- {TICKET_KEY}: {Brief description and relationship}
- {Links to related tickets from description or comments}

#### Testing Checklist
- [ ] {Acceptance criterion 1 - verified against code}
- [ ] {Acceptance criterion 2 - verified against code}
- [ ] No regressions in related features
- [ ] {Additional criteria from ticket comments if applicable}
```
