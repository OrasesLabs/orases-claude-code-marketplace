---
name: work-summary:generate-work-summary
description: "Generate work summary from git changes and post to Jira"
argument-hint: "[ABC-123]"
---

<task>
Generate a work summary from git changes and post to Jira as a structured comment.
</task>

Load the `work-summary:work-summary-generator` skill, then execute the workflow defined within it. The
skill contains all steps, templates, and error handling guidance. Reference files should be
loaded as directed by the skill.

Target ticket: $ARGUMENTS

If no arguments provided, the skill will extract the ticket from the current
git branch name or ask for identification.
