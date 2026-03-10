# Review Display Format

Use this format when presenting summaries to the user for review (Step 7) and when posting
the combined comment to Jira (Step 8). The client-friendly and technical sections use the
templates defined in `client-summary-template.md` and `technical-summary-template.md`.

```markdown
## Work Summary: {TICKET_KEY}

**Ticket**: {TICKET_KEY}: {Ticket Title}
**Branch**: `{branch-name}`
**Commits**: {count}
**Files Modified**: {count}
**PR**: {URL or "None"}

---

{Client-Friendly Summary from client-summary-template.md}

---

{Technical Summary from technical-summary-template.md}

---

### Deployment Information
- Feature branch: `{branch-name}`
- PR: {URL or "Not yet created"}
- Status: {Ready for review / Ready for testing / In progress}
```
