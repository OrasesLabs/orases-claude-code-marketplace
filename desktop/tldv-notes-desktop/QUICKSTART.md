# Quick Start

Get the TLDV Meeting Notes skill deployed to your team in under 5 minutes.

## 1. Zip the Skill

```bash
cd desktop/tldv-notes-desktop
zip -r tldv-meeting-notes.zip tldv-meeting-notes/
```

## 2. Upload

1. Go to **Organization settings > Skills** on [claude.ai](https://claude.ai)
2. Click **"+ Add"**
3. Upload `tldv-meeting-notes.zip`
4. Set to **"Enabled by default"**

## 3. Use It

Open a new chat and say:

> "Create meeting notes from today's calls"

Other things you can say:

- "Process my meetings from the last 3 days"
- "Preview my meeting notes without publishing"
- "Generate notes for meeting abc123"

## What Happens

Claude will:
1. Fetch your recent TLDV meetings
2. Extract transcripts and highlights
3. Generate structured notes with summary, discussion topics, and action items
4. Create a Confluence page (or preview in dry run mode)
5. Report results with page URLs

## Tips

- Say "preview" or "dry run" to see notes without publishing
- Say "last 7 days" to process a week's worth of meetings
- Reference a specific meeting ID to process just one
- On first use, Claude will help you find your Confluence configuration values
