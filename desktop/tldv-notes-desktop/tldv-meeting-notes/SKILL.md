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

## Required Tools

This skill requires MCP tools from two integrations. Search your available tools to find them.

### TLDV MCP Tools (for meeting data)

Look for these tools by name — they may appear with a server prefix (e.g., `mcp__tldv__list-meetings` or similar):

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| `list-meetings` | List meetings with filters | `from`, `to` (ISO datetime), `onlyParticipated` (boolean), `limit` (integer) |
| `get-meeting-metadata` | Get meeting details by ID | `id` (string) |
| `get-transcript` | Get speaker-attributed transcript | `meetingId` (string) |
| `get-highlights` | Get AI-extracted highlights | `meetingId` (string) |

### Atlassian / Confluence Tools (for publishing pages)

Look for Confluence tools by searching for tools containing "confluence" or "atlassian". Common tool names include:
- `confluence_create_page` or `createConfluencePage` — create a new page
- `confluence_search` or `searchConfluenceUsingCql` — search for pages
- `confluence_get_page` or `getConfluencePage` — read a page
- `getConfluenceSpaces` or `confluence_search` — list spaces
- `getAccessibleAtlassianResources` — list cloud instances (for Cloud ID discovery)

If any required tools are not available, inform the user and explain which integration (TLDV or Atlassian) needs to be installed or enabled.

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

1. **Cloud ID** — Use `getAccessibleAtlassianResources` (or equivalent available Atlassian tool) to list cloud instances. Let the user pick their instance.
2. **Space ID** — Use `getConfluenceSpaces` (or equivalent) to list Confluence spaces for the chosen Cloud ID. Show names and keys, let the user pick.
3. **Parent Page ID** — Ask where notes should go. Search for pages using `confluence_search` or `searchConfluenceUsingCql`, or ask the user to paste the page URL and extract the ID.

Once discovered, confirm the values with the user so they can be reused in future conversations.

### Format Settings

These control how each section is rendered. Use the defaults unless the user requests changes. See `templates/section-formats.md` for the exact template of each variant.

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

Call the `list-meetings` tool with:
- `onlyParticipated: true`
- `from`: start of date range (ISO 8601 datetime in configured timezone)
- `to`: end of date range (ISO 8601 datetime in configured timezone)
- `limit: 50`

If a specific meeting ID was requested, skip the list and go directly to Step 3 for that meeting.

If no meetings found, report: "No meetings found for the specified period."

### Step 3: For Each Meeting, Gather Data

For each meeting, call these TLDV tools:

1. **Metadata** — `get-meeting-metadata` with `id: "<meeting_id>"` → returns title, date, start time, end time, duration, attendees, organizer, recording URL
2. **Transcript** — `get-transcript` with `meetingId: "<meeting_id>"` → returns speaker-attributed conversation text
3. **Highlights** — `get-highlights` with `meetingId: "<meeting_id>"` → returns AI-extracted key points, topics, and action items

### Step 4: Generate Structured Notes

Read `templates/page-layout.md` for the full page structure and section order.
Read `templates/section-formats.md` for the exact rendering of each section based on the user's format settings.
Read `templates/empty-states.md` for fallback content when data is missing.

Assemble the page using only the enabled sections and the user's chosen format variants.

### Step 5: Create Confluence Page

**If dry run:** Display the generated markdown to the user. Do not create a page. Label output clearly as "[DRY RUN] Preview".

**If publishing:** Use the `confluence_create_page` or `createConfluencePage` tool to create a Confluence page with:
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

## Error Handling

- **No meetings found** — Report "No meetings found for the specified period"
- **Missing transcript** — Create page with available data, note transcript unavailable
- **Missing highlights** — Generate summary from transcript if possible
- **Confluence error** — Report the error, offer to display the notes as markdown so the user can copy them
- **Configuration missing** — Walk the user through interactive discovery (see Configuration section)
- **Tools not available** — Inform the user which integration (TLDV or Atlassian) needs to be installed or enabled
