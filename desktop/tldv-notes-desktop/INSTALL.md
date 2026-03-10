# Installation

## Prerequisites

1. A [Claude.ai Teams](https://claude.ai) account with **admin access**
2. **Skills** enabled in Organization settings (Settings > Features)
3. **TLDV connector** connected (Organization settings > Connectors)
4. **Atlassian connector** connected (Organization settings > Connectors)

## Upload the Skill

### Step 1: Create the Zip

From the repository root:

```bash
cd desktop/tldv-notes-desktop
zip -r tldv-meeting-notes.zip tldv-meeting-notes/
```

Verify the structure:

```bash
unzip -l tldv-meeting-notes.zip
```

You should see:

```
tldv-meeting-notes/
tldv-meeting-notes/SKILL.md
```

### Step 2: Upload via Admin Settings

1. Go to [claude.ai](https://claude.ai) and sign in with an admin account
2. Open **Organization settings** (gear icon > Organization)
3. Navigate to **Skills**
4. Click **"+ Add"**
5. Upload `tldv-meeting-notes.zip`
6. Set availability to **"Enabled by default"** (recommended) or "Available to enable"
7. Click **Save**

The skill immediately appears for all organization members.

### Step 3: Verify Connectors

Ensure both connectors are available to your organization:

1. In Organization settings, go to **Connectors**
2. Confirm **TLDV** is connected
3. Confirm **Atlassian** is connected

Team members may need to individually authorize their Atlassian and TLDV accounts on first use.

## Usage

Team members don't need to install anything. They just open a new chat and ask:

> "Create meeting notes from today's calls"

On first use, Claude will help the user discover their Confluence configuration (Cloud ID, Space ID, Parent Page ID) interactively using the Atlassian connector.

### Example Prompts

- "Create meeting notes from today's calls"
- "Process my TLDV meetings from the last 3 days"
- "Preview my meeting notes without publishing" (dry run)
- "Generate notes for meeting abc123"
- "Summarize this week's meetings to Confluence"

## Updating the Skill

To update the skill with new instructions:

1. Edit `tldv-meeting-notes/SKILL.md`
2. Re-zip: `zip -r tldv-meeting-notes.zip tldv-meeting-notes/`
3. In Organization settings > Skills, remove the old version
4. Upload the new zip

## Troubleshooting

### Skill not appearing for team members

- Verify the skill is set to "Enabled by default" (not "Available to enable")
- If set to "Available to enable", team members need to go to Customize > Skills and enable it manually

### Connector errors

- Each team member needs to authorize their own TLDV and Atlassian accounts
- Check that both connectors are enabled at the organization level

### Configuration values unknown

- This is normal on first use — the skill guides users through interactive discovery of their Cloud ID, Space ID, and Parent Page ID using the Atlassian connector
