# Page Layout Template

The overall structure for a meeting notes Confluence page.
Only sections enabled by the user will be included. Assemble the page using the section order shown below.

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

- **{PERSON_1}**
  - {TASK_1}
  - {TASK_2} *(by Wednesday)*
- **{PERSON_2}**
  - {TASK_3}
- **{PERSON_3} / {PERSON_4}**
  - {SHARED_TASK} *(by Friday)*

---

*Generated automatically from TLDV recording*
```

## Section Order

1. Header (title + meeting details + recording link)
2. Attendees
3. Summary
4. Discussion Notes
5. Action Items
6. Footer

## Meeting Type Variations

Adjust note emphasis based on the type of meeting:

- **Standup/Daily Sync** — Shorter format, focus on blockers, progress updates, quick decisions
- **Planning/Sprint Meeting** — Emphasize decisions made, items prioritized, assignments
- **Client Call** — Emphasize client requests, commitments made, follow-up items, timeline discussions
- **1:1 Meeting** — Focus on discussion topics, feedback given/received, career/growth items, action items for both parties
