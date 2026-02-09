---
name: docs-management:generate-index
description: Generate a compressed documentation index. Scans docs directories and produces a token-efficient INDEX.md using compact notation. By default writes INDEX.md inside the docs directory.
argument-hint: "[docs-path] [--dry-run] [--quadrant NAME]"
allowed-tools: Bash, Read, Glob
---

# Generate Documentation Index

Generate a compressed, machine-readable documentation index and write it to `INDEX.md` inside the docs directory.

## Default Behavior

By default this command:
1. Scans the project's `./docs/` directory for all `.md` files
2. Generates a compressed index with description hints from frontmatter
3. **Writes `INDEX.md`** inside the docs directory (overwrites if it already exists)
4. Reminds the user to add `@docs/INDEX.md` to their CLAUDE.md if not already present

Use `--dry-run` to preview the index without writing any files.

## Arguments

$ARGUMENTS

## Instructions

### Step 1: Determine the docs path

1. **If a path is provided in the arguments** -- use it directly
2. **If no path is provided** -- locate the project's main docs directory:
   - Use Glob to search for `docs/README.md` or `docs/` in the current working directory
   - If `./docs/` exists, use it
   - If not found, check for common alternatives: `./documentation/`, `./doc/`
   - If still not found, tell the user no docs directory was detected and ask them to specify the path

### Step 2: Run the script

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py <docs-path> [flags]
```

### Argument parsing

**Path argument** -- the docs directory to scan:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py /absolute/path/to/docs
```

**Dry run** -- preview without writing:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --dry-run
```

**Quadrant filter** -- if user mentions a specific section (tutorials, guides, reference, technical, architecture, research):
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --quadrant reference
```

**Explicit output target**:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --output ./custom/INDEX.md
```

### After running

- Confirm which INDEX.md was written and whether it was created or updated
- Check if the project's CLAUDE.md already contains `@docs/INDEX.md` (or the appropriate relative path to the index)
- If the `@` reference is missing, remind the user to add it to their CLAUDE.md so the index is loaded into context automatically
