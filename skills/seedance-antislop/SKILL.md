---
name: seedance-antislop
description: "This skill should be used when a Seedance 2.0 prompt contains generic AI filler, hollow superlatives, vague cinematic language, bloated adjectives, weak verbs, or needs sharper production-specific wording."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - prompt-quality
  - anti-slop
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


# seedance-antislop

Remove filler that hides missing visual decisions.

## Test

Every major phrase should be visible to a camera, measurable by a light meter, audible in the mix, or observable as motion.

Replace:

- `epic` with scale, lens, motion, or stakes.
- `cinematic` with shot scale, camera move, lighting, or grade.
- `beautiful` with material, color, composition, or light behavior.
- `dynamic` with a specific movement and endpoint.

Load `[ref:anti-slop-lexicon]` for the extended replacement table.

## Output Contract

Return removed words, replacements, and the tightened prompt.
