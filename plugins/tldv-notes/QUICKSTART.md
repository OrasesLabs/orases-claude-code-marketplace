# Quick Start

Get meeting notes published to Confluence in under 5 minutes.

## 1. Configure Your Settings

Create `.claude/tldv-notes.local.md` in your project:

```markdown
---
cloud_id: "your-atlassian-cloud-id"
space_id: "your-confluence-space-id"
parent_page_id: "your-parent-page-id"
timezone: "America/New_York"
---
```

Or skip this step — the plugin will prompt you for these values on first run.

## 2. Run the Command

```
/tldv-notes:meeting-notes
```

Or with options:

```
/tldv-notes:meeting-notes days:3
```

## 3. Follow the Workflow

The plugin will:

1. Fetch your recent TLDV meetings
2. Extract transcripts and highlights
3. Generate structured notes
4. Create a Confluence page (or preview in dry run mode)
5. Report results with page URLs

## Tips

- Use `dryrun:true` to preview notes before publishing
- Use `meetingid:ID` to process a single specific meeting
- The `.local.md` settings file is per-user and should be gitignored
- Use `.claude/tldv-notes.md` (without `.local`) to share team defaults
- Customize which sections appear by editing the `sections` list in your settings
