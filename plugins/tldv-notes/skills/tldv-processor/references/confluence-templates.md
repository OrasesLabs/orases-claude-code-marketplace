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

### header (default)

```markdown
# {MEETING_TITLE}

**Date:** {DATE}
**Duration:** {DURATION}
```

### header (meeting_details_format: listed)

Render meeting details as bold-labeled fields on separate lines. Include the recording link inline. Attendees are moved to their own section.

```markdown
# {MEETING_TITLE}

**Date:** {DATE} at {TIME}
**Duration:** {DURATION}
**Organizer:** {ORGANIZER}
**Recording:** [View Recording]({TLDV_URL})
```

### meeting_link (default)

```markdown
## Meeting Link

[View Recording]({TLDV_URL})
```

Note: When `meeting_details_format: listed`, the recording link is included in the header details above — omit this separate section.

### attendees (default)

```markdown
## Attendees

{ATTENDEE_LIST}
```

### attendees (meeting_details_format: listed)

```markdown
## Attendees

- **{ORGANIZER_NAME}** (Organizer)
- {ATTENDEE_2}
- {ATTENDEE_3}
```

### summary (default — bullets)

```markdown
## Summary

- {HIGHLIGHT_1}
- {HIGHLIGHT_2}
- {HIGHLIGHT_3}
```

### summary (summary_format: paragraph)

```markdown
## Summary

{COHESIVE_PROSE_PARAGRAPH_SYNTHESIZING_HIGHLIGHTS}
```

### discussion_notes (default — prose)

```markdown
## Discussion Notes

### {TOPIC_TITLE}

{PROSE_PARAGRAPH_ABOUT_TOPIC}
```

### discussion_notes (discussion_notes_format: bulleted)

```markdown
## Discussion Notes

### {TOPIC_TITLE}

- {KEY_POINT_1}
- {KEY_POINT_2}
- {KEY_POINT_3}
```

### action_items (default — flat checklist)

```markdown
## Action Items

{ACTION_ITEMS}
```

### action_items (action_items_format: grouped_by_person)

```markdown
## Action Items

- **{PERSON_1}**
  - {TASK_1}
  - {TASK_2} *(by Wednesday)*
- **{PERSON_2}**
  - {TASK_3}
- **{PERSON_3} / {PERSON_4}**
  - {SHARED_TASK} *(by Friday)*
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

### Default (flat checklist)

#### With Assignee
```markdown
- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION}
```

#### With Deadline
```markdown
- [ ] {TASK_DESCRIPTION} (Due: {DATE})
```

#### With Assignee and Deadline
```markdown
- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION} (Due: {DATE})
```

#### General
```markdown
- [ ] {TASK_DESCRIPTION}
```

### Grouped by Person (action_items_format: grouped_by_person)

#### Single owner
```markdown
- **{PERSON}**
  - {TASK_DESCRIPTION}
  - {TASK_DESCRIPTION} *(by {DUE_DATE})*
```

#### Shared across multiple owners
```markdown
- **{PERSON_1} / {PERSON_2}**
  - {SHARED_TASK_DESCRIPTION}
```

#### No action items
```markdown
- _No action items identified_
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
