# Changelog

All notable changes to the docs-management plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0-beta-1] - 2026-02-06

### Added

- **Compressed Documentation Index System** - Generate token-efficient, machine-readable documentation indexes
- `generate-docs-index.py` script - Scans docs directories and produces compressed indexes with frontmatter extraction
  - `--quadrant` flag to filter by Diataxis section
  - `--format` flag supporting `full`, `readme`, and `claude-md` output formats
  - `--output` flag to write directly to file
  - `--update-section` flag to replace content between markers in existing files
  - `--docs-root` flag to override relative path display
- `update-docs-index.sh` script - Regenerates all quadrant indexes and optionally updates CLAUDE.md in one pass
- `/docs-management:generate-index` command - Slash command to run index generation directly

## [1.0.0] - 2026-02-04

### Added

- Initial release with Diataxis framework support
- Documentation commands: create-tutorial, create-how-to, create-reference, create-explanation
- Project setup and migration commands
- Coverage review and git-based update detection
- Writer skills with embedded templates and quality checklists
- Documentation engineer agent for complex tasks
