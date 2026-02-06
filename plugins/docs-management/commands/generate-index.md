---
name: docs-management:generate-index
description: Generate a compressed documentation index and update CLAUDE.md. Scans docs directories and produces a token-efficient index using compact notation. By default writes to the project's CLAUDE.md between index markers.
argument-hint: "[docs-path] [--dry-run] [--quadrant NAME]"
allowed-tools: Bash, Read, Glob
---

# Generate Documentation Index

Generate a compressed, machine-readable documentation index and write it to the project's CLAUDE.md.

## Default Behavior

By default this command:
1. Scans the project's `./docs/` directory for all `.md` files
2. Generates a compressed index with description hints from frontmatter
3. **Writes the index to CLAUDE.md** between `<!-- DOCS-INDEX:START -->` and `<!-- DOCS-INDEX:END -->` markers
4. If CLAUDE.md has no markers, appends the index section with markers at the end
5. If CLAUDE.md doesn't exist, creates it with the index section

Use `--dry-run` to preview the index without writing any files.

## Arguments

$ARGUMENTS

## Instructions

### Step 1: Determine the docs path

1. **If a path is provided in the arguments** — use it directly
2. **If no path is provided** — locate the project's main docs directory:
   - Use Glob to search for `docs/README.md` or `docs/` in the current working directory
   - If `./docs/` exists, use it
   - If not found, check for common alternatives: `./documentation/`, `./doc/`
   - If still not found, tell the user no docs directory was detected and ask them to specify the path

### Step 2: Run the script

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py <docs-path> [flags]
```

### Argument parsing

**Path argument** — the docs directory to scan:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py /absolute/path/to/docs
```

**Dry run** — preview without writing:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --dry-run
```

**Quadrant filter** — if user mentions a specific section (tutorials, guides, reference, technical, architecture, research):
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --quadrant reference
```

**Explicit output target**:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --output ./CLAUDE.md
```

### After running

- If files were written, confirm which CLAUDE.md was updated and whether the section was created, appended, or updated
- If `--dry-run` was used, display the generated index to the user
