# Release Plan

## v5.1.0

Must ship: YAML repair, trigger descriptions, current API status references, CI validation, eval plan, IP-safe wording repairs, and progressive-disclosure migration of oversized skill bodies.

Validation:
```bash
python scripts/validate_skills.py --strict
python scripts/content_audit.py --strict
```

## v5.2.0

Must ship: deeper eval runner, curated vocabulary references, more example labels, and benchmarked prompt outputs.
