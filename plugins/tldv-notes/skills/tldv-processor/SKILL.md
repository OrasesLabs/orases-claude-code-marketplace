---
name: tldv-notes:tldv-processor
description: >
  This skill should be used when the user asks to "create meeting notes",
  "process TLDV meetings", "generate confluence notes from meetings",
  "summarize my meetings", "create notes from today's calls",
  or mentions TLDV recordings and Confluence page creation.
---

# TLDV Processor Skill

This skill processes TLDV meeting recordings and creates structured Confluence pages with meeting notes.

## Overview

Fetch meetings from TLDV where the user participated, extract transcripts and highlights, generate structured notes, and publish to Confluence.

## Configuration

This plugin supports per-user and per-project configuration via settings files.
Before processing, check for settings in this order:

1. `.claude/tldv-notes.local.md` - Project-local settings (not committed, gitignored)
2. `.claude/tldv-notes.md` - Project-scoped settings (can be committed for team defaults)
3. `~/.claude/tldv-notes.md` - User-global settings (applies across all projects)

Parse YAML frontmatter for: `cloud_id`, `space_id`, `parent_page_id`, `timezone`, `sections`, `footer`, `mcp_server`, `duration_rounding`, `meeting_details_format`, `summary_format`, `discussion_notes_format`, `action_items_format`.

### Timezone and Daylight Saving Time

The `timezone` value is an IANA timezone identifier. **You must account for Daylight Saving Time (DST) when converting timestamps.**

For `America/New_York`:
- **EST** (Eastern Standard Time) = **UTC-5** — first Sunday of November through second Sunday of March
- **EDT** (Eastern Daylight Time) = **UTC-4** — second Sunday of March through first Sunday of November

**To determine the correct offset:** Check the meeting's date against these DST boundaries. If the meeting occurred during DST, use UTC-4 and display "EDT". If outside DST, use UTC-5 and display "EST".

Common US timezone DST rules (all follow the same March–November schedule):
| IANA Timezone | Standard | DST |
|---|---|---|
| `America/New_York` | EST (UTC-5) | EDT (UTC-4) |
| `America/Chicago` | CST (UTC-6) | CDT (UTC-5) |
| `America/Denver` | MST (UTC-7) | MDT (UTC-6) |
| `America/Los_Angeles` | PST (UTC-8) | PDT (UTC-7) |

**When converting TLDV timestamps (which are in UTC) to local time:**
1. Determine whether DST is active on the meeting's date
2. Apply the correct UTC offset
3. Use the correct abbreviation (e.g., EDT not EST) in the displayed time

If no settings file exists, ask the user for the required values and offer to save them. When prompting interactively, use friendly names and provide clear options — not raw setting keys. For example:

| Setting key | Friendly prompt | Options / Help |
|---|---|---|
| `cloud_id` | "What is your Atlassian Cloud ID?" | Help the user find it: use Atlassian MCP tools like `getAccessibleAtlassianResources` to list their available cloud instances, or direct them to `https://admin.atlassian.com` → select their org → the Cloud ID is in the URL. |
| `space_id` | "Which Confluence Space should notes go to?" | Use `getConfluenceSpaces` to list available spaces and let the user pick one. Show space name and key. |
| `parent_page_id` | "What is the parent page ID for meeting notes?" | Help the user navigate: use `searchConfluenceUsingCql` to find pages in their chosen space, or ask them to paste the URL of the parent page and extract the ID from it. |
| `duration_rounding` | "How should meeting duration be displayed?" | "Rounded up to nearest 15 minutes (Recommended)" / "Exact duration" |
| `meeting_details_format` | "How should meeting details be laid out?" | "Standard format (Recommended)" / "Listed on separate lines" |
| `summary_format` | "How should the summary be written?" | "Bullet points (Recommended)" / "Single paragraph" |
| `discussion_notes_format` | "How should discussion notes be formatted?" | "Bullet points (Recommended)" / "Prose paragraphs" |
| `action_items_format` | "How should action items be organized?" | "Grouped by person (Recommended)" / "Flat checklist" |

Store the user's choices using the setting key names (e.g. `action_items_format: flat` to override the default grouped format).

## MCP Tools Required

### TLDV MCP Server

| Tool | Purpose | Key Parameters |
|------|---------|----------------|
| `mcp__tldv__list-meetings` | List meetings with filters | `from`, `to` (ISO datetime), `onlyParticipated` (boolean), `limit` (integer) |
| `mcp__tldv__get-meeting-metadata` | Get meeting details by ID | `id` (string) |
| `mcp__tldv__get-transcript` | Get speaker-attributed transcript | `meetingId` (string) |
| `mcp__tldv__get-highlights` | Get AI-extracted highlights | `meetingId` (string) |

### Atlassian MCP Server

| Tool | Purpose |
|------|---------|
| `mcp__atlassian__createConfluencePage` | Create the notes page |
| `mcp__atlassian__getConfluenceSpaces` | Find target space |
| `mcp__atlassian__searchConfluenceUsingCql` | Search for pages |
| `mcp__atlassian__getAccessibleAtlassianResources` | List cloud instances (for Cloud ID discovery) |

The MCP server prefix (`atlassian`) can be overridden via the `mcp_server` setting. Tools may appear under different prefixes depending on the environment — search for tools containing "confluence" or "atlassian" if the exact names above are not found.

## Workflow

### Step 1: Load Configuration

Read settings file and extract configuration values.
Fall back to interactive prompts if required values are missing.

### Step 2: Fetch Meetings

Retrieve recent meetings where user participated:

```
mcp__tldv__list-meetings with:
- onlyParticipated: true
- from: start of date range as ISO 8601 datetime with the correct UTC offset
  (e.g., 2026-03-13T00:00:00-04:00 for EDT, 2026-03-13T00:00:00-05:00 for EST)
  Check if DST is active on the target date — see Timezone and Daylight Saving Time section.
- to: end of date range, same offset rules as from
```

### Step 3: For Each Meeting, Gather Data

1. Get metadata: title, date, attendees, recording URL
2. Get transcript: speaker-attributed conversation
3. Get highlights: AI-extracted key points and topics

### Step 4: Generate Structured Notes

Create markdown using only the enabled sections from configuration.

Available sections:
1. **header** - Meeting title, date | time | duration on one line, and meeting recording link below
2. **meeting_link** - Included inline in the header by default (separate section only if `meeting_details_format: listed`)
3. **attendees** - Bulleted list of participants with organizer in **bold** and noted as "(Organizer)"
4. **summary** - 3-5 highlights as bullet points (format controlled by `summary_format`)
5. **discussion_notes** - Detailed notes grouped by topic as bullet points (format controlled by `discussion_notes_format`)
6. **action_items** - Extracted tasks grouped by person (format controlled by `action_items_format`)
7. **footer** - Configurable footer text

If the settings file has a markdown body, append it as "Custom Notes".

### Format Settings

These settings control how each section is rendered. When absent, the default format is used.

#### `duration_rounding`
Controls how meeting duration is displayed.
- `ceil_15m` (default): Round up to the nearest 15-minute increment — 28 min → 30 min, 42 min → 45 min, 31 min → 45 min, 60 min → 60 min
- `exact`: Display exact duration with no rounding

#### `meeting_details_format`
Controls how the header area is laid out.
- `standard` (default): Date | Time | Duration on a single pipe-separated line, meeting recording link below, then a separate `## Attendees` section with organizer in **bold**
- `listed`: Render date, time, duration, organizer, and recording link as bold-labeled fields on separate lines

#### `summary_format`
Controls how the summary section is written.
- `bullets` (default): Top highlights as bullet points
- `paragraph`: Single cohesive prose paragraph synthesizing the highlights

#### `discussion_notes_format`
Controls how discussion notes are rendered under each topic heading.
- `bulleted` (default): Bullet points under each topic heading
- `prose`: Prose paragraphs under each topic heading

#### `action_items_format`
Controls how action items are organized.
- `grouped_by_person` (default): Bulleted list grouped by owner. Each owner is a top-level **bold** bullet, their tasks are sub-bullets. Due dates appear inline in italics, e.g. *(by Wednesday)*. Shared tasks list all owners together, e.g. **Hyun / Matt / Ed**.
- `flat`: Flat checklist with assignee and due date on each line

### Step 5: Create Confluence Page

Use Atlassian MCP to create page:
- Cloud ID: from settings
- Space: from settings or specified space
- Parent Page: from settings or specified parent
- Content Format: markdown

## Note Generation Guidelines

### Summary Section
- Extract top 5 highlights as bullet points
- Focus on decisions, outcomes, and key discussions
- Keep each point concise (1-2 sentences)
- If `summary_format: paragraph`: Write a single cohesive prose paragraph instead

### Detailed Notes
- Group by topic from TLDV's topic detection
- Render each topic's notes as bullet points under the topic heading
- Include relevant quotes from transcript
- Preserve speaker attribution for important statements
- If `discussion_notes_format: prose`: Write as prose paragraphs instead

### Action Items Extraction
Look for:
- Explicit mentions of "action item", "to do", "follow up"
- Assignments: "[Person] will [task]"
- Deadlines mentioned
- Commitments made

Group items by owner as top-level **bold** bullets with task sub-bullets:
- Include due dates inline in italics: *(by Wednesday)*
- For shared tasks, combine owners: **Hyun / Matt / Ed**
- If `action_items_format: flat`: Use a flat checklist with assignee and due date instead

If no action items found, note: "No action items identified"

### Meeting Type Variations

Adjust note emphasis based on the type of meeting:

- **Standup/Daily Sync** - Shorter format, focus on blockers, progress updates, and quick decisions
- **Planning/Sprint Meeting** - Emphasize decisions made, items prioritized, and assignments
- **Client Call** - Emphasize client requests, commitments made, follow-up items, and timeline discussions
- **1:1 Meeting** - Focus on discussion topics, feedback given/received, career/growth items, and action items for both parties

## Default Configuration

| Setting | Default Value |
|---------|---------------|
| Timezone | `America/New_York` |
| Days lookback | 1 (today only) |
| Only participated | true |
| Content format | markdown |
| Sections | all enabled |
| Footer | `*Generated automatically from TLDV recording*` |
| MCP server | `atlassian` |
| duration_rounding | `ceil_15m` (round up to nearest 15 min) |
| meeting_details_format | standard |
| summary_format | bullets |
| discussion_notes_format | `bulleted` |
| action_items_format | `grouped_by_person` |

## Error Handling

- **No settings file**: Prompt user for required values, offer to create file
- **No meetings found**: Report "No meetings found for the specified period"
- **Missing transcript**: Create page with available data, note transcript unavailable
- **Missing highlights**: Generate summary from transcript if possible
- **Confluence error**: Report error, offer to save notes locally as markdown

## Template Overrides

Users can customize templates by placing override files in their settings directory. Before using a built-in template, check for overrides in this order:

1. `.claude/tldv-notes-templates/` (project-local overrides)
2. `~/.claude/tldv-notes-templates/` (user-global overrides)
3. Built-in `${CLAUDE_SKILL_DIR}/templates/` directory (defaults, shipped with plugin)

Override files use the same filenames as the built-in references. Only the files present in the override directory are replaced — missing files fall back to the built-in defaults.

| Override file | What it controls |
|---|---|
| `page-layout.md` | Overall page structure and section order |
| `section-formats.md` | Format variants for each section (header, summary, discussion, action items, etc.) |
| `empty-states.md` | Fallback content when data is unavailable |

## Reference Files

- **`${CLAUDE_SKILL_DIR}/templates/page-layout.md`** - Overall page structure template
- **`${CLAUDE_SKILL_DIR}/templates/section-formats.md`** - Section format variants controlled by settings
- **`${CLAUDE_SKILL_DIR}/templates/empty-states.md`** - Empty state fallback messages
