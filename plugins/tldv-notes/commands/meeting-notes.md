---
name: meeting-notes
description: Create Confluence pages from TLDV meeting recordings
argument-hint: days:N space:KEY dryrun:true meetingid:ID
---

# TLDV Meeting Notes Generator

Process TLDV meetings and create Confluence pages with structured notes.

## Arguments

Arguments are passed as plain text after the command. Parse `$ARGUMENTS` to extract options.

**Supported formats:**
- `/meeting-notes` - Process today's meetings
- `/meeting-notes days:7` - Process last 7 days
- `/meeting-notes dryrun:true` - Preview without creating pages
- `/meeting-notes meetingid:abc123` - Process specific meeting
- `/meeting-notes parentid:12345` - Create under specific parent page
- `/meeting-notes days:3 space:TEAM dryrun:true` - Combined options

## Instructions

### Step 1: Load Configuration

Check for settings files in this priority order (first found wins):
1. `.claude/tldv-notes.local.md` (user-local, not committed)
2. `.claude/tldv-notes.md` (project-scoped, can be committed)

If a settings file is found, parse the YAML frontmatter to extract configuration.
If no settings file exists, inform the user they can create one for persistent configuration (see **Configuration** section below), then ask for the required values interactively.

**Required settings (must come from file or user input):**
- `cloud_id` - Atlassian Cloud ID
- `space_id` - Confluence Space ID
- `parent_page_id` - Default parent page ID for notes

**Optional settings with defaults:**
- `timezone` - Display timezone (default: `America/New_York`)
- `sections` - Note sections to include (default: all)
- `footer` - Custom footer text (default: `*Generated automatically from TLDV recording*`)
- `mcp_server` - MCP server prefix for Atlassian tools (default: `atlassian`)

### Step 2: Parse Arguments

Parse `$ARGUMENTS` string to extract options:
- `days:N` - Number of days to look back (default: 1)
- `space:KEY` - Confluence space key (overrides settings file)
- `parentid:ID` - Parent page ID (overrides settings file)
- `dryrun:true` - Preview mode, don't create pages
- `meetingid:ID` - Process specific meeting only

Command-line arguments override settings file values.

**Arguments received:** $ARGUMENTS

### Step 3: Fetch Meetings from TLDV

If a specific meeting ID was provided:
- Fetch only that meeting's data

Otherwise:
- Use `mcp__tldv__list-meetings` with `onlyParticipated: true`
- Filter to meetings within the specified day range

Report how many meetings were found.

### Step 4: For Each Meeting

Gather meeting data:
1. **Metadata**: Use `mcp__tldv__get-meeting-metadata` for title, date, attendees, URL
   - **Duration**: Round up to the next 15-minute increment (e.g., 21m -> 30m, 44m -> 45m, 62m -> 1h 15m, 45m -> 45m)
   - **Timezone**: Convert all meeting times from UTC to the configured timezone. Display as "h:mm AM/PM TZ".
2. **Transcript**: Use `mcp__tldv__get-transcript` for full conversation
3. **Highlights**: Use `mcp__tldv__get-highlights` for AI-extracted key points

### Step 5: Generate Notes

Generate notes using only the sections enabled in configuration.
Default sections (all enabled unless overridden):

1. **header** - Meeting title, date, and duration (rounded to next 15m increment). Display meeting time in configured timezone.
2. **meeting_link** - TLDV recording URL
3. **attendees** - List participants, mark organizer
4. **summary** - Top 3-5 highlights as bullets
5. **discussion_notes** - Group by topic from highlights
6. **action_items** - Extract from transcript/highlights
   - Include due dates if mentioned in the discussion
   - Format: "- [Action item] (Due: [date])" or "- [Action item]" if no due date mentioned
7. **footer** - Configurable footer text

If the settings file contains a markdown body (content after the frontmatter), append it as an additional "Custom Notes" section at the end.

See `references/confluence-templates.md` for formatting templates.

### Step 6: Create Confluence Page

Determine the correct MCP tool prefix from configuration (`mcp_server` setting, default: `atlassian`).

If NOT in dry run mode:
- Use `mcp__atlassian__createConfluencePage` (or configured MCP server)
- Cloud ID: from settings
- Space ID: from settings (or `space:KEY` argument)
- Parent ID: from `parentid` argument, or settings `parent_page_id`
- Title: "{Meeting Title} - {Date}"
- Content: Generated markdown notes
- Format: markdown

If in dry run mode:
- Display the generated notes
- Show what page would be created
- Do NOT call the Confluence API

### Step 7: Report Results

For each meeting processed, report:
- Meeting title
- Date/time (in configured timezone)
- Page URL (if created) or "[DRY RUN]" indicator
- Any errors encountered

## Configuration

Users can create a settings file for persistent configuration.

**`.claude/tldv-notes.local.md`** (user-local, gitignored):
```markdown
---
cloud_id: "your-cloud-id"
space_id: "your-space-id"
parent_page_id: "your-parent-page-id"
timezone: "America/New_York"
mcp_server: "atlassian"
sections:
  - header
  - meeting_link
  - attendees
  - summary
  - discussion_notes
  - action_items
  - footer
footer: "*Generated automatically from TLDV recording*"
---

Any markdown content here will be appended as a "Custom Notes" section.
```

**`.claude/tldv-notes.md`** (project-scoped, can be committed):
Same format. Use this to share team defaults across a project.

## Error Handling

- If no settings file AND required values not provided: Prompt user, offer to create settings file
- If no TLDV MCP server configured: Inform user to configure TLDV MCP
- If no meetings found: Report "No meetings found for the specified period"
- If transcript unavailable: Create page with available data, note limitation
- If Confluence fails: Save notes locally and report error
