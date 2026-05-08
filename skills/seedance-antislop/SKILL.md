---
name: seedance-antislop
description: "This skill should be used when a Seedance 2.0 prompt contains generic AI filler, hollow superlatives, vague cinematic language, bloated adjectives, weak verbs, or needs sharper production-specific wording."
license: MIT
user-invocable: true
tags:
  - prompt-quality
  - anti-slop
  - seedance-20
metadata:
  version: "5.3.0"
  updated: "2026-05-08"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-antislop

Remove filler that hides missing visual decisions. A strong Seedance prompt uses observable nouns, verbs, camera moves, light sources, sound cues, and constraints. A weak prompt asks for excellence without saying what excellence looks or sounds like.

## Visibility Test

Every major phrase should be visible to a camera, measurable by a light meter, audible in the mix, or observable as motion. If a phrase cannot pass that test, replace it with production language.

| Filler | Ask what it means | Strong replacement pattern |
|---|---|---|
| cinematic | What camera and light make it cinematic? | `locked close-up, warm practical key, cool rim light` |
| epic | What is the scale or stake? | `wide low-angle shot, tiny figure against storm wall` |
| beautiful | What color, texture, or light behavior? | `pearl highlights on wet ceramic, soft window bounce` |
| dynamic | What moves, how fast, and where does it end? | `fast lateral track ending on the hero label` |
| professional | What production setup? | `clean commercial tabletop, controlled reflection, no clutter` |

## Rewrite Pass

First, underline all superlatives and vague style labels. Second, decide whether each word should become camera, light, motion, material, sound, or constraint language. Third, reduce duplicates. Fourth, keep the prompt within the character budget and preserve reference tags.

## Do Not Over-Correct

Do not remove useful genre language when it is paired with concrete direction. `Noir hallway with hard venetian-blind shadows` is useful; `dramatic cinematic noir vibes` is not. Keep terms that communicate medium, era, palette, or lens behavior.

Load `[ref:anti-slop-lexicon]` for the extended replacement table.

## Output Contract

Return removed words, replacements grouped by camera/light/motion/sound/constraint, and the tightened prompt.
