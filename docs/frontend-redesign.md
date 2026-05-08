# Frontend Redesign

The repository does not currently contain a standalone web app. The public frontend is the GitHub README plus SVG assets.

## v5.2 Design Goals

- Replace collapsed one-line Markdown with readable sections.
- Put the workflow selector near the top.
- Use dark/light hero assets with accessible SVG metadata.
- Show the skill constellation visually, then provide tables for navigation.
- Keep platform status source-aware instead of hardcoding stale claims.
- Validate design quality with `scripts/design_audit.py`.

## Assets

- `assets/hero-dark.svg`
- `assets/hero-light.svg`
- `assets/skill-map.svg`

## Design Rules

- No external fonts or scripts in SVG.
- Every SVG needs `<title>` and `<desc>`.
- README should stay readable on mobile and dark mode.
- Avoid dense badge walls and noisy decorative text.
