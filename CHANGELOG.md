# Changelog — seedance-20

All notable changes to this project are documented here.

## [5.2.0] — 2026-05-08

### Fixed

- Repaired the partial v5.1 deployment: restored multiline Markdown, multiline YAML frontmatter, real Python scripts, non-empty evals, and the missing GitHub Actions workflow.
- Replaced old one-line active files that made README, references, and scripts render poorly.
- Normalized all 23 sub-skill frontmatter blocks to `metadata.version: "5.2.0"` and `metadata.parent: "seedance-20"`.

### Changed

- Redesigned the GitHub-facing README as a cleaner project front page with a start-here table, skill map, reference library, validation section, and design standard.
- Replaced neon/overloaded visual language with a disciplined cinematic-control design system.
- Converted oversized active sub-skills into lean procedural routers while preserving old local content through the patcher backup/migration path.
- Updated platform guidance to source-aware, date-stamped language.

### Added

- New SVG frontend assets: `assets/hero-dark.svg`, `assets/hero-light.svg`, and `assets/skill-map.svg`.
- Validation scripts: `scripts/validate_skills.py`, `scripts/content_audit.py`, `scripts/eval_schema_check.py`, and `scripts/design_audit.py`.
- CI workflow: `.github/workflows/validate-skills.yml`.
- Evals: `evals/evals.json` with 14 realistic test cases.
- References: `api-status.md`, `source-registry.md`, `audio-guide.md`, `anti-slop-lexicon.md`, `filter-vocab.md`, `progressive-disclosure.md`, `eval-rubric.md`, and `frontend-design-system.md`.

## [5.1.0] — 2026-05-08

Validation, status, and progressive-disclosure repair release. Superseded by v5.2.0 because the pushed v5.1 files were partially collapsed and incomplete.

## [5.0.0] — 2026-03-03

Intent-first prompting release. Introduced the Director Formula, short-prompt preference, expanded references, and quad-modal workflow routing.

## Historical Releases

Earlier v3.x and v4.x releases built the modular skill structure, multilingual vocabulary, example library, troubleshooting modules, and platform support matrix. See repository history for the full legacy changelog.
