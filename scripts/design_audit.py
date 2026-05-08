#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repo", nargs="?", default=".")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    root = Path(args.repo).resolve()
    errors = []

    readme = root / "README.md"
    if not readme.exists():
        errors.append("README.md missing")
    else:
        text = readme.read_text(encoding="utf-8")
        lines = text.splitlines()
        if len(lines) < 80:
            errors.append(f"README.md is too short or collapsed ({len(lines)} lines)")
        long_lines = [i + 1 for i, line in enumerate(lines) if len(line) > 500]
        if long_lines:
            errors.append("README.md has lines over 500 chars: " + ", ".join(map(str, long_lines[:10])))
        for required in ["<picture>", "## Start Here", "## Skill Map", "## Validation", "## Design Standard"]:
            if required not in text:
                errors.append(f"README.md missing `{required}`")

    if not (root / "docs" / "frontend-redesign.md").exists():
        errors.append("missing docs/frontend-redesign.md")

    for rel in ["assets/hero-dark.svg", "assets/hero-light.svg", "assets/skill-map.svg"]:
        path = root / rel
        if not path.exists():
            errors.append(f"missing asset: {rel}")
            continue
        svg = path.read_text(encoding="utf-8", errors="ignore")
        if "<svg" not in svg:
            errors.append(f"{rel} is not an SVG")
        if "<title>" not in svg or "<desc>" not in svg:
            errors.append(f"{rel} missing accessible title/desc")
        if re.search(r"<script|href=[\"\']https?://|xlink:href=[\"\']https?://", svg, re.I):
            errors.append(f"{rel} must not include scripts or external resources")

    if errors:
        print("Design audit errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Design audit passed: README and SVG assets are structured and accessible.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
