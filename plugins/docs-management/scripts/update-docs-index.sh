#!/usr/bin/env bash
# update-docs-index.sh - Regenerate the CLAUDE.md documentation index.
#
# Thin wrapper around generate-docs-index.py that auto-detects the docs
# directory and updates CLAUDE.md with a compressed index.
#
# Usage:
#   ./update-docs-index.sh [docs-dir] [--output CLAUDE.md] [--dry-run]
#
# Arguments:
#   docs-dir       Path to docs directory (default: ./docs)
#   --output       Explicit path to CLAUDE.md (default: auto-detect)
#   --dry-run      Print index without writing files

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GENERATOR="${SCRIPT_DIR}/generate-docs-index.py"

if [[ ! -f "$GENERATOR" ]]; then
    echo "Error: generate-docs-index.py not found at '$GENERATOR'" >&2
    exit 1
fi

# Default docs directory
DOCS_DIR="./docs"
EXTRA_ARGS=()

# Parse arguments — pass through to Python script
for arg in "$@"; do
    case "$arg" in
        -h|--help)
            echo "Usage: $(basename "$0") [docs-dir] [--output CLAUDE.md] [--dry-run]"
            echo ""
            echo "Regenerate the CLAUDE.md documentation index."
            echo ""
            echo "Arguments:"
            echo "  docs-dir         Path to docs directory (default: ./docs)"
            echo "  --output PATH    Explicit path to CLAUDE.md (default: auto-detect)"
            echo "  --dry-run        Print index without writing files"
            exit 0
            ;;
        --*)
            EXTRA_ARGS+=("$arg")
            ;;
        *)
            DOCS_DIR="$arg"
            ;;
    esac
done

if [[ ! -d "$DOCS_DIR" ]]; then
    echo "Error: '$DOCS_DIR' is not a directory" >&2
    exit 1
fi

python3 "$GENERATOR" "$DOCS_DIR" "${EXTRA_ARGS[@]}"
