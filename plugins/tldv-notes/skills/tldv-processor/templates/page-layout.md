# Page Layout Template

The overall structure for a meeting notes page.
Only sections enabled in the user's configuration will be included.

```markdown
# {MEETING_TITLE}

**Date:** {DATE} | **Time:** {TIME} {TZ} | **Duration:** {DURATION}

**Meeting Recording:** [{MEETING_TITLE}]({TLDV_URL})

## Attendees

- **{ORGANIZER_NAME}** (Organizer) - {EMAIL}
- {ATTENDEE_2} - {EMAIL}
- {ATTENDEE_3} - {EMAIL}

## Summary

- {HIGHLIGHT_1}
- {HIGHLIGHT_2}
- {HIGHLIGHT_3}

## Discussion Notes

### {TOPIC_TITLE}

- {KEY_POINT_1}
- {KEY_POINT_2}
- {KEY_POINT_3}

## Action Items

- **{PERSON_1}**: {TASK_1}
- **{PERSON_1}**: {TASK_2} *(by {DUE_DATE})*
- **{PERSON_2}**: {TASK_3}

---

{FOOTER}
```
