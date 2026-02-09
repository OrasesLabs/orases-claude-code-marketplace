# Changelog

All notable changes to the docs-management plugin will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0-beta-3] - 2026-02-09

### Added

- `docs/INDEX-FORMAT.md` - Compressed index format reference documentation for human and machine consumption
- Index regeneration instructions added to `documentation-standards` skill with event table and usage guidance
- Index regeneration checklist item added to all 6 writer skills (tutorial, how-to, tech-specs, research, system-overview, adr)

### Fixed

- Marketplace version pin (`marketplace.json`) now matches plugin version

### Changed

- Updated README with generate-index command, scripts section, compressed index documentation, and usage examples

## [1.1.0-beta-2] - 2026-02-06

### Added

- **Compressed Documentation Index System** - Generate token-efficient, machine-readable documentation indexes that update CLAUDE.md
- `generate-docs-index.py` script - Scans docs directories and writes compressed index to CLAUDE.md
  - Auto-detects project CLAUDE.md from docs directory location
  - Creates CLAUDE.md if missing, appends markers if absent, updates in-place if present
  - `--dry-run` flag to preview index without writing files
  - `--quadrant` flag to filter by Diataxis section
  - `--output` flag to target a specific CLAUDE.md
  - `--docs-root` flag to override relative path display
- `update-docs-index.sh` script - Thin wrapper for quick CLAUDE.md index regeneration
- `/docs-management:generate-index` command - Slash command to run index generation directly

## [1.0.0] - 2026-02-04

### Added

- Initial release with Diataxis framework support
- Documentation commands: create-tutorial, create-how-to, create-reference, create-explanation
- Project setup and migration commands
- Coverage review and git-based update detection
- Writer skills with embedded templates and quality checklists
- Documentation engineer agent for complex tasks
