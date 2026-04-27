---
name: seedance-copyright
description: "This skill should be used when a Seedance 2.0 prompt mentions named characters, franchises, celebrities, public figures, brand logos, copyrighted scenes, music titles, streamer originals, or real-person likeness workflows and needs an IP-safe rewrite."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - copyright
  - ip-safety
  - policy
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

# seedance-copyright

Use this skill to rewrite risky prompts involving protected characters, franchises, celebrities, public figures, brand logos, copyrighted scenes, music titles, studio styles, or real-person likeness workflows.

Preserve creative function, mood, genre, camera behavior, and story beat. Remove protected identity, exact look, trademarked costume, logo, named character, celebrity name, and studio/franchise label unless the user has a clearly authorized workflow.

Rewrite formula:
- protected identity -> original archetype
- brand/franchise/studio name -> production descriptors
- exact scene recreation -> new scene with similar dramatic function
- celebrity/public figure likeness -> fictional character or authorized portrait workflow

Safe examples:
- “an original masked acrobat hero swings through Tokyo” -> “an original masked acrobat hero swings between neon rooftops.”
- “soft hand-painted storybook animation style” -> “soft hand-painted storybook animation with warm natural light.”
- “Studio Trigger action” -> “bold ink outlines, flat color fills, high-contrast cel shading, smear frames.”

Return: risk diagnosis, removed items, preserved intent, safe rewritten prompt, and optional stricter rewrite.

Legacy details moved to `references/migrated/seedance-copyright-original.md`.
