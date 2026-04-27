---
name: seedance-antislop
description: "This skill should be used when the user wants to remove AI filler language, hollow superlatives, generic cinematic fluff, vague adjectives, or non-actionable wording from a Seedance 2.0 prompt."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - prompt-quality
  - anti-slop
  - compression
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

# seedance-antislop

Use this skill to remove generic AI-video filler and convert vague language into observable production instructions.

Test: if a camera operator, lighting technician, actor, or editor cannot act on a word, replace it.

Remove first: cinematic masterpiece, ultra realistic, breathtaking, stunning, beautiful, epic, professional quality, dramatic atmosphere, magical, dreamy, highly detailed.

Replace with: subject noun, action verb, one camera move, light source, material texture, timing, reference role, physical consequence, audio cue.

Compression order: reference tags -> subject nouns -> action verbs -> camera move -> light source -> audio cue -> style constraint. Delete generic adjectives first.

Return the cleaned prompt, removed phrases, and one sentence explaining the compression tradeoff.

Legacy details moved to `references/migrated/seedance-antislop-original.md`.
