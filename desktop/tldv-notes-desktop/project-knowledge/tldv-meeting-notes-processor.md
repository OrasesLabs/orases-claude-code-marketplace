# TLDV Meeting Notes Processor

This document contains all instructions for processing TLDV meeting recordings and creating structured Confluence pages.

## Configuration

Edit the values below to match your Atlassian environment. These are required for creating Confluence pages.

```yaml
cloud_id: "YOUR_CLOUD_ID"
space_id: "YOUR_SPACE_ID"
parent_page_id: "YOUR_PARENT_PAGE_ID"
timezone: "America/New_York"
```

If the values above are still placeholders, use `getAccessibleAtlassianResources` to discover the Cloud ID, `getConfluenceSpaces` to find the Space ID, and `searchConfluenceUsingCql` to locate the Parent Page ID. Walk the user through each step interactively.

### Format Settings

These control how each section is rendered. Defaults are shown — change only what you need.

| Setting | Default | Options |
|---------|---------|---------|
| `duration_rounding` | `ceil_15m` | `ceil_15m` (round up to 15 min) / `exact` |
| `meeting_details_format` | `standard` | `standard` (date\|time\|duration on one line) / `listed` (separate lines) |
| `summary_format` | `bullets` | `bullets` / `paragraph` |
| `discussion_notes_format` | `bulleted` | `bulleted` / `prose` |
| `action_items_format` | `grouped_by_person` | `grouped_by_person` / `flat` |
| `footer` | `*Generated automatically from TLDV recording*` | Any text |

### Enabled Sections

All sections are enabled by default. Remove any you don't want:

- header
- meeting_link
- attendees
- summary
- discussion_notes
- action_items
- footer

## MCP Tools

### TLDV Tools

- `list-meetings` — List meetings (use `onlyParticipated: true`)
- `get-meeting-metadata` — Get meeting details (title, date, attendees, URL)
- `get-transcript` — Get speaker-attributed transcript
- `get-highlights` — Get AI-extracted key points

### Atlassian Tools (Claude.ai Integration)

- `createConfluencePage` — Create the notes page (params: cloudId, spaceId, body, contentFormat, parentId, title)
- `getConfluenceSpaces` — List available spaces (params: cloudId)
- `searchConfluenceUsingCql` — Search for pages (params: cloudId, cql)
- `getAccessibleAtlassianResources` — Discover Cloud IDs (no params)

## Workflow

### Step 1: Load Configuration

Read the configuration values from the Configuration section above.
If any required values (`cloud_id`, `space_id`, `parent_page_id`) are still placeholders, help the user discover them interactively:

1. **Cloud ID** — Call `getAccessibleAtlassianResources` to list available cloud instances. Let the user pick one.
2. **Space ID** — Call `getConfluenceSpaces` with the Cloud ID. Show space names and keys, let the user pick.
3. **Parent Page ID** — Ask the user where notes should go. Use `searchConfluenceUsingCql` to help them find the page, or ask them to paste the page URL and extract the ID.

Remind the user to update the Configuration section in this document with their values for next time.

### Step 2: Parse User Request

Extract options from the user's natural language request:

| Option | How to detect | Default |
|--------|---------------|---------|
| Days lookback | "last 3 days", "this week", "past 7 days" | 1 (today only) |
| Dry run | "preview", "don't publish", "dry run" | false |
| Specific meeting | "meeting ID abc123", references a specific meeting | none |
| Space override | "in the TEAM space", "space KEY" | from config |
| Parent override | "under page 12345" | from config |

### Step 3: Fetch Meetings

Call `list-meetings` with:
- `onlyParticipated: true`
- `from` / `to` date range based on days lookback (use configured timezone)
- `limit: 50`

If a specific meeting ID was requested, skip the list and go directly to Step 4 for that meeting.

If no meetings found, report: "No meetings found for the specified period."

### Step 4: For Each Meeting, Gather Data

For each meeting, call these in sequence:

1. **Metadata** — `get-meeting-metadata` with the meeting ID
   - Extract: title, date, start time, end time, duration, attendees, organizer, recording URL
2. **Transcript** — `get-transcript` with the meeting ID
   - Extract: speaker-attributed conversation text
3. **Highlights** — `get-highlights` with the meeting ID
   - Extract: AI-generated key points, topics, action items

### Step 5: Generate Structured Notes

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

### Step 6: Create Confluence Page

**If dry run:** Display the generated markdown to the user. Do not create a page. Label output clearly as "[DRY RUN] Preview".

**If publishing:** Call `createConfluencePage` with:
- `cloudId` — from configuration
- `spaceId` — from configuration (or override)
- `parentId` — from configuration (or override)
- `title` — meeting title with date, e.g. "Weekly Standup - March 10, 2026"
- `body` — the generated markdown content
- `contentFormat` — `"markdown"`

Ask for confirmation before creating each page (unless user pre-approved batch processing).

### Step 7: Report Results

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
- **Configuration missing** — Walk the user through interactive setup (see Step 1)
