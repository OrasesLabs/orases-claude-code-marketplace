# TLDV Notes — Desktop

Create Confluence pages from TLDV meeting recordings using **Claude.ai Teams Projects** or the **Claude Desktop** application.

This is the desktop companion to [tldv-notes](../plugins/tldv-notes/) (Claude Code CLI plugin). Same meeting-notes workflow, adapted for Claude.ai's project-based interface.

## Features

- Fetches meetings from TLDV where you participated
- Extracts transcripts and AI-generated highlights
- Generates structured Confluence pages with configurable sections
- Customizable formatting (summary style, action item layout, duration rounding, etc.)
- Dry run mode for previewing notes before publishing
- Process specific meetings by ID or batch by date range

## How It Works

Instead of slash commands and a plugin system, the desktop version uses **Claude.ai Projects**:

| Claude Code CLI | Claude.ai Desktop |
|-----------------|-------------------|
| Plugin with skills + commands | Project knowledge files |
| `/tldv-notes:generate-meeting-notes` | "Create meeting notes from today's calls" |
| Settings in `.claude/tldv-notes.md` | Configuration in project knowledge document |
| `mcp__atlassian__*` tools | Built-in Atlassian integration |

## Prerequisites

- A [Claude.ai Teams](https://claude.ai) account (or Claude Desktop app)
- TLDV account with MCP server access
- Atlassian/Confluence account

## Quick Start

1. Create a new Project in Claude.ai
2. Paste `custom-instructions.txt` into the Project's custom instructions
3. Upload `project-knowledge/tldv-meeting-notes-processor.md` as project knowledge
4. Connect the **Atlassian** integration (built-in)
5. Connect the **TLDV** integration (custom MCP server)
6. Edit the configuration section in the project knowledge with your Confluence details
7. Start a conversation: "Create meeting notes from today's calls"

See [INSTALL.md](INSTALL.md) for detailed setup instructions.

## Usage

Just ask in natural language:

- "Create meeting notes from today's calls"
- "Process my TLDV meetings from the last 7 days"
- "Preview my meeting notes without publishing"
- "Generate notes for meeting abc123"
- "Summarize this week's meetings to Confluence"

## Configurable Sections

- **Header** — Title, date, time, duration, recording link
- **Attendees** — Participant list with organizer highlighted
- **Summary** — Key highlights (bullets or paragraph)
- **Discussion Notes** — Topics with details (bullets or prose)
- **Action Items** — Tasks grouped by person or flat checklist
- **Footer** — Customizable footer text

## Author

Created by **Hyun Masiello** (hyun@orases.com) at [Orases](https://orases.com).

## License

MIT — see [LICENSE](LICENSE).
