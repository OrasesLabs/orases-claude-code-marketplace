# Quick Start

Get meeting notes published to Confluence in under 5 minutes.

## 1. Set Up the Project

In Claude.ai Teams:
1. Create a new **Project** called "TLDV Meeting Notes"
2. Paste [`custom-instructions.txt`](custom-instructions.txt) into Custom Instructions
3. Upload [`project-knowledge/tldv-meeting-notes-processor.md`](project-knowledge/tldv-meeting-notes-processor.md) as project knowledge
4. Connect the **Atlassian** and **TLDV** integrations

## 2. Configure (Optional)

Edit the project knowledge file and replace the placeholder values with your Confluence details:

```yaml
cloud_id: "your-cloud-id"
space_id: "your-space-id"
parent_page_id: "your-parent-page-id"
```

Or skip this — Claude will help you find these values on first use.

## 3. Create Notes

Start a conversation and say:

> "Create meeting notes from today's calls"

Other things you can say:

- "Process my meetings from the last 3 days"
- "Preview my meeting notes without publishing"
- "Generate notes for meeting abc123"

## 4. What You Get

Claude will:
1. Fetch your recent TLDV meetings
2. Extract transcripts and highlights
3. Generate structured notes with summary, discussion topics, and action items
4. Create a Confluence page (or preview in dry run mode)
5. Report results with page URLs

## Tips

- Say "preview" or "dry run" to see notes without publishing
- Say "last 7 days" to process a week's worth of meetings
- Reference a specific meeting ID to process just one meeting
- Edit the project knowledge to change formatting preferences
