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

1. `.claude/tldv-notes.local.md` - User-local settings (not committed)
2. `.claude/tldv-notes.md` - Project-scoped settings (can be committed)

Parse YAML frontmatter for: `cloud_id`, `space_id`, `parent_page_id`, `timezone`, `sections`, `footer`, `mcp_server`, `duration_rounding`, `meeting_details_format`, `summary_format`, `discussion_notes_format`, `action_items_format`.

If no settings file exists, ask the user for the required values and offer to save them. When prompting interactively, use friendly names and provide clear options — not raw setting keys. For example:

| Setting key | Friendly prompt | Options / Help |
|---|---|---|
| `cloud_id` | "What is your Atlassian Cloud ID?" | Help the user find it: use Atlassian MCP tools like `getAccessibleAtlassianResources` to list their available cloud instances, or direct them to `https://admin.atlassian.com` → select their org → the Cloud ID is in the URL. |
| `space_id` | "Which Confluence Space should notes go to?" | Use `getConfluenceSpaces` to list available spaces and let the user pick one. Show space name and key. |
| `parent_page_id` | "What is the parent page ID for meeting notes?" | Help the user navigate: use `searchConfluenceUsingCql` to find pages in their chosen space, or ask them to paste the URL of the parent page and extract the ID from it. |
| `duration_rounding` | "How should meeting duration be displayed?" | "Exact duration" / "Rounded up to nearest 15 minutes" |
| `meeting_details_format` | "How should meeting details be laid out?" | "Standard format" / "Listed on separate lines" |
| `summary_format` | "How should the summary be written?" | "Bullet points" / "Single paragraph" |
| `discussion_notes_format` | "How should discussion notes be formatted?" | "Prose paragraphs" / "Bullet points" |
| `action_items_format` | "How should action items be organized?" | "Flat checklist" / "Grouped by person" |

Store the user's choices using the setting key names (e.g. `action_items_format: grouped_by_person`).

## MCP Tools Required

### TLDV MCP Server
- `mcp__tldv__list-meetings` - List meetings (use `onlyParticipated: true`)
- `mcp__tldv__get-meeting-metadata` - Get meeting details
- `mcp__tldv__get-transcript` - Get full transcript
- `mcp__tldv__get-highlights` - Get AI-generated highlights

### Atlassian MCP Server
- `mcp__atlassian__createConfluencePage` - Create the notes page
- `mcp__atlassian__getConfluenceSpaces` - Find target space

The MCP server prefix (`atlassian`) can be overridden via the `mcp_server` setting.

## Workflow

### Step 1: Load Configuration

Read settings file and extract configuration values.
Fall back to interactive prompts if required values are missing.

### Step 2: Fetch Meetings

Retrieve recent meetings where user participated:

```
mcp__tldv__list-meetings with:
- onlyParticipated: true
- Filter by date range as needed
```

### Step 3: For Each Meeting, Gather Data

1. Get metadata: title, date, attendees, recording URL
2. Get transcript: speaker-attributed conversation
3. Get highlights: AI-extracted key points and topics

### Step 4: Generate Structured Notes

Create markdown using only the enabled sections from configuration.

Available sections:
1. **header** - Meeting title and date
2. **meeting_link** - Link to TLDV recording
3. **attendees** - List of participants (organizer noted)
4. **summary** - 3-5 highlights (format controlled by `summary_format`)
5. **discussion_notes** - Detailed notes grouped by topic (format controlled by `discussion_notes_format`)
6. **action_items** - Extracted tasks and follow-ups (format controlled by `action_items_format`)
7. **footer** - Configurable footer text

If the settings file has a markdown body, append it as "Custom Notes".

### Format Settings

These settings control how each section is rendered. When absent, the default format is used.

#### `duration_rounding: ceil_15m`
Round meeting duration up to the nearest 15-minute increment.
- 28 min → 30 min, 42 min → 45 min, 31 min → 45 min, 60 min → 60 min
- Default: no rounding (exact duration)

#### `meeting_details_format: listed`
Render meeting details (date, time, duration, organizer, recording link) as inline bold-labeled fields on separate lines instead of a table. Attendees move to their own `## Attendees` section as a bulleted list with the organizer in **bold**.
- Default: standard header + separate attendees section

#### `summary_format: paragraph`
Write the summary as a single cohesive prose paragraph instead of bullet points.
- Default: bullet points

#### `discussion_notes_format: bulleted`
Render discussion notes under each topic heading as bullet points instead of prose paragraphs.
- Default: prose paragraphs

#### `action_items_format: grouped_by_person`
Replace the action items table/checklist with a bulleted list grouped by owner:
- Each owner is a top-level **bold** bullet
- Their tasks are sub-bullets
- Due dates appear inline in italics, e.g. *(by Wednesday)*
- Shared tasks list all owners together, e.g. **Hyun / Matt / Ed**
- Default: flat checklist with assignee and due date

### Step 5: Create Confluence Page

Use Atlassian MCP to create page:
- Cloud ID: from settings
- Space: from settings or specified space
- Parent Page: from settings or specified parent
- Content Format: markdown

## Note Generation Guidelines

### Summary Section
- If `summary_format: paragraph`: Write a single cohesive prose paragraph synthesizing the top highlights
- Default: Extract top 5 highlights as bullet points
- Focus on decisions, outcomes, and key discussions
- Keep each point concise (1-2 sentences)

### Detailed Notes
- Group by topic from TLDV's topic detection
- If `discussion_notes_format: bulleted`: Render each topic's notes as bullet points
- Default: Write as prose paragraphs
- Include relevant quotes from transcript
- Preserve speaker attribution for important statements

### Action Items Extraction
Look for:
- Explicit mentions of "action item", "to do", "follow up"
- Assignments: "[Person] will [task]"
- Deadlines mentioned
- Commitments made

If `action_items_format: grouped_by_person`:
- Group items by owner as top-level **bold** bullets with task sub-bullets
- Include due dates inline in italics: *(by Wednesday)*
- For shared tasks, combine owners: **Hyun / Matt / Ed**

Default: flat checklist with assignee and due date.

If no action items found, note: "No action items identified"

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
| duration_rounding | none (exact duration) |
| meeting_details_format | standard |
| summary_format | bullets |
| discussion_notes_format | prose |
| action_items_format | flat checklist |

## Error Handling

- **No settings file**: Prompt user for required values, offer to create file
- **No meetings found**: Report "No meetings found for the specified period"
- **Missing transcript**: Create page with available data, note transcript unavailable
- **Missing highlights**: Generate summary from transcript if possible
- **Confluence error**: Report error, offer to save notes locally as markdown

## Additional Resources

### Reference Files
- **`references/confluence-templates.md`** - Markdown templates for different meeting types
