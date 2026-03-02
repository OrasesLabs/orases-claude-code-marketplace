# Confluence Note Templates

These templates define the structure for generated meeting notes.
Only sections enabled in the user's configuration will be included.

## Standard Meeting Notes Template

```markdown
# {MEETING_TITLE}

**Date:** {DATE}
**Duration:** {DURATION}

---

## Meeting Link

[View Recording]({TLDV_URL})

## Attendees

{ATTENDEE_LIST}

## Summary

{SUMMARY_BULLETS}

## Discussion Notes

{TOPIC_SECTIONS}

## Action Items

{ACTION_ITEMS}

---

{FOOTER}
```

## Section Templates

### header

```markdown
# {MEETING_TITLE}

**Date:** {DATE}
**Duration:** {DURATION}
```

### meeting_link

```markdown
## Meeting Link

[View Recording]({TLDV_URL})
```

### attendees

```markdown
## Attendees

{ATTENDEE_LIST}
```

### summary

```markdown
## Summary

{SUMMARY_BULLETS}
```

### discussion_notes

```markdown
## Discussion Notes

{TOPIC_SECTIONS}
```

### action_items

```markdown
## Action Items

{ACTION_ITEMS}
```

### footer

```markdown
---

{FOOTER}
```

Default footer: `*Generated automatically from TLDV recording*`

## Topic Section Template

```markdown
### {TOPIC_TITLE}

{HIGHLIGHTS_FOR_TOPIC}

**Key Points:**
{BULLET_POINTS}
```

## Action Item Formats

### With Assignee
```markdown
- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION}
```

### With Deadline
```markdown
- [ ] {TASK_DESCRIPTION} (Due: {DATE})
```

### With Assignee and Deadline
```markdown
- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION} (Due: {DATE})
```

### General
```markdown
- [ ] {TASK_DESCRIPTION}
```

## Attendee List Formats

### With Roles
```markdown
- {NAME} (Organizer)
- {NAME}
- {NAME}
```

### From Email (when name unavailable)
```markdown
- {EMAIL}
```

## Empty State Messages

### No Summary Available
```markdown
_No summary available - transcript may be processing_
```

### No Action Items
```markdown
- _No action items identified_
```

### No Transcript
```markdown
_Transcript not yet available for this meeting_
```

## Meeting Type Variations

### Standup/Daily Sync
Shorter format, focus on:
- Blockers mentioned
- Progress updates
- Quick decisions

### Planning/Sprint Meeting
Include:
- Decisions made
- Items prioritized
- Assignments

### Client Call
Emphasize:
- Client requests
- Commitments made
- Follow-up items
- Timeline discussions

### 1:1 Meeting
Focus on:
- Discussion topics
- Feedback given/received
- Career/growth items
- Action items for both parties
