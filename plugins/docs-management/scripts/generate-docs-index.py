#!/usr/bin/env python3
"""Generate compressed documentation indexes for Claude Code.

Scans a docs directory and produces a compact, machine-readable index
using a compressed notation format optimized for token efficiency.
By default, updates the project's CLAUDE.md between index markers.

Format rules:
  |           path delimiter prefix
  :           maps directory to contents
  {a,b}       groups multiple files in same directory
  ->          optional description hint (from frontmatter)

Examples:
  |getting-started/README.md    -> Learning-oriented guides
  |reference/api:{AUTH.md,ENDPOINTS.md}
  |technical:DATA-MODELS.md

Usage:
  python3 generate-docs-index.py ./docs                    # Updates CLAUDE.md
  python3 generate-docs-index.py ./docs --dry-run          # Print only, no writes
  python3 generate-docs-index.py ./docs --quadrant reference
  python3 generate-docs-index.py ./docs --output CLAUDE.md # Explicit target
"""

import argparse
import os
import sys
from collections import OrderedDict
from pathlib import Path


def parse_frontmatter(filepath):
    """Extract title and description from YAML frontmatter.

    Simple parser that handles --- delimited frontmatter without
    requiring external YAML libraries. Returns (title, description).
    """
    title = None
    description = None

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            if first_line != '---':
                return title, description

            for line in f:
                line = line.strip()
                if line == '---':
                    break
                if line.startswith('title:'):
                    title = line[len('title:'):].strip().strip('"').strip("'")
                elif line.startswith('description:'):
                    description = line[len('description:'):].strip().strip('"').strip("'")
    except (IOError, UnicodeDecodeError):
        pass

    return title, description


def extract_heading(filepath):
    """Extract the first H1 heading from a markdown file as fallback."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line.startswith('# ') and not line.startswith('##'):
                    return line[2:].strip()
    except (IOError, UnicodeDecodeError):
        pass
    return None


def get_hint(filepath):
    """Get a description hint for a file from frontmatter or heading."""
    title, description = parse_frontmatter(filepath)
    if description:
        return description
    if title:
        return title
    heading = extract_heading(filepath)
    if heading:
        return heading
    return None


QUADRANT_MAP = {
    'getting-started': 'Tutorials',
    'guides': 'How-to Guides',
    'reference': 'Reference',
    'technical': 'Technical Specs',
    'architecture': 'Explanation',
    'research': 'Research',
}

QUADRANT_DESCRIPTIONS = {
    'getting-started': 'Learning-oriented guides',
    'guides': 'Task-oriented procedures',
    'reference': 'Technical specifications',
    'technical': 'Technical specifications and data models',
    'architecture': 'Architecture and design rationale',
    'research': 'Research findings and analysis',
}

SECTION_MARKER = 'DOCS-INDEX'


def scan_docs(docs_path, quadrant_filter=None):
    """Scan docs directory and group files by relative directory.

    Returns OrderedDict mapping relative_dir -> list of (filename, hint).
    Excludes README.md and CLAUDE.md from file listings but includes
    directory README.md entries separately for top-level index.
    """
    docs_path = Path(docs_path).resolve()
    if not docs_path.is_dir():
        print("Error: '{}' is not a directory".format(docs_path), file=sys.stderr)
        sys.exit(1)

    groups = {}
    readme_entries = []

    for root, dirs, files in os.walk(str(docs_path)):
        dirs.sort()
        root_path = Path(root)
        rel_dir = root_path.relative_to(docs_path)
        rel_dir_str = str(rel_dir) if str(rel_dir) != '.' else ''

        # Apply quadrant filter
        if quadrant_filter:
            if rel_dir_str == '':
                # Skip root-level files when filtering by quadrant
                continue
            else:
                top_dir = rel_dir_str.split('/')[0] if '/' in rel_dir_str else rel_dir_str
                if top_dir != quadrant_filter:
                    continue

        md_files = sorted([f for f in files if f.endswith('.md')])

        for fname in md_files:
            full_path = root_path / fname
            hint = get_hint(str(full_path))

            if fname == 'README.md':
                if rel_dir_str:
                    readme_entries.append((rel_dir_str, hint))
                continue

            if fname == 'CLAUDE.md':
                continue

            if rel_dir_str not in groups:
                groups[rel_dir_str] = []
            groups[rel_dir_str].append((fname, hint))

    # Sort groups by key
    sorted_groups = OrderedDict(sorted(groups.items()))

    return sorted_groups, sorted(readme_entries, key=lambda x: x[0])


def format_index(groups, readme_entries, docs_root_label=None):
    """Format as compressed index."""
    lines = []

    root_label = docs_root_label or './docs/'
    if not root_label.endswith('/'):
        root_label += '/'
    lines.append('root:{}|IMPORTANT: Read relevant docs before implementing.'.format(root_label))
    lines.append('')

    # README entries (top-level directory index)
    if readme_entries:
        for dir_name, hint in readme_entries:
            entry = '|{}/README.md'.format(dir_name)
            if hint:
                entry += '    -> {}'.format(hint)
            elif dir_name in QUADRANT_DESCRIPTIONS:
                entry += '    -> {}'.format(QUADRANT_DESCRIPTIONS[dir_name])
            lines.append(entry)
        lines.append('')

    # Grouped file entries
    for dir_path, file_list in groups.items():
        if not file_list:
            continue

        if not dir_path:
            # Root-level files
            for fname, hint in file_list:
                entry = '|{}'.format(fname)
                if hint:
                    entry += '    -> {}'.format(hint)
                lines.append(entry)
        elif len(file_list) == 1:
            fname, hint = file_list[0]
            entry = '|{}:{}'.format(dir_path, fname)
            if hint:
                entry += '    -> {}'.format(hint)
            lines.append(entry)
        else:
            filenames = ','.join(f for f, _ in file_list)
            lines.append('|{}:{{{}}}'.format(dir_path, filenames))

    return '\n'.join(lines)


def format_claude_md(groups, readme_entries, docs_root_label=None):
    """Format for embedding in CLAUDE.md."""
    lines = []
    lines.append('### Documentation Index')
    lines.append('')
    lines.append('Use this index to find relevant documentation before implementing changes.')
    lines.append('')
    lines.append('```')
    lines.append(format_index(groups, readme_entries, docs_root_label))
    lines.append('```')

    return '\n'.join(lines)


def find_claude_md(docs_path):
    """Auto-detect CLAUDE.md by searching from docs_path up to project root.

    Looks for CLAUDE.md in the parent of the docs directory first,
    then searches upward for common project root indicators.
    """
    docs_resolved = Path(docs_path).resolve()

    # Start from the parent of the docs directory
    search_dir = docs_resolved.parent

    # Walk up looking for CLAUDE.md alongside project root indicators
    for _ in range(10):  # Safety limit
        candidate = search_dir / 'CLAUDE.md'
        if candidate.is_file():
            return str(candidate)

        # Check for project root indicators
        root_indicators = ['.git', 'package.json', 'composer.json', 'Cargo.toml',
                           'pyproject.toml', 'go.mod', '.claude']
        is_project_root = any((search_dir / ind).exists() for ind in root_indicators)

        if is_project_root:
            # This is the project root but no CLAUDE.md found
            return str(candidate)  # Return path where it should be created

        parent = search_dir.parent
        if parent == search_dir:
            break
        search_dir = parent

    # Fallback: CLAUDE.md next to docs dir
    return str(docs_resolved.parent / 'CLAUDE.md')


def update_section(filepath, marker, content):
    """Replace content between <!-- MARKER:START --> and <!-- MARKER:END --> markers.

    If the file exists but has no markers, appends the section with markers.
    If the file doesn't exist, creates it with the section.
    """
    start_marker = '<!-- {}:START -->'.format(marker)
    end_marker = '<!-- {}:END -->'.format(marker)
    section_block = '{}\n{}\n{}'.format(start_marker, content, end_marker)

    file_path = Path(filepath)

    if not file_path.is_file():
        # Create new CLAUDE.md with the section
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write('# CLAUDE.md\n\n{}\n'.format(section_block))
            return 'created'
        except IOError as e:
            print("Error creating '{}': {}".format(filepath, e), file=sys.stderr)
            sys.exit(1)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
    except IOError as e:
        print("Error reading '{}': {}".format(filepath, e), file=sys.stderr)
        sys.exit(1)

    start_idx = original.find(start_marker)
    end_idx = original.find(end_marker)

    if start_idx == -1 or end_idx == -1 or end_idx < start_idx:
        # No valid markers found — append section at end
        new_content = original.rstrip('\n') + '\n\n{}\n'.format(section_block)
        action = 'appended'
    else:
        # Replace content between markers (preserve markers themselves)
        new_content = original[:start_idx + len(start_marker)] + '\n' + content + '\n' + original[end_idx:]
        action = 'updated'

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
    except IOError as e:
        print("Error writing '{}': {}".format(filepath, e), file=sys.stderr)
        sys.exit(1)

    return action


def main():
    parser = argparse.ArgumentParser(
        description='Generate compressed documentation indexes for Claude Code. '
                    'By default, updates the project CLAUDE.md with a compressed index.'
    )
    parser.add_argument(
        'docs_dir',
        help='Path to the documentation directory to scan'
    )
    parser.add_argument(
        '--quadrant',
        choices=list(QUADRANT_MAP.keys()),
        help='Generate index for a specific Diataxis section only'
    )
    parser.add_argument(
        '--output',
        help='Target CLAUDE.md file path (default: auto-detect from project root)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print the index to stdout without writing any files'
    )
    parser.add_argument(
        '--section-marker',
        default=SECTION_MARKER,
        metavar='MARKER',
        help='Marker name for section delimiters (default: {})'.format(SECTION_MARKER)
    )
    parser.add_argument(
        '--docs-root',
        help='Override the docs root label for relative path display (e.g., ./docs/)'
    )

    args = parser.parse_args()

    # Scan docs
    groups, readme_entries = scan_docs(args.docs_dir, args.quadrant)

    # Determine docs root label
    docs_root_label = args.docs_root or './{}/'.format(Path(args.docs_dir).name)

    # Format output for CLAUDE.md
    output = format_claude_md(groups, readme_entries, docs_root_label)

    if args.dry_run:
        print(output)
        return

    # Determine target file
    target = args.output or find_claude_md(args.docs_dir)

    # Update the target file
    action = update_section(target, args.section_marker, output)
    print("{} CLAUDE.md index in '{}'".format(action.capitalize(), target))


if __name__ == '__main__':
    main()
