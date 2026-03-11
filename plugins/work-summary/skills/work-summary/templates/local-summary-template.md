# Local Summary Template

File structure for `.claude/work-summaries/{TICKET_KEY}.md`. This file serves as a local
reference and audit trail for work summaries posted to Jira.

When appending to an existing file, add a separator line before the new entry.

```markdown
# Work Summary: {TICKET_KEY}

## {YYYY-MM-DD HH:MM} - {Ticket Title}

**Branch**: `{branch-name}`
**Commits**: {count}
**Files Modified**: {count}
**PR**: {URL or "None"}
**Posted to Jira**: {Yes/No} - {timestamp if posted}

---

### Client-Friendly Summary

{Full client-friendly summary content}

---

### Technical Summary

{Full technical summary content}

---

### Deployment Information
- Feature branch: `{branch-name}`
- PR: {URL or "Not yet created"}
- Status: {Ready for review / Ready for testing / In progress}
```

## Append Separator

When appending a new summary to an existing file, insert this separator:

```markdown

---
---

## {YYYY-MM-DD HH:MM} - {Ticket Title} (Updated)

{New summary content follows the same structure above}
```
