---
name: seedance-filter
description: "This skill should be used when a Seedance 2.0 prompt is blocked, rejected, silently degraded, or likely to trigger a content filter; or when the user asks for a safer rewrite without losing the creative intent."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - content-filter
  - safety
  - rewrites
metadata:
  version: "5.1.0"
  updated: "2026-04-27"
  parent: "seedance-20"
  author: "Emily (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: ""
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-filter

Use this skill when a prompt is blocked, degraded, or likely to trigger content filters. The job is not to bypass safety systems; it is to preserve legitimate creative intent with safer surface wording.

Diagnostic questions:
1. Is the risk identity-based: celebrity, public figure, named character, brand, logo, voice, or face?
2. Is the risk violence, sexuality, minors, self-harm, or weapon wording?
3. Is the risk copyright or platform policy?
4. Is the risk false-positive wording that can be replaced with neutral production language?

Rewrite rules:
- Replace protected identity with original archetype.
- Replace graphic harm with non-graphic action consequence.
- Replace weapon emphasis with choreography, blocking, or prop-neutral movement.
- Replace clone/copy/replicate with reference-informed pacing only when references are owned/licensed.

Return: likely trigger category, safe rewrite, retained intent, removed terms, and retry variant.

Legacy details moved to `references/migrated/seedance-filter-original.md`.
