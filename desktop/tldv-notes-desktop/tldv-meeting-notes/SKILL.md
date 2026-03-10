---
name: tldv-meeting-notes
description: Process TLDV meeting recordings and create structured Confluence pages with summaries, discussion notes, and action items.
---

# TLDV Meeting Notes Processor

Process TLDV meeting recordings and create structured Confluence pages with summaries, discussion topics, and action items.

## How Users Will Ask

Users will ask using natural language like:
- "Create meeting notes from today's calls"
- "Process my TLDV meetings from the last 3 days"
- "Summarize my meetings to Confluence"
- "Generate notes for meeting [ID]"
- "Preview my meeting notes" (dry run — no pages created)

## Required Connectors

This skill requires two connectors to be enabled in your organization:
- **TLDV** — for fetching meetings, transcripts, and highlights
- **Atlassian** — for creating Confluence pages

If either connector is not available, inform the user and explain which connector needs to be enabled by their organization admin.

## Configuration

The user's Confluence environment details are needed to create pages. Ask the user for these values on first use if not previously provided:

```yaml
cloud_id: ""
space_id: ""
parent_page_id: ""
timezone: "America/New_York"
```

### Interactive Discovery

If configuration values are unknown, help the user discover them:

1. **Cloud ID** — Use the Atlassian connector to list accessible cloud resources. Let the user pick their instance.
2. **Space ID** — Use the Atlassian connector to list Confluence spaces for the chosen Cloud ID. Show names and keys, let the user pick.
3. **Parent Page ID** — Ask where notes should go. Use the Atlassian connector to search for pages, or ask the user to paste the page URL and extract the ID.

Once discovered, confirm the values with the user so they can be reused in future conversations.

### Format Settings

These control how each section is rendered. Use the defaults unless the user requests changes.

| Setting | Default | Options |
|---------|---------|---------|
| `duration_rounding` | `ceil_15m` | `ceil_15m` (round up to 15 min) / `exact` |
| `meeting_details_format` | `standard` | `standard` (date\|time\|duration on one line) / `listed` (separate lines) |
| `summary_format` | `bullets` | `bullets` / `paragraph` |
| `discussion_notes_format` | `bulleted` | `bulleted` / `prose` |
| `action_items_format` | `grouped_by_person` | `grouped_by_person` / `flat` |
| `footer` | `*Generated automatically from TLDV recording*` | Any text |

### Enabled Sections

All sections are enabled by default. The user may request to exclude any:

- header
- meeting_link
- attendees
- summary
- discussion_notes
- action_items
- footer

## Workflow

### Step 1: Parse User Request

Extract options from the user's natural language request:

| Option | How to detect | Default |
|--------|---------------|---------|
| Days lookback | "last 3 days", "this week", "past 7 days" | 1 (today only) |
| Dry run | "preview", "don't publish", "dry run" | false |
| Specific meeting | "meeting ID abc123", references a specific meeting | none |
| Space override | "in the TEAM space", "space KEY" | from config |
| Parent override | "under page 12345" | from config |

### Step 2: Fetch Meetings

Use the TLDV connector to list meetings with:
- Only meetings the user participated in
- Date range based on days lookback (use configured timezone)
- Limit of 50

If a specific meeting ID was requested, skip the list and go directly to Step 3 for that meeting.

If no meetings found, report: "No meetings found for the specified period."

### Step 3: For Each Meeting, Gather Data

For each meeting, use the TLDV connector to fetch:

1. **Metadata** — meeting details (title, date, start time, end time, duration, attendees, organizer, recording URL)
2. **Transcript** — speaker-attributed conversation text
3. **Highlights** — AI-extracted key points, topics, and action items

### Step 4: Generate Structured Notes

Create markdown content using only the enabled sections. Follow the templates below based on the configured format settings.

#### Duration Calculation

- If `duration_rounding: ceil_15m` — Round up to the nearest 15 minutes: 28 min → 30 min, 42 min → 45 min, 31 min → 45 min, 60 min → 60 min
- If `duration_rounding: exact` — Display exact duration

#### Header Section

**Standard format** (default):

```markdown
# {MEETING_TITLE}

**Date:** {DATE} | **Time:** {TIME} {TZ} | **Duration:** {DURATION}

**Meeting Recording:** [{MEETING_TITLE}]({TLDV_URL})
```

**Listed format** (`meeting_details_format: listed`):

```markdown
# {MEETING_TITLE}

**Date:** {DATE} at {TIME}
**Duration:** {DURATION}
**Organizer:** {ORGANIZER}
**Recording:** [View Recording]({TLDV_URL})
```

#### Attendees Section

```markdown
## Attendees

- **{ORGANIZER_NAME}** (Organizer) - {EMAIL}
- {ATTENDEE_2} - {EMAIL}
- {ATTENDEE_3} - {EMAIL}
```

When name is unavailable, fall back to email address only.

#### Summary Section

**Bullets format** (default):

```markdown
## Summary

- {HIGHLIGHT_1}
- {HIGHLIGHT_2}
- {HIGHLIGHT_3}
```

**Paragraph format** (`summary_format: paragraph`):

```markdown
## Summary

{COHESIVE_PROSE_PARAGRAPH_SYNTHESIZING_HIGHLIGHTS}
```

#### Discussion Notes Section

**Bulleted format** (default):

```markdown
## Discussion Notes

### {TOPIC_TITLE}

- {KEY_POINT_1}
- {KEY_POINT_2}
- {KEY_POINT_3}
```

**Prose format** (`discussion_notes_format: prose`):

```markdown
## Discussion Notes

### {TOPIC_TITLE}

{PROSE_PARAGRAPH_ABOUT_TOPIC}
```

#### Action Items Section

**Grouped by person** (default):

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

- Single owner: bold name as top-level bullet, tasks as sub-bullets with optional due date in italics
- Shared task: combine owners with ` / ` separator
- No action items: `- _No action items identified_`

**Flat format** (`action_items_format: flat`):

```markdown
## Action Items

- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION}
- [ ] **{ASSIGNEE}**: {TASK_DESCRIPTION} (Due: {DATE})
```

#### Footer Section

```markdown
---

{FOOTER}
```

Default footer: `*Generated automatically from TLDV recording*`

### Step 5: Create Confluence Page

**If dry run:** Display the generated markdown to the user. Do not create a page. Label output clearly as "[DRY RUN] Preview".

**If publishing:** Use the Atlassian connector to create a Confluence page with:
- The configured Cloud ID, Space ID, and Parent Page ID (or overrides)
- Title: meeting title with date, e.g. "Weekly Standup - March 10, 2026"
- Body: the generated markdown content
- Content format: markdown

Ask for confirmation before creating each page (unless user pre-approved batch processing).

### Step 6: Report Results

For each meeting processed, report:
- Meeting title
- Date/time (in configured timezone)
- Confluence page URL (if created) or "[DRY RUN]" indicator
- Any errors encountered

## Note Generation Guidelines

### Summary Section

- Extract top 3-5 highlights as bullet points
- Focus on decisions, outcomes, and key discussions
- Keep each point concise (1-2 sentences)
- If `summary_format: paragraph` — write a single cohesive prose paragraph instead

### Discussion Notes

- Group by topic from TLDV's topic detection
- Render each topic's notes as bullet points under the topic heading
- Include relevant quotes from transcript
- Preserve speaker attribution for important statements
- If `discussion_notes_format: prose` — write as prose paragraphs instead

### Action Items Extraction

Look for:
- Explicit mentions of "action item", "to do", "follow up"
- Assignments: "[Person] will [task]"
- Deadlines mentioned
- Commitments made

Group items by owner with task sub-bullets. Include due dates inline in italics.
For shared tasks, combine owners with ` / ` separator.
If no action items found: `- _No action items identified_`

### Meeting Type Variations

Adjust note emphasis based on the type of meeting:

- **Standup/Daily Sync** — Shorter format, focus on blockers, progress updates, quick decisions
- **Planning/Sprint Meeting** — Emphasize decisions made, items prioritized, assignments
- **Client Call** — Emphasize client requests, commitments made, follow-up items, timeline discussions
- **1:1 Meeting** — Focus on discussion topics, feedback given/received, career/growth items, action items for both parties

## Empty States

When data is unavailable, use these fallbacks:

- **No summary:** `_No summary available — transcript may be processing_`
- **No action items:** `- _No action items identified_`
- **No transcript:** `_Transcript not yet available for this meeting_`

## Error Handling

- **No meetings found** — Report "No meetings found for the specified period"
- **Missing transcript** — Create page with available data, note transcript unavailable
- **Missing highlights** — Generate summary from transcript if possible
- **Confluence error** — Report the error, offer to display the notes as markdown so the user can copy them
- **Configuration missing** — Walk the user through interactive discovery (see Configuration section)
- **Connector not available** — Inform the user which connector needs to be enabled by their organization admin
