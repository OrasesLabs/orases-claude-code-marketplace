# TLDV Notes Plugin

Create Confluence pages from TLDV meeting recordings.
Processes your meetings and generates structured notes with summaries, discussion topics, and action items.

## Features

- Fetches meetings from TLDV where you participated
- Extracts transcripts and AI-generated highlights
- Generates structured Confluence pages with configurable sections
- Supports per-user and per-project configuration
- Customizable note sections (header, attendees, summary, discussion, action items)
- Configurable timezone, footer text, and Confluence targets
- Dry run mode for previewing notes before publishing

## Prerequisites

- TLDV MCP server configured in Claude Code
- Atlassian MCP server configured for Confluence access

## Usage

### Slash Command

```
/tldv-notes:meeting-notes
```

### With Options

```
/tldv-notes:meeting-notes days:7
/tldv-notes:meeting-notes dryrun:true
/tldv-notes:meeting-notes meetingid:abc123
/tldv-notes:meeting-notes days:3 space:TEAM dryrun:true
```

### Natural Language

- "Create meeting notes from today's calls"
- "Process my TLDV meetings"
- "Summarize my meetings to Confluence"

## Configuration

Create a settings file for persistent configuration.

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
```

**`.claude/tldv-notes.md`** (project-scoped, can be committed) uses the same format for shared team defaults.

If no settings file exists, the plugin will prompt for required values interactively.

## Options

| Option | Description | Default |
|--------|-------------|---------|
| `days:N` | Number of days to look back | 1 |
| `space:KEY` | Confluence space key | From settings |
| `parentid:ID` | Parent page ID | From settings |
| `dryrun:true` | Preview without creating pages | false |
| `meetingid:ID` | Process specific meeting only | - |

## Components

| Component | Name | Description |
|-----------|------|-------------|
| Skill | `tldv-notes:tldv-processor` | Core processing workflow and note generation |
| Command | `/tldv-notes:meeting-notes` | Slash command entry point |

## Author

Created by **Hyun Masiello** (hyun@orases.com) at [Orases](https://orases.com).
