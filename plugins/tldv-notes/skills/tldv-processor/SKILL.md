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

Parse YAML frontmatter for: `cloud_id`, `space_id`, `parent_page_id`, `timezone`, `sections`, `footer`, `mcp_server`.

If no settings file exists, ask the user for required Confluence values (cloud_id, space_id, parent_page_id) and offer to save them.

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
4. **summary** - 3-5 bullet points from highlights
5. **discussion_notes** - Detailed notes grouped by topic
6. **action_items** - Extracted tasks and follow-ups
7. **footer** - Configurable footer text

If the settings file has a markdown body, append it as "Custom Notes".

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

### Detailed Notes
- Group by topic from TLDV's topic detection
- Include relevant quotes from transcript
- Preserve speaker attribution for important statements

### Action Items Extraction
Look for:
- Explicit mentions of "action item", "to do", "follow up"
- Assignments: "[Person] will [task]"
- Deadlines mentioned
- Commitments made

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

## Error Handling

- **No settings file**: Prompt user for required values, offer to create file
- **No meetings found**: Report "No meetings found for the specified period"
- **Missing transcript**: Create page with available data, note transcript unavailable
- **Missing highlights**: Generate summary from transcript if possible
- **Confluence error**: Report error, offer to save notes locally as markdown

## Additional Resources

### Reference Files
- **`references/confluence-templates.md`** - Markdown templates for different meeting types
