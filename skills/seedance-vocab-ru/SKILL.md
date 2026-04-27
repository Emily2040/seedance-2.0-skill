---
name: seedance-vocab-ru
description: "This skill should be used when the user asks for Russian Seedance 2.0 prompt wording, Russian cinematic vocabulary, Russian prompt compression, or translation of camera, lighting, action, VFX, audio, or production terms into Russian."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - video-generation
  - vocab
  - ru
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

# seedance-vocab-ru

Use this skill for Russian Seedance 2.0 prompt wording and cinematic vocabulary. Keep active skill guidance lean; extended legacy term lists were moved to `references/migrated/seedance-vocab-ru-original.md`.

Rules:
- Translate production intent, not word-for-word English filler.
- Preserve reference tags exactly: `[Image1]`, `[Video1]`, `[Audio1]`.
- Preserve concrete nouns, action verbs, camera moves, light sources, and sound cues before style adjectives.
- Avoid protected names, studio names, celebrity names, and brand names unless the workflow is authorized.

Return: compact Russian prompt, optional English back-translation, key vocabulary choices, and safety/IP notes if relevant.
