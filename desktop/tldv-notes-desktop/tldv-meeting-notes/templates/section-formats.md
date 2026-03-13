# Section Format Templates

Format variants for each section, controlled by user preferences.

**Important:** `{TZ}` must be the DST-aware abbreviation (e.g., EDT during daylight saving, EST during standard time). See the "Timezone and Daylight Saving Time" section in SKILL.md.

## Header

### Standard (default)

```markdown
# {MEETING_TITLE}

**Date:** {DATE} | **Time:** {TIME} {TZ} | **Duration:** {DURATION}

**Meeting Recording:** [{MEETING_TITLE}]({TLDV_URL})
```

### Listed (meeting_details_format: listed)

```markdown
# {MEETING_TITLE}

**Date:** {DATE} at {TIME}
**Duration:** {DURATION}
**Organizer:** {ORGANIZER}
**Recording:** [View Recording]({TLDV_URL})
```

## Attendees

```markdown
## Attendees

- **{ORGANIZER_NAME}** (Organizer) - {EMAIL}
- {ATTENDEE_2} - {EMAIL}
- {ATTENDEE_3} - {EMAIL}
```

When name is unavailable, fall back to email address only.

## Summary

### Bullets (default)

```markdown
## Summary

- {HIGHLIGHT_1}
- {HIGHLIGHT_2}
- {HIGHLIGHT_3}
```

### Paragraph (summary_format: paragraph)

```markdown
## Summary

{COHESIVE_PROSE_PARAGRAPH_SYNTHESIZING_HIGHLIGHTS}
```

## Discussion Notes

### Bulleted (default)

```markdown
## Discussion Notes

### {TOPIC_TITLE}

- {KEY_POINT_1}
- {KEY_POINT_2}
- {KEY_POINT_3}
```

### Prose (discussion_notes_format: prose)

```markdown
## Discussion Notes

### {TOPIC_TITLE}

{PROSE_PARAGRAPH_ABOUT_TOPIC}
```

## Action Items

### Grouped by Person (default)

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

Rules:
- Single owner: bold name as top-level bullet, tasks as sub-bullets
- Due dates: inline in italics
- Shared task: combine owners with ` / ` separator
- No action items: `- _No action items identified_`

### Flat (action_items_format: flat)

```markdown
## Action Items

- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION}
- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION} (Due: {DATE})
```

## Duration Calculation

- **ceil_15m** (default): Round up to nearest 15 minutes — 28 min → 30 min, 42 min → 45 min, 31 min → 45 min, 60 min → 60 min
- **exact**: Display exact duration

## Footer

```markdown
---

{FOOTER}
```

Default footer: `*Generated automatically from TLDV recording*`
