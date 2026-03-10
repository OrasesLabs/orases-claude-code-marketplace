# Installation

## Option A: Claude.ai Teams (Web)

### Step 1: Create a Project

1. Go to [claude.ai](https://claude.ai) and sign in to your Teams account
2. Click **Projects** in the sidebar
3. Click **Create Project**
4. Name it something like "TLDV Meeting Notes"

### Step 2: Add Custom Instructions

1. Open your new project's settings
2. Find the **Custom Instructions** field
3. Copy the entire contents of [`custom-instructions.txt`](custom-instructions.txt) and paste it in
4. Save

### Step 3: Upload Project Knowledge

1. In the project settings, find **Project Knowledge**
2. Click **Add content** → **Upload files**
3. Upload `project-knowledge/tldv-meeting-notes-processor.md`

### Step 4: Configure Your Confluence Details

1. After uploading, click on the knowledge file to edit it
2. Find the **Configuration** section at the top
3. Replace the placeholder values:

```yaml
cloud_id: "your-actual-cloud-id"
space_id: "your-actual-space-id"
parent_page_id: "your-actual-parent-page-id"
timezone: "America/New_York"
```

**Don't know your Cloud ID?** No problem — skip this step. On first use, Claude will use the Atlassian integration to help you discover these values interactively.

### Step 5: Connect Integrations

#### Atlassian (Built-in)

1. In the project, click the **Integrations** panel (or the plug icon)
2. Find **Atlassian** in the list of available integrations
3. Click **Connect** and authorize access to your Atlassian account
4. Ensure Confluence access is granted

#### TLDV (Custom MCP)

The TLDV integration needs to be added as a custom MCP server. Contact your team admin or check TLDV's documentation for their MCP server endpoint details.

1. In your organization's admin settings, add TLDV as a custom integration
2. Configure the MCP server URL provided by TLDV
3. Enable it for your project

### Step 6: Test It

Start a new conversation in the project and say:

> "Preview my meeting notes from today"

Claude will fetch your TLDV meetings and show you a dry-run preview without creating any Confluence pages.

---

## Option B: Claude Desktop App

### Step 1: Configure MCP Servers

Edit your Claude Desktop configuration file:

- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

Add the TLDV MCP server to your configuration. Example structure:

```json
{
  "mcpServers": {
    "tldv": {
      "command": "npx",
      "args": ["-y", "@tldv/mcp-server"]
    }
  }
}
```

> **Note:** The exact TLDV MCP server package name and configuration may vary. Check TLDV's documentation for current setup instructions.

The Atlassian integration is available as a built-in integration in Claude Desktop — connect it through the app's integration settings.

### Step 2: Create a Project

1. Open Claude Desktop
2. Create a new Project
3. Follow Steps 2–4 from Option A above (custom instructions + project knowledge + configuration)

### Step 3: Test It

Open a conversation in the project and ask:

> "Create meeting notes from today's calls"

---

## Finding Your Confluence Details

### Cloud ID

Option 1 (Recommended): Just ask Claude — it will call `getAccessibleAtlassianResources` to list your available cloud instances.

Option 2: Go to `https://admin.atlassian.com`, select your organization. The Cloud ID appears in the URL.

### Space ID

Ask Claude to list your Confluence spaces. It will call `getConfluenceSpaces` and show you the available spaces with their names and IDs.

### Parent Page ID

This is the Confluence page under which meeting notes will be created. Find it by:

1. Asking Claude to search for pages in your space
2. Navigating to the page in Confluence and checking the URL (the ID is in the path)
3. Creating a new "Meeting Notes" page in Confluence and using its ID

## Customizing Format Settings

To change how notes are formatted, edit the **Format Settings** table in the project knowledge document. Available options:

| Setting | Options |
|---------|---------|
| Duration rounding | `ceil_15m` (default) or `exact` |
| Meeting details | `standard` (default) or `listed` |
| Summary style | `bullets` (default) or `paragraph` |
| Discussion notes | `bulleted` (default) or `prose` |
| Action items | `grouped_by_person` (default) or `flat` |
