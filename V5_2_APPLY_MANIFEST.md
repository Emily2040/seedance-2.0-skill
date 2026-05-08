# Seedance v5.2.0 Apply Manifest

Applied during local fix-pack integration and finalized for public-readiness review on 2026-05-08 UTC.

Backup note: create a branch or archive before reapplying this manifest manually. No sandbox-local backup path is part of the public repository.

## Files written

- `.github/workflows/validate-skills.yml`
- `CHANGELOG.md`
- `README.md`
- `SKILL.md`
- `assets/hero-dark.svg`
- `assets/hero-light.svg`
- `assets/skill-map.svg`
- `docs/frontend-redesign.md`
- `docs/v5.2-frontend-audit.md`
- `docs/v5.2-release-plan.md`
- `evals/evals.json`
- `references/anti-slop-lexicon.md`
- `references/api-status.md`
- `references/audio-guide.md`
- `references/eval-rubric.md`
- `references/filter-vocab.md`
- `references/frontend-design-system.md`
- `references/genre-guides.md`
- `references/i2v-guide.md`
- `references/intent-vs-precision.md`
- `references/json-schema.md`
- `references/platform-constraints.md`
- `references/progressive-disclosure.md`
- `references/prompt-examples.md`
- `references/quick-ref.md`
- `references/reference-workflow.md`
- `references/source-registry.md`
- `references/storytelling-framework.md`
- `references/vocab/es.md`
- `references/vocab/ja.md`
- `references/vocab/ko.md`
- `references/vocab/ru.md`
- `references/vocab/zh.md`
- `scripts/content_audit.py`
- `scripts/design_audit.py`
- `scripts/eval_schema_check.py`
- `scripts/validate_skills.py`
- `skills/seedance-antislop/SKILL.md`
- `skills/seedance-audio/SKILL.md`
- `skills/seedance-camera/SKILL.md`
- `skills/seedance-characters/SKILL.md`
- `skills/seedance-copyright/SKILL.md`
- `skills/seedance-examples-zh/SKILL.md`
- `skills/seedance-filter/SKILL.md`
- `skills/seedance-interview/SKILL.md`
- `skills/seedance-interview-short/SKILL.md`
- `skills/seedance-lighting/SKILL.md`
- `skills/seedance-motion/SKILL.md`
- `skills/seedance-pipeline/SKILL.md`
- `skills/seedance-prompt/SKILL.md`
- `skills/seedance-prompt-short/SKILL.md`
- `skills/seedance-recipes/SKILL.md`
- `skills/seedance-style/SKILL.md`
- `skills/seedance-troubleshoot/SKILL.md`
- `skills/seedance-vfx/SKILL.md`
- `skills/seedance-vocab-es/SKILL.md`
- `skills/seedance-vocab-ja/SKILL.md`
- `skills/seedance-vocab-ko/SKILL.md`
- `skills/seedance-vocab-ru/SKILL.md`
- `skills/seedance-vocab-zh/SKILL.md`
- `removed scripts/__pycache__`

## Legacy skill bodies archived

- `references/migrated/v5.2-legacy-skill-bodies/seedance-audio.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-copyright.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-antislop.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-filter.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-vocab-zh.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-vocab-ja.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-vocab-ko.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-vocab-es.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-vocab-ru.md`
- `references/migrated/v5.2-legacy-skill-bodies/seedance-examples-zh.md`

## Required validation

```bash
python scripts/validate_skills.py --strict
python scripts/content_audit.py --strict
python scripts/eval_schema_check.py --strict
python scripts/design_audit.py --strict
```

## Additional refactor cleanup

After applying the payload, the refactor removed stale v5.1 public backup/release artifacts from the active tree, including `*.bak-v5.1.0`, `RUN_V5_1_0_VALIDATION.md`, `RELEASE_PLAN.md`, and `v5.1.0-change-manifest.json`. The original content remains recoverable through Git history and the patcher's external selected-file backup. The README reference library was also normalized to remove duplicate rows and list all 22 v5.2 reference files.
