---
name: docs-management:generate-index
description: Generate a compressed documentation index. Scans docs directories and produces a token-efficient INDEX.md using compact notation. By default writes INDEX.md inside the docs directory.
argument-hint: "[docs-path] [--dry-run] [--quadrant NAME]"
allowed-tools: Bash, Read, Write, Glob, AskUserQuestion
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

### Step 2: Check for missing README files

Before generating the index, verify that every subdirectory in the docs path contains a `README.md`. Directory READMEs are what provide the `-> description` labels in the index — without them, directories appear unlabeled.

1. **Scan for subdirectories** -- use Glob to find all subdirectories under the docs path, then check which ones are missing a `README.md`
   - Use `docs-path/**/` to discover directories
   - For each directory, check if `README.md` exists
   - Exclude the root docs directory itself (it has its own README handling)
   - Exclude `assets/`, `images/`, `diagrams/`, and other non-documentation directories
2. **If all directories have READMEs** -- report that all directories are covered and proceed to Step 3
3. **If any directories are missing READMEs** -- present the list of directories without READMEs and ask the user what to do:
   - **Option 1: Create README files** -- Generate a `README.md` for each missing directory before indexing. Each README should have:
     - YAML frontmatter with `title` and `description` fields derived from the directory name and a quick scan of the files inside it
     - An H1 heading matching the title
     - A brief 1-2 sentence description of the directory's contents based on scanning the filenames and any available frontmatter in the files within
     - A note that it was auto-generated
   - **Option 2: Generate index without READMEs** -- Skip README creation and proceed directly to Step 3. Directories without READMEs will appear unlabeled in the index.
   - **Option 3: Create READMEs for selected directories only** -- Let the user pick which directories should get READMEs

**When creating READMEs**, follow this template:

```markdown
---
title: {Directory Label}
description: {Brief description of directory contents}
---

# {Directory Label}

{1-2 sentence description of what this directory contains, based on the files found inside.}
```

To derive good descriptions:
- Read the first few files in the directory to understand their content
- Use frontmatter descriptions or H1 headings from those files to infer the directory's purpose
- Keep descriptions concise and informative

### Step 3: Run the script

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
