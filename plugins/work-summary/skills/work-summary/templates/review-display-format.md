# Review Display Format

Use this format when presenting summaries to the user for review (Step 8) and when posting
the combined comment to Jira (Step 9).

If a `review_display_template` path is configured in the work-summary settings file, use
that template instead of this one.

The client-friendly and technical sections use the templates defined in:
- `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/client-summary-template.md`
- `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/technical-summary-template.md`

Or their respective override paths (`client_summary_template`, `technical_summary_template`)
if configured in settings.

```markdown
## Work Summary: {TICKET_KEY}

**Ticket**: {TICKET_KEY}: {Ticket Title}
**Branch**: `{branch-name}`
**Commits**: {count}
**Files Modified**: {count}
**PR/MR**: {URL or "None"}

---

{Client-Friendly Summary — from client-summary-template.md or configured override}

---

{Technical Summary — from technical-summary-template.md or configured override}

---

### Deployment Information
- Feature branch: `{branch-name}`
- PR/MR: {URL or "Not yet created"}
- Status: {Ready for review / Ready for testing / In progress}
```
