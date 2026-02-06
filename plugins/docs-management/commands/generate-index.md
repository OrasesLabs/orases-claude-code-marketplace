---
name: docs-management:generate-index
description: Generate a compressed documentation index for Claude Code. Scans docs directories and outputs a token-efficient index using compact notation. Supports filtering by quadrant, multiple output formats, and updating existing files.
argument-hint: "[docs-path] [--quadrant NAME] [--format full|readme|claude-md]"
allowed-tools: Bash, Read
---

# Generate Documentation Index

Generate a compressed, machine-readable documentation index optimized for Claude Code discovery.

## Arguments

$ARGUMENTS

## Instructions

Run the `generate-docs-index.py` script to produce the documentation index.

### Default behavior (no arguments)

If no arguments are provided, scan the current project's `./docs/` directory:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs
```

### With arguments

Parse the arguments to determine which flags to pass:

**Path argument** - First positional argument is the docs directory path:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py <path>
```

**Quadrant filter** - If user mentions a specific section (tutorials, guides, reference, technical, architecture, research):
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --quadrant reference
```

**Format options**:
- `full` (default) - Raw compressed index for stdout
- `readme` - Wrapped in a README template for a quadrant
- `claude-md` - Formatted for CLAUDE.md embedding

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --format claude-md
```

**Write to file**:
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --format claude-md --output CLAUDE.md
```

**Update a section in an existing file** (replaces content between markers):
```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/generate-docs-index.py ./docs --format claude-md --output CLAUDE.md --update-section DOCS-INDEX
```

This replaces content between `<!-- DOCS-INDEX:START -->` and `<!-- DOCS-INDEX:END -->` markers.

**Regenerate all indexes at once**:
```bash
bash ${CLAUDE_PLUGIN_ROOT}/scripts/update-docs-index.sh ./docs --claude-md CLAUDE.md
```

### Compressed Index Format

The output uses a compact notation:

```
root:./docs/|IMPORTANT: Read relevant docs before implementing.

|getting-started/README.md    -> Learning-oriented guides
|guides/README.md             -> Task-oriented procedures
|reference/README.md          -> Technical specifications

|reference/api:{AUTHENTICATION.md,ENDPOINTS.md,ERROR-CODES.md}
|technical:{API-SPECIFICATION.md,DATA-MODELS.md}
```

### After running

Display the generated index to the user. If using `--update-section`, confirm which file and section were updated.
