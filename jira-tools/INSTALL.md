# Installation Guide

Complete installation and configuration guide for the Jira Tools Plugin.

## Prerequisites

- **Claude Code** installed (>=1.0.0)
- **Python 3.6+** (for Jira API scripts)
- **Access to Atlassian Jira** instance (yoursite.atlassian.net)
- **Git** (for cloning from private repository)

## Installation Methods

### Method 1: Git Repository Installation (Recommended)

Since this is a private repository, you'll need proper authentication:

```bash
# Ensure you have access to the OrasesLabs organization
# Install directly from GitHub
claude plugin install git@github.com:OrasesLabs/orases-claude-code-marketplace.git
```

### Method 2: Local Installation (Development)

```bash
# Clone the repository
git clone git@github.com:OrasesLabs/orases-claude-code-marketplace.git
cd orases-claude-code-marketplace/jira-tools

# Install the plugin locally
claude plugin install .
```

## Configuration

### Step 1: Set Atlassian Hostname

Add to `~/.claude/CLAUDE.md`:

```markdown
- All Atlassian resources are found at the hostname `yoursite.atlassian.net`
```

### Step 2: Configure API Authentication

For Jira ticket transitions and API operations, you need API token authentication.

#### Generate API Token

1. Visit: https://id.atlassian.com/manage-profile/security/api-tokens
2. Click "Create API token"
3. Name it: `Claude Code Jira Plugin`
4. Set expiration: 365 days (maximum)
5. Copy the token (shown only once!)

#### Set Environment Variables

Add to `~/.bashrc` or `~/.zshrc`:

```bash
export ATLASSIAN_EMAIL="your.email@company.com"
export ATLASSIAN_API_TOKEN="ATATT..."
export ATLASSIAN_SITE="yoursite.atlassian.net"
```

Reload your shell:
```bash
source ~/.bashrc  # or source ~/.zshrc
```

**Security Note:** Never commit API tokens to git! They're excluded via `.gitignore`.

## Verification

### Test API Authentication

```bash
python3 scripts/test_connection.py
```

Expected output:
```
✅ Connection Successful!

User: Your Name
Email: your.email@company.com
Active: True
```

### Test Skills

Start Claude Code and ask:
```
"Show me ticket PROJ-123"
"What transitions are available for PROJ-123?"
```

## Troubleshooting

### Plugin Not Found

**Problem:** `claude plugin install` fails

**Solution:**
- Verify you have access to OrasesLabs organization on GitHub
- Check SSH key is configured: `ssh -T git@github.com`
- Try absolute path for local installation
- Check `.claude-plugin/plugin.json` exists and is valid

### Skills Not Loading

**Problem:** Skills don't appear to work

**Solution:**
- Restart Claude Code
- Verify `skills/*/SKILL.md` files have valid YAML frontmatter
- Check skill descriptions include trigger terms
- Run `claude --debug` to see skill loading messages

### API Authentication Failures (401)

**Problem:** Scripts return 401 Unauthorized

**Solution:**
- Regenerate API token (may have expired)
- Verify `ATLASSIAN_EMAIL` matches token owner
- Check environment variables are set: `echo $ATLASSIAN_API_TOKEN`
- Test with curl:
  ```bash
  curl -u "$ATLASSIAN_EMAIL:$ATLASSIAN_API_TOKEN" \
    https://$ATLASSIAN_SITE/rest/api/3/myself
  ```

### Permission Errors (403)

**Problem:** "You don't have permission"

**Solution:**
- Check Jira project permissions
- Contact Jira admin for "Browse Project" access
- Verify you can access the ticket in your browser

### Python Not Found

**Problem:** `python3: command not found`

**Solution:**
- Install Python 3.6+
- On Windows WSL: `sudo apt install python3`
- On macOS: `brew install python3`
- Verify: `python3 --version`

## Uninstallation

```bash
# Remove the plugin
claude plugin uninstall jira-tools

# Remove environment variables (edit ~/.bashrc or ~/.zshrc)
# Remove API token from Atlassian (optional)
```

## Next Steps

- Review **README.md** for plugin overview
- Read **QUICKSTART.md** for usage examples
- Explore **scripts/README.md** for script documentation
- See **skills/jira/docs/** for skill-specific guides

## Support

- **Documentation:** See README.md and QUICKSTART.md
- **Issues:** https://github.com/OrasesLabs/orases-claude-code-marketplace/issues
- **Script Help:** See scripts/README.md and scripts/SETUP.md
- **Troubleshooting:** See skills/jira/docs/
