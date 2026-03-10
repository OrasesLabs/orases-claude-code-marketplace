# Quick Start

Get a work summary posted to Jira in under 5 minutes.

## 1. Check Out a Feature Branch

```bash
git checkout meckert/abc-123-my-feature
```

## 2. Run the Command

```
/work-summary:work-summary ABC-123
```

Or omit the ticket key to auto-detect from the branch name:

```
/work-summary:work-summary
```

## 3. Follow the Prompts

The workflow will:

1. Confirm the Jira ticket with you
2. Analyze your git changes
3. Generate client-friendly and technical summaries
4. Ask you to review before posting
5. Post to Jira and save a local copy

## Tips

- Run from any feature branch -- the plugin detects the base branch (`review` or `main`) automatically
- QA steps are derived from actual code changes, not guessed
- You can edit the summary before posting
- Local copies are saved to `.claude/work-summaries/` for reference
