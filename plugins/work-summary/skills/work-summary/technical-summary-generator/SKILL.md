---
name: work-summary:technical-summary-generator
description: >-
  This skill should be used when the user asks to "generate a technical summary",
  "create a developer summary", "summarize the architecture changes",
  "list modified files by category", or needs a developer-oriented summary of
  code changes with file categories, commits, and architecture notes. Can be
  used standalone or as part of the work-summary workflow.
---

# Technical Summary Generator

Generate a technical summary from git branch changes. This summary targets developers and
maintainers — architecture decisions, file categories, commit history, and code quality notes.

## Prerequisites

This skill requires:
- Git change data (commit list, modified files, change statistics)
- File categorization patterns (from settings or built-in defaults)

When invoked from the `work-summary:work-summary-generator` skill, these are provided from
earlier steps. When used standalone, gather them first.

## Configuration

Check for template overrides in settings. If a `technical_summary_template` path is defined
in the work-summary settings file (`.claude/work-summary.local.md`, `.claude/work-summary.md`,
or `~/.claude/work-summary.md`), load that template instead of the built-in default.

For file categorization patterns, check the `file_categories` setting. If not defined, load
defaults from `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/references/file-categories.md`.

## Process

### 1. Gather Context

If not already available from an earlier workflow step:
- Run `git log` and `git diff` commands to gather commit messages, modified files, and statistics
- Determine file categorization patterns from settings or defaults

### 2. Categorize Modified Files

Sort modified files into categories based on the configured patterns. Files not matching
any pattern are grouped under "Other". For each category, calculate:
- File count
- Total additions and deletions

### 3. Generate Summary Sections

Produce these sections (omit any that do not apply):

- **Architecture & Implementation**: Pattern changes, new abstractions, integration points
- **Modified Files**: Categorized list with per-category file counts and line change totals
- **Commits**: All commit hashes and messages from the branch
- **Testing Coverage**: Unit/integration test files added or modified
- **Code Quality**: Standards compliance, deprecations addressed
- **Performance Considerations**: Query changes, caching impact (only if applicable)

Refer to the template at `${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/technical-summary-template.md`
for the complete Markdown structure. If a template override is configured in settings, use
that instead.

## Guidelines

- Focus on architectural impact, not just listing files
- Group related changes to tell a coherent story
- Note any patterns introduced or deprecated
- Highlight database schema changes (migrations) prominently
- Include testing coverage gaps if apparent
- Performance notes only when relevant (query changes, caching, etc.)

## Additional Resources

### Templates
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/templates/technical-summary-template.md`** - Default Markdown structure for the technical summary

### References
- **`${CLAUDE_PLUGIN_ROOT}/skills/work-summary/references/file-categories.md`** - Default file categorization patterns and custom category examples
