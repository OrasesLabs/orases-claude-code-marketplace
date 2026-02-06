#!/usr/bin/env bash
# update-docs-index.sh - Regenerate all documentation indexes in one pass.
#
# Iterates over each quadrant directory under the docs root, calls
# generate-docs-index.py for each, and optionally updates CLAUDE.md.
#
# Usage:
#   ./update-docs-index.sh [docs-dir] [--claude-md PATH]
#
# Arguments:
#   docs-dir       Path to docs directory (default: ./docs)
#   --claude-md    Path to CLAUDE.md to update the main index section
#
# The script expects generate-docs-index.py to be in the same directory.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="${SCRIPT_DIR}/generate-docs-index.py"

# Defaults
DOCS_DIR="./docs"
CLAUDE_MD=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case "$1" in
        --claude-md)
            CLAUDE_MD="$2"
            shift 2
            ;;
        --claude-md=*)
            CLAUDE_MD="${1#*=}"
            shift
            ;;
        -h|--help)
            echo "Usage: $(basename "$0") [docs-dir] [--claude-md PATH]"
            echo ""
            echo "Regenerate all documentation indexes."
            echo ""
            echo "Arguments:"
            echo "  docs-dir         Path to docs directory (default: ./docs)"
            echo "  --claude-md PATH Path to CLAUDE.md to update main index section"
            exit 0
            ;;
        *)
            DOCS_DIR="$1"
            shift
            ;;
    esac
done

if [[ ! -d "$DOCS_DIR" ]]; then
    echo "Error: '$DOCS_DIR' is not a directory" >&2
    exit 1
fi

if [[ ! -f "$GENERATOR" ]]; then
    echo "Error: generate-docs-index.py not found at '$GENERATOR'" >&2
    exit 1
fi

# Known quadrant directories
QUADRANTS=("getting-started" "guides" "reference" "technical" "architecture" "research")

updated=0
skipped=0

echo "Scanning docs in: $DOCS_DIR"
echo ""

for quadrant in "${QUADRANTS[@]}"; do
    quadrant_dir="${DOCS_DIR}/${quadrant}"

    if [[ ! -d "$quadrant_dir" ]]; then
        skipped=$((skipped + 1))
        continue
    fi

    readme="${quadrant_dir}/README.md"

    if [[ -f "$readme" ]]; then
        # Check if README has update markers
        if grep -q "<!-- DOCS-INDEX:START -->" "$readme" 2>/dev/null; then
            python3 "$GENERATOR" "$DOCS_DIR" \
                --quadrant "$quadrant" \
                --format readme \
                --output "$readme" \
                --update-section "DOCS-INDEX" \
                --docs-root "./${DOCS_DIR##*/}/"
            echo "  [updated] ${quadrant}/README.md (section replaced)"
            updated=$((updated + 1))
        else
            echo "  [skipped] ${quadrant}/README.md (no DOCS-INDEX markers)"
        fi
    else
        # Generate a new README with the index
        python3 "$GENERATOR" "$DOCS_DIR" \
            --quadrant "$quadrant" \
            --format readme \
            --output "$readme" \
            --docs-root "./${DOCS_DIR##*/}/"
        echo "  [created] ${quadrant}/README.md"
        updated=$((updated + 1))
    fi
done

# Update CLAUDE.md if specified and has markers
if [[ -n "$CLAUDE_MD" ]]; then
    if [[ ! -f "$CLAUDE_MD" ]]; then
        echo ""
        echo "Warning: CLAUDE.md not found at '$CLAUDE_MD', skipping"
    elif grep -q "<!-- DOCS-INDEX:START -->" "$CLAUDE_MD" 2>/dev/null; then
        python3 "$GENERATOR" "$DOCS_DIR" \
            --format claude-md \
            --output "$CLAUDE_MD" \
            --update-section "DOCS-INDEX" \
            --docs-root "./${DOCS_DIR##*/}/"
        echo ""
        echo "  [updated] CLAUDE.md (DOCS-INDEX section)"
        updated=$((updated + 1))
    else
        echo ""
        echo "  [skipped] CLAUDE.md (no DOCS-INDEX markers found)"
        echo "  Add these markers where you want the index:"
        echo "    <!-- DOCS-INDEX:START -->"
        echo "    <!-- DOCS-INDEX:END -->"
    fi
fi

echo ""
echo "Done: $updated updated, $skipped quadrants not found"
