# Seedance v5.1.0 Fix Pack

This pack applies the v5.1.0 repair release to a local checkout of `Emily2040/seedance-2.0`.

## Apply

```bash
cd /path/to/seedance-2.0
python3 -S /path/to/seedance_fix_pack/apply_seedance_fixes.py .
python scripts/validate_skills.py --strict
python scripts/content_audit.py --strict
```

## What it fixes

1. Normalizes YAML frontmatter for root and all 23 sub-skills.
2. Moves `metadata.parent` into the correct YAML location.
3. Rewrites skill descriptions into third-person trigger format.
4. Replaces stale Feb. 2026 API/face-status language with dated April 2026 guidance.
5. Adds `references/api-status.md` and `references/source-registry.md`.
6. Adds validation scripts and GitHub Actions CI.
7. Adds `evals/evals.json` with realistic test cases.
8. Moves oversized legacy skill bodies into `references/migrated/` before replacing active skill bodies with lean routers.
9. Patches risky studio/franchise/clone wording in active docs.
10. Adds a release plan and a machine-readable change manifest.

The script creates `.bak-v5.1.0` backups for files it edits. It does not delete legacy content; oversized active skill bodies are archived before replacement.
