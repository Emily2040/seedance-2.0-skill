---
name: seedance-filter
description: "This skill should be used when a Seedance 2.0 prompt is blocked, rejected, silently degraded, or likely to trigger a content filter; or when the user asks for a safer rewrite without losing the creative intent."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - content-filter
  - safe-rewrite
  - seedance-20
metadata:
  version: "5.2.0"
  updated: "2026-05-08"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---


# seedance-filter

Use this when a prompt is blocked, degraded, or likely to trip moderation.

## Repair Method

1. Identify the creative intent.
2. Identify risky surface wording.
3. Replace risky terms with professional, non-graphic, production-context language.
4. Preserve composition, action, mood, and camera logic.
5. Do not help bypass safety systems.

Load `[ref:filter-vocab]` for safer substitutions.

## Output Contract

Return likely trigger class, safer wording, final prompt, and what changed.
