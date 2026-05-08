---
name: seedance-prompt
description: "This skill should be used when the user asks to write, improve, translate, compress, or debug a Seedance 2.0 video prompt; mentions T2V, I2V, V2V, R2V, camera direction, prompt quality, or provides reference assets for a production-ready prompt."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - prompt-engineering
  - video-generation
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


# seedance-prompt

Build production-ready Seedance prompts from clear concepts or supplied reference assets.

## Director Formula

`Subject + Action + Scene + Camera + Lighting/Style + Audio + Constraints`

Use the formula flexibly. Do not force every slot if a reference asset already shows the information.

## Mode Gate

- T2V: describe subject, action, scene, camera, style, and constraints.
- I2V: describe only motion, camera, timing, transformation, and audio. Do not repeat visible static details.
- V2V/R2V: map each reference to a role before writing the prompt.

## Final Output Contract

Return:

1. Mode: T2V, I2V, V2V, or R2V.
2. Reference role map, if any.
3. Final prompt.
4. Optional Chinese compressed version when useful.
5. Safety or copyright note when relevant.

Before finalizing, run an anti-slop pass and remove vague quality boosters.
