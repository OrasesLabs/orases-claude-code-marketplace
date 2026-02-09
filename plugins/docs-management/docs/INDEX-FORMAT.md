# Compressed Documentation Index Format

*Reference for the token-efficient index notation used in CLAUDE.md documentation indexes.*

## Overview

The compressed index format provides a machine-readable map of a project's documentation tree. It is designed to be embedded in CLAUDE.md so that Claude Code can quickly locate relevant docs before implementing changes, without reading every file.

The format prioritizes **token efficiency** -- conveying the maximum amount of structural information in the fewest tokens possible.

## Format Specification

### Root Declaration

Every index starts with a root declaration:

```
root:<path>|<directive>
```

| Part | Description |
|------|-------------|
| `root:` | Literal prefix, always present |
| `<path>` | Relative path to the docs directory (e.g., `./docs/`) |
| `|` | Separator between path and directive |
| `<directive>` | Instruction for the reader (e.g., `IMPORTANT: Read relevant docs before implementing.`) |

Example:

```
root:./docs/|IMPORTANT: Read relevant docs before implementing.
```

### File Entries

Each entry starts with `|` as a path delimiter prefix:

```
|<path>
```

Example:

```
|getting-started/README.md
```

### Description Hints

Append `->` followed by a short description extracted from the file's YAML frontmatter or H1 heading:

```
|<path>    -> <description>
```

The whitespace before `->` is for alignment readability and is not significant.

Example:

```
|architecture/OVERVIEW.md    -> System architecture and design rationale
```

### Directory Grouping with `:`

Use `:` to map a directory to its contents, avoiding path repetition:

```
|<directory>:<filename>
```

Example:

```
|technical:DATA-MODELS.md    -> Database structure and relationships
```

This is equivalent to `|technical/DATA-MODELS.md` but saves tokens when the directory name is long.

### Multi-File Grouping with `{}`

When a directory contains multiple files, group them with curly braces and commas:

```
|<directory>:{<file1>,<file2>,<file3>}
```

Example:

```
|reference/api:{AUTH.md,ENDPOINTS.md,ERROR-CODES.md}
```

This is equivalent to listing each file separately:

```
|reference/api/AUTH.md
|reference/api/ENDPOINTS.md
|reference/api/ERROR-CODES.md
```

> **Note:** When using `{}` grouping, individual file hints are omitted to keep the line compact. Directory-level README hints cover the group instead.

### README Entries

Directory README files are listed separately at the top of the index to provide section-level context:

```
|<directory>/README.md    -> <section description>
```

These serve as navigation hints for each major section. The description may come from the file's frontmatter, H1 heading, or a default based on the Diataxis quadrant.

## Complete Example

```
root:./docs/|IMPORTANT: Read relevant docs before implementing.

|getting-started/README.md    -> Learning-oriented guides
|guides/README.md             -> Task-oriented procedures
|reference/README.md          -> Technical specifications
|architecture/README.md       -> Architecture and design rationale
|research/README.md           -> Research findings and analysis

|getting-started:{QUICK-START.md,SETUP-GUIDE.md,PREREQUISITES.md}
|guides/developer:{CONTRIBUTING.md,TESTING.md,DEPLOYMENT.md}
|guides/user:FEATURE-GUIDE.md    -> End-user feature walkthrough
|reference:CONFIGURATION.md      -> Config options reference
|reference/api:{AUTH.md,ENDPOINTS.md,ERROR-CODES.md}
|technical:{API-SPECIFICATION.md,DATA-MODELS.md,DATABASE-SCHEMA.md}
|architecture:{OVERVIEW.md,DESIGN-DECISIONS.md,DATA-FLOW.md,SECURITY.md}
|research/findings:{PERFORMANCE-AUDIT.md,API-COMPARISON.md}
```

## Notation Summary

| Symbol | Meaning | Example |
|--------|---------|---------|
| `root:` | Docs root path declaration | `root:./docs/` |
| `\|` | Path delimiter prefix (starts every entry) | `\|getting-started/README.md` |
| `:` | Maps directory to file(s) | `\|technical:DATA-MODELS.md` |
| `{a,b}` | Groups multiple files in one directory | `\|api:{AUTH.md,ENDPOINTS.md}` |
| `->` | Description hint from frontmatter/heading | `-> System architecture` |
| `\|` (in root) | Separates root path from directive | `root:./docs/\|IMPORTANT: ...` |

## How Hints Are Extracted

The generator extracts description hints in this priority order:

1. **YAML frontmatter `description:`** field (highest priority)
2. **YAML frontmatter `title:`** field
3. **First H1 heading** (`# Heading`) in the file
4. **Diataxis quadrant default** for README files (e.g., "Learning-oriented guides" for `getting-started/`)
5. No hint (omitted if nothing is found)

## CLAUDE.md Integration

The index is written as a standalone `INDEX.md` file inside the docs directory. To include it in Claude's context, add an `@` file reference in your project's CLAUDE.md:

```markdown
@docs/INDEX.md
```

This keeps the root CLAUDE.md clean while ensuring the index is always loaded into context. The `INDEX.md` file is overwritten in place on each regeneration -- no marker-based splicing is needed.

## Quadrant Filtering

The generator supports filtering output to a specific Diataxis section using the `--quadrant` flag:

| Quadrant | Directory | Diataxis Type |
|----------|-----------|---------------|
| `getting-started` | `getting-started/` | Tutorials |
| `guides` | `guides/` | How-to Guides |
| `reference` | `reference/` | Reference |
| `technical` | `technical/` | Technical Specs |
| `architecture` | `architecture/` | Explanation |
| `research` | `research/` | Research |

## Design Rationale

**Why a compressed format instead of plain file lists?**

- A full file tree with paths repeated on every line costs many tokens in a CLAUDE.md context
- Grouping (`{}`) eliminates redundant directory prefixes
- Hints (`->`) give Claude enough context to select the right file without reading every one
- The `root:` directive instructs Claude on how to use the index

**Why a standalone INDEX.md with `@` reference?**

- Keeps the root CLAUDE.md clean and human-readable
- `@docs/INDEX.md` in CLAUDE.md auto-loads the index into every Claude Code session
- No marker-based splicing needed -- the entire file is overwritten on regeneration
- The index lives alongside the documentation it describes
