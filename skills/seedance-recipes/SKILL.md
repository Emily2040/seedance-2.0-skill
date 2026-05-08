---
name: seedance-recipes
description: "This skill should be used when the user asks for a Seedance 2.0 template, genre recipe, product ad, lifestyle video, drama scene, music video, landscape shot, commercial, animation scene, or reusable production pattern."
license: MIT
user-invocable: true
tags:
  - templates
  - genres
  - recipes
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

# seedance-recipes

Use recipes as starting patterns, not rigid prompt templates. Pick the recipe that matches the user's outcome, then customize subject, action, camera, lighting, audio, and constraints. Recipes should preserve the one-beat discipline of a short clip.

## Recipe Families

| Family | Best use | Core pattern |
|---|---|---|
| Product | Ads, ecommerce, hero shots, material reveals. | `product anchor + one material change + controlled camera + logo preservation` |
| Lifestyle | Human use, food, travel, social clips. | `simple action + lived environment + handheld or natural light + ambient sound` |
| Drama | Emotion, dialogue, short narrative beats. | `character tag + gesture + motivated camera + silence or sparse sound` |
| Music video | Beat sync, dance, stylized edits. | `rhythm reference + visible beat changes + light pulses + clear character blocking` |
| Landscape | Establishing shots, nature, atmosphere. | `slow camera + weather motion + layered depth + natural sound` |
| Commercial | Brand-safe polish and function. | `problem/use/result beat + precise product constraint + clean light` |
| Animation | Original characters and stylized motion. | `medium + shape language + palette + elastic or weighted motion` |
| VFX | Transformations, particles, weather, energy. | `source + material behavior + interaction + dissipation endpoint` |

## Prompt Skeletons

**Product I2V:** `[Image1] is the product reference; preserve logo, label, shape, and materials exactly. [One material or light change]. Camera: [single move]. Lighting: [physical source]. Sound: [ambient/SFX].`

**Drama T2V:** `Character A [visible emotional action] in [specific setting]. Camera: [motivated framing]. Lighting: [motivated source]. Sound: [ambient or short dialogue]. End state: [changed expression/action].`

**Reference Motion:** `[Video1] provides only [camera/action/timing] reference; do not transfer identity, costume, logo, or environment. New subject: [authorized/original subject]. [Action and endpoint].`

**Animation:** `Original [character archetype] [action] in [environment]. Style: [medium, line quality, texture, palette]. Motion: [rhythm]. Camera and sound: [simple support].`

## Selection Rule

If a user gives many goals, choose the recipe that protects the most fragile requirement. Product identity beats camera spectacle; lip-sync beats large head motion; character consistency beats complex choreography; safety and authorization beat style mimicry.

## Output Contract

Return one selected recipe, why it fits, the customized prompt skeleton, and a compact final prompt.
