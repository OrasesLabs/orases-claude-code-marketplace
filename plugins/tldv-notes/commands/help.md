---
name: tldv-notes:help
description: Learn about the TLDV Notes plugin, configure settings, and customize templates
disable-model-invocation: true
---

# TLDV Notes Plugin — Help & Setup

Guide the user through understanding, configuring, and customizing the TLDV Notes plugin.

## Instructions

When the user runs this command, present a welcome overview and then ask what they'd like help with. Walk them through each topic interactively — don't dump everything at once.

### Step 1: Welcome Overview

Display this summary:

> **TLDV Notes Plugin** processes your TLDV meeting recordings and creates structured Confluence pages with summaries, discussion notes, and action items.
>
> **What it needs:**
> - A TLDV MCP server connection (for fetching meetings, transcripts, and highlights)
> - An Atlassian MCP server connection (for creating Confluence pages)
> - Your Atlassian Cloud ID, Confluence Space ID, and a parent page ID
>
> **Commands:**
> - `/tldv-notes:generate-meeting-notes` — Process meetings and create Confluence pages
> - `/tldv-notes:help` — This help guide

### Step 2: Ask What They Need

Use AskUserQuestion to ask:

**"What would you like help with?"**
- **Get started** — Set up the plugin for first use
- **Customize formatting** — Change how notes look (discussion style, action item layout, etc.)
- **Customize templates** — Override the page layout or section templates
- **View current settings** — Show what's currently configured

Then follow the appropriate path below.

---

## Path: Get Started

### Step A: Check MCP Servers

Verify that the required MCP servers are available:
1. Check for `mcp__tldv__list-meetings` — if unavailable, inform the user they need to configure a TLDV MCP server
2. Check for `mcp__atlassian__createConfluencePage` — if unavailable, inform the user they need to configure an Atlassian MCP server

If either is missing, explain what's needed and stop here.

### Step B: Check for Existing Settings

Look for settings files in priority order:
1. `.claude/tldv-notes.local.md`
2. `.claude/tldv-notes.md`
3. `~/.claude/tldv-notes.md`

If a settings file is found, show the user their current configuration and ask if they want to modify it. If none found, continue to Step C.

### Step C: Gather Required Settings

Walk the user through each required setting interactively:

1. **Cloud ID** — Use `getAccessibleAtlassianResources` (or equivalent Atlassian MCP tool) to list their available cloud instances. Let them pick one. If the tool isn't available, ask them to check `https://admin.atlassian.com` and find the Cloud ID in the URL.

2. **Space ID** — Use `getConfluenceSpaces` to list available spaces. Show space name and key, let the user pick.

3. **Parent Page ID** — Ask the user where meeting notes should be created. Help them find the page: use `searchConfluenceUsingCql` to search in their chosen space, or ask them to paste the URL of the parent page and extract the ID.

### Step D: Ask Where to Save

Use AskUserQuestion to ask:

**"Where should these settings be saved?"**
- **Project-local** (`.claude/tldv-notes.local.md`) — Only for you, in this project. Not committed to git.
- **Project-shared** (`.claude/tldv-notes.md`) — Shared with your team via git. Good for team defaults.
- **User-global** (`~/.claude/tldv-notes.md`) — Applies across all your projects. Good if you always use the same Confluence space.

### Step E: Write Settings File

Create the settings file at the chosen location with YAML frontmatter containing the gathered values. Use defaults for format settings — only include format overrides if the user explicitly changed them.

Example minimal settings file:
```markdown
---
cloud_id: "your-cloud-id"
space_id: "your-space-id"
parent_page_id: "your-parent-page-id"
---
```

Confirm success and suggest they try `/tldv-notes:generate-meeting-notes dryrun:true` to preview.

---

## Path: Customize Formatting

### Step A: Show Current Defaults

Display the current format settings (from settings file if it exists, otherwise the defaults):

| Setting | Current Value | Description |
|---|---|---|
| `duration_rounding` | `ceil_15m` | Round up to nearest 15 minutes |
| `meeting_details_format` | `standard` | Date/time/duration on one line |
| `summary_format` | `bullets` | Summary as bullet points |
| `discussion_notes_format` | `bulleted` | Discussion notes as bullet points |
| `action_items_format` | `grouped_by_person` | Action items grouped by owner |
| `timezone` | `America/New_York` | Display timezone |
| `footer` | `*Generated automatically from TLDV recording*` | Page footer text |

### Step B: Ask What to Change

Use AskUserQuestion to ask which settings they want to modify. For each setting they choose, present the available options using AskUserQuestion with clear descriptions.

Refer to the **tldv-notes:tldv-processor** skill's Format Settings section for the full list of options and their descriptions.

### Step C: Ask Where to Save

If a settings file already exists, ask:

**"Update your existing settings file, or save to a different location?"**
- **Update existing** (`{path to existing file}`)
- **Project-local** (`.claude/tldv-notes.local.md`)
- **Project-shared** (`.claude/tldv-notes.md`)
- **User-global** (`~/.claude/tldv-notes.md`)

If no settings file exists, ask the same location question from the Get Started path.

### Step D: Save Changes

Update or create the settings file with the new format values. Preserve any existing settings that weren't changed.

---

## Path: Customize Templates

### Step A: Explain Template System

Explain to the user:

> The plugin uses three template files that control how Confluence pages are generated:
>
> - **`page-layout.md`** — The overall page structure and section order
> - **`section-formats.md`** — How each section is rendered (header, summary, discussion notes, action items, etc.)
> - **`empty-states.md`** — Fallback content when data is unavailable (e.g., no transcript yet)
>
> You can override any of these by placing your own version in a templates directory. You only need to override the files you want to change — the rest fall back to the built-in defaults.

### Step B: Ask Where to Save Templates

Use AskUserQuestion to ask:

**"Where should your custom templates be stored?"**
- **Project-local** (`.claude/tldv-notes-templates/`) — Custom templates for this project only
- **User-global** (`~/.claude/tldv-notes-templates/`) — Custom templates across all projects

### Step C: Ask Which Templates to Customize

Use AskUserQuestion to ask which template files they want to override. For each selected file:

1. Read the built-in version from the plugin's `templates/` directory
2. Show the user the current content
3. Ask what they'd like to change
4. Write the customized version to the chosen override directory

---

## Path: View Current Settings

### Step A: Check All Locations

Read settings from all three locations (if they exist):
1. `.claude/tldv-notes.local.md` (project-local)
2. `.claude/tldv-notes.md` (project-shared)
3. `~/.claude/tldv-notes.md` (user-global)

### Step B: Show Effective Configuration

Display:
- Which settings files were found and their locations
- The effective (merged) configuration, noting where each value comes from
- Any template overrides found in `.claude/tldv-notes-templates/` or `~/.claude/tldv-notes-templates/`
- Which MCP servers are available (tldv, atlassian)

### Step C: Offer Next Steps

Ask if they'd like to modify any settings or customize templates, and route to the appropriate path above.
