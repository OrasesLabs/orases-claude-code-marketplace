---
name: work-summary:client-summary-generator
description: >-
  This skill should be used when the user asks to "generate a client summary",
  "create a client-friendly summary", "write QA steps from my changes",
  "summarize changes for stakeholders", or needs a non-technical summary of
  code changes with QA steps and testing checklists. Can be used standalone
  or as part of the work-summary workflow.
---

# Client-Friendly Summary Generator

Generate a client-friendly summary from code changes and Jira ticket context. This summary
targets non-technical stakeholders — project managers, QA teams, and clients. Every claim
must be grounded in actual code changes or ticket data.

## Prerequisites

This skill requires:
- Git change data (commit list, modified files, change statistics)
- Jira ticket context (description, comments, acceptance criteria) — optional but recommended

When invoked from the `work-summary:work-summary-generator` skill, these are provided from
earlier steps. When used standalone, gather them first.

## Configuration

Check for template overrides in settings. If a `client_summary_template` path is defined
in the work-summary settings file (`.claude/work-summary.local.md`, `.claude/work-summary.md`,
or `~/.claude/work-summary.md`), load that template instead of the built-in default.

## Process

### 1. Gather Context

If not already available from an earlier workflow step:
- Read the Jira ticket description and comments for acceptance criteria and scope decisions
- Gather git change data (`git diff`, `git log`) for the relevant branch

### 2. Analyze User-Facing Changes

1. Review the Jira ticket description and comments for acceptance criteria,
   scope decisions, and context added after ticket creation
2. Read modified controller and template files to understand user-facing behavior changes
3. If acceptance criteria exist, cross-reference each against actual code changes
4. Build QA steps only from verified, observable behavior changes
5. Flag any acceptance criteria that could not be mapped to code changes

### 3. Generate Summary Sections

Produce these sections (omit any that do not apply):

- **What Changed**: Business-level description of modifications
- **QA Steps**: Numbered validation steps derived from code inspection, not guessed
- **Related Tasks**: Links to related tickets from issue links and mentions in comments
- **Testing Checklist**: Acceptance criteria checkboxes, each verified against code

Refer to the template at `${CLAUDE_PLUGIN_ROOT}/skills/client-summary-generator/templates/client-summary-template.md`
for the complete Markdown structure. If a template override is configured in settings, use
that instead.

### 4. Review with User

After generating, display the QA Steps and Testing Checklist as plain text output so the user
can read them. Then ask via `AskUserQuestion`:
- Question: "Are these QA steps and testing items accurate?"
- Options: "Yes, looks good" / "Needs changes"
- If "Needs changes": await freeform feedback with corrections, then regenerate affected sections

## Guidelines

- Never assume or fabricate QA steps — derive only from actual code changes
- Use business-friendly language, avoid technical jargon
- Keep QA steps specific and actionable
- If acceptance criteria exist in the ticket, cross-reference every criterion
- Flag any acceptance criteria that have no corresponding code change
- Group related changes together for clarity

## Additional Resources

### Templates
- **`${CLAUDE_PLUGIN_ROOT}/skills/client-summary-generator/templates/client-summary-template.md`** - Default Markdown structure for the client-friendly summary
