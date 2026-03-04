# Section Format Templates

Format variants for each section, controlled by configuration settings.

## Header

### header (default — standard)

```markdown
# {MEETING_TITLE}

**Date:** {DATE} | **Time:** {TIME} {TZ} | **Duration:** {DURATION}

**Meeting Recording:** [{MEETING_TITLE}]({TLDV_URL})
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

## Meeting Link

In the default (standard) format, the meeting recording link is included inline in the header. When `meeting_details_format: listed`, it appears as a bold-labeled line in the header details. A separate "Meeting Link" section is only needed if the link is not already in the header.

## Attendees

```markdown
## Attendees

- **{ORGANIZER_NAME}** (Organizer) - {EMAIL}
- {ATTENDEE_2} - {EMAIL}
- {ATTENDEE_3} - {EMAIL}
```

When name is unavailable, fall back to email address only.

## Summary

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

## Discussion Notes

### discussion_notes (default — bulleted)

```markdown
## Discussion Notes

### {TOPIC_TITLE}

- {KEY_POINT_1}
- {KEY_POINT_2}
- {KEY_POINT_3}
```

### discussion_notes (discussion_notes_format: prose)

```markdown
## Discussion Notes

### {TOPIC_TITLE}

{PROSE_PARAGRAPH_ABOUT_TOPIC}
```

## Action Items

### action_items (default — grouped_by_person)

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

Variations:

- **Single owner:** Top-level bold name, tasks as sub-bullets with optional due date in italics
- **Shared task:** Combine owners with ` / ` separator
- **No action items:** `- _No action items identified_`

### action_items (action_items_format: flat)

```markdown
## Action Items

- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION}
- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION} (Due: {DATE})
- [ ] {TASK_DESCRIPTION}
```

## Footer

```markdown
---

{FOOTER}
```

Default footer: `*Generated automatically from TLDV recording*`
