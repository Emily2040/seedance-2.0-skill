---
name: seedance-prompt-short
description: "This skill should be used when the user asks for a compact Seedance 2.0 prompt, short Chinese prompt, prompt compression, 30-100 word output, or removal of unnecessary prompt language."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - prompt-compression
  - chinese-prompt
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


# seedance-prompt-short

Compress Seedance prompts without losing the production signal.

## Compression Priority

Preserve in this order:

1. Reference tags.
2. Subject nouns.
3. Action verbs.
4. Camera move.
5. Light source or atmosphere.
6. Audio cue.
7. Safety or continuity constraint.

Delete generic adjectives before deleting physical details.

## Output Contract

Return one compact prompt, ideally 30-100 English words or an equivalent Chinese prompt when the user asks for Chinese or maximum compression.
