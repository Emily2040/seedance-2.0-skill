---
name: seedance-audio
description: "This skill should be used when the user asks for Seedance 2.0 audio, dialogue, lip-sync, music, sound effects, ambience, beat-sync, audio-reference mapping, desync troubleshooting, or sound-driven visual timing."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - audio
  - lip-sync
  - dialogue
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


# seedance-audio

Use this for dialogue, lip-sync, sound layers, music, ambience, and audio reference behavior.

## Core Rules

- Keep dialogue short.
- Put spoken lines in quotes.
- Assign every line to a speaker.
- Prefer locked or stable framing for lip-sync.
- Remove head-turning and face-motion tokens when mouth accuracy matters.
- Treat `[Audio1]` as a reference unless the active platform documents exact playback behavior.

Load `[ref:audio-guide]` for detailed constraints, beat-sync, desync repair, and multi-character workarounds.

## Output Contract

Return speaker map, dialogue, sound layer, audio reference role, and lip-sync constraints.
