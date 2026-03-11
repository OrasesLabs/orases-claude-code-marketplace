# Error Handling

Handle these scenarios gracefully with clear recovery guidance.

## Ticket Access Issues

**Symptom**: Atlassian MCP tool returns authentication or permission errors.

**Recovery**:
1. Verify the ticket key format is correct (e.g., `ABC-123`)
2. Confirm the Atlassian MCP server is configured and accessible
3. Ask the user to verify their Atlassian credentials or MCP server status
4. If the ticket exists but is restricted, note this and offer to generate the summary
   without Jira posting (local-only mode)

## Empty Branch / No Commits

**Symptom**: `git log {BASE_BRANCH}...HEAD` returns no commits.

**Recovery**:
1. Verify the current branch is not the base branch itself
2. Confirm the base branch was detected correctly in Step 4
3. If truly no commits exist, inform the user and suggest checking the branch
4. Offer to compare against a different branch if the feature was based on another point

## Ambiguous Branch Name

**Symptom**: Cannot extract a ticket key from the branch name.

**Recovery**:
1. Display the current branch name to the user
2. Use `AskUserQuestion` to ask for the ticket identifier directly
3. Do not guess - always confirm with the user

## PR/Merge Request Not Found

**Symptom**: No pull request or merge request found for the current branch.

**Recovery**:
1. This is not an error — summaries can be posted without a PR/MR link
2. Note in the summary that no PR/MR is linked yet
3. Continue with the workflow; the PR/MR can be referenced in a follow-up comment

**CodeCommit-specific**: If using AWS CodeCommit, verify:
- The AWS CLI is installed and configured (`aws configure list`)
- The repository name is correct (check `git remote -v`)
- The `aws codecommit list-pull-requests` command has appropriate IAM permissions

**GitHub-specific**: If using GitHub, verify:
- The GitHub CLI (`gh`) is installed and authenticated
- The repository has a GitHub remote configured

## Jira Comment Posting Failure

**Symptom**: Failure when posting the comment to Jira.

**Recovery**:
1. Display the error message to the user
2. Offer to retry the post
3. If retry fails, save the summary locally (Step 10) so no work is lost
4. Suggest the user post the summary manually from the local file

## Large Diff / Many Files

**Symptom**: Branch has an unusually large number of changed files (50+).

**Recovery**:
1. Warn the user about the scope before generating summaries
2. Use `AskUserQuestion`: "This branch has {count} modified files. Generate full summary
   or focus on a specific area?"
3. If focused: filter git diff to the specified path prefix
4. Consider grouping minor changes (e.g., "15 template files updated for styling consistency")
   rather than listing every file individually

## MCP Tool Name Mismatch

**Symptom**: Atlassian MCP tool call fails because the tool name is not recognized.

**Recovery**:
1. MCP tool names vary depending on how the MCP server is configured
2. Check available Atlassian MCP tools by listing tools matching the `mcp_server` prefix
3. If the prefix is wrong, ask the user to update the `mcp_server` setting
4. Common prefixes: `claude_ai_Atlassian`, `atlassian`, `jira`
