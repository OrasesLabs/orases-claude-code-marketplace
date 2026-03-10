# TLDV Meeting Notes — Organization Skill

An **Organization Skill** for Claude.ai Teams that creates Confluence pages from TLDV meeting recordings. Upload once, available to all team members instantly.

This is the Claude.ai Teams companion to [tldv-notes](../../plugins/tldv-notes/) (Claude Code CLI plugin). Same meeting-notes workflow, packaged as an Organization Skill.

## Features

- Fetches meetings from TLDV where the user participated
- Extracts transcripts and AI-generated highlights
- Generates structured Confluence pages with configurable sections
- Customizable formatting (summary style, action item layout, duration rounding, etc.)
- Dry run mode for previewing notes before publishing
- Process specific meetings by ID or batch by date range
- Zero setup for team members — admin uploads once, everyone gets it

## How It Works

The skill is uploaded as a zip file by a Claude.ai Teams admin. Once uploaded, it automatically appears for all organization members. Team members just ask Claude naturally:

> "Create meeting notes from today's calls"

| Claude Code CLI | Claude.ai Organization Skill |
|-----------------|------------------------------|
| Plugin with skills + commands | Org-wide skill (zip upload) |
| `/tldv-notes:generate-meeting-notes` | "Create meeting notes from today's calls" |
| Settings in `.claude/tldv-notes.md` | Interactive configuration on first use |
| Local MCP servers | Organization connectors (TLDV + Atlassian) |

## Prerequisites

- [Claude.ai Teams](https://claude.ai) account with admin access (for upload)
- TLDV connector enabled in Organization settings
- Atlassian connector enabled in Organization settings

## Quick Start

**Admins:** See [INSTALL.md](INSTALL.md) to upload the skill.

**Team members:** Just open a new chat and say:
- "Create meeting notes from today's calls"
- "Preview my meeting notes without publishing"
- "Process my meetings from the last 7 days"

## Configurable Sections

- **Header** — Title, date, time, duration, recording link
- **Attendees** — Participant list with organizer highlighted
- **Summary** — Key highlights (bullets or paragraph)
- **Discussion Notes** — Topics with details (bullets or prose)
- **Action Items** — Tasks grouped by person or flat checklist
- **Footer** — Customizable footer text

## Skill Structure

```
tldv-meeting-notes/
└── SKILL.md
```

Zip and upload this folder. See [INSTALL.md](INSTALL.md) for details.

## Author

Created by **Hyun Masiello** (hyun@orases.com) at [Orases](https://orases.com).

## License

MIT — see [LICENSE](LICENSE).
