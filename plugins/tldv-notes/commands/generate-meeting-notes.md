---
name: tldv-notes:generate-meeting-notes
description: Create Confluence pages from TLDV meeting recordings
argument-hint: days:N space:KEY dryrun:true meetingid:ID
---

# TLDV Meeting Notes Generator

Process TLDV meetings and create Confluence pages with structured notes using the **tldv-notes:tldv-processor** skill.

## Arguments

Arguments are passed as plain text after the command. Parse `$ARGUMENTS` to extract options.

**Supported formats:**
- `/generate-meeting-notes` - Process today's meetings
- `/generate-meeting-notes days:7` - Process last 7 days
- `/generate-meeting-notes dryrun:true` - Preview without creating pages
- `/generate-meeting-notes meetingid:abc123` - Process specific meeting
- `/generate-meeting-notes parentid:12345` - Create under specific parent page
- `/generate-meeting-notes days:3 space:TEAM dryrun:true` - Combined options

## Instructions

### Step 1: Parse Arguments

Parse `$ARGUMENTS` string to extract options:
- `days:N` - Number of days to look back (default: 1)
- `space:KEY` - Confluence space key (overrides settings file)
- `parentid:ID` - Parent page ID (overrides settings file)
- `dryrun:true` - Preview mode, don't create pages
- `meetingid:ID` - Process specific meeting only

Command-line arguments override settings file values.

**Arguments received:** $ARGUMENTS

### Step 2: Execute the Skill

Invoke the **tldv-notes:tldv-processor** skill, passing along the parsed arguments.

The skill handles:
- Loading configuration from settings files
- Fetching meetings from TLDV
- Gathering transcripts and highlights
- Generating structured notes
- Creating the Confluence page (or previewing in dry run mode)

### Step 3: Report Results

For each meeting processed, report:
- Meeting title
- Date/time (in configured timezone)
- Page URL (if created) or "[DRY RUN]" indicator
- Any errors encountered
