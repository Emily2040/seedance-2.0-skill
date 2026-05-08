#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED = ["id", "prompt", "expected_output", "assertions", "skills_expected_to_activate", "failure_mode"]
REQUIRED_IDS = {
    "api_status_check",
    "audio_lipsync",
    "copyright_rewrite",
    "direct_prompt_t2v",
    "filter_repair",
    "frontend_design_audit",
    "frontend_redesign",
    "i2v_minimal",
    "multi_character_scene",
    "product_ad_recipe",
    "progressive_disclosure",
    "real_person_authorization",
    "reference_role_map",
    "source_verification",
    "style_safe_animation",
    "troubleshoot_camera_chaos",
    "vague_idea_interview",
    "zh_compression",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    path = Path(args.repo) / "evals" / "evals.json"
    if not path.exists():
        print("Missing evals/evals.json")
        return 1

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"Invalid JSON: {exc}")
        return 1

    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) < 16:
        print("evals/evals.json must contain at least 16 cases")
        return 1

    ids = set()
    errors = []
    for i, case in enumerate(cases):
        if not isinstance(case, dict):
            errors.append(f"case {i} is not an object")
            continue
        for field in REQUIRED:
            if field not in case:
                errors.append(f"case {i} missing {field}")
        cid = case.get("id")
        if cid in ids:
            errors.append(f"duplicate id: {cid}")
        ids.add(cid)
        if not isinstance(case.get("assertions"), list) or len(case.get("assertions", [])) < 2:
            errors.append(f"case {cid} needs at least two assertions")
        if not isinstance(case.get("skills_expected_to_activate"), list) or not case.get("skills_expected_to_activate"):
            errors.append(f"case {cid} needs skills_expected_to_activate")

    missing_ids = REQUIRED_IDS - ids
    if missing_ids:
        errors.append("missing required eval ids: " + ", ".join(sorted(missing_ids)))

    if errors:
        print("Eval schema errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Eval schema passed: {len(cases)} cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
