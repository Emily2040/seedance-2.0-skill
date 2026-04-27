---
name: seedance-audio
description: "This skill should be used when the user asks for native audio, dialogue, lip-sync, voice, sound effects, music timing, beat sync, ambient sound, audio references, or audio-video synchronization in Seedance 2.0."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - audio
  - lip-sync
  - sound-design
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

# seedance-audio

Use this skill for dialogue, lip-sync, music timing, sound effects, ambient sound, and audio-reference planning.

Return: audio goal, speaker/source assignment, prompt-ready wording, sync constraints, risk notes, and retry variant.

Rules:
- Keep spoken lines short and assign each line to a specific character.
- Separate dialogue, ambience, SFX, and music.
- Map references by role: `[Audio1] rhythm`, `[Audio2] voice tone`, `[Audio3] ambience`.
- Do not claim universal language, duration, or voice-cloning support. Check `[ref:api-status]`.
- Real-person voices and likeness workflows require authorization and platform-specific support.

Prompt pattern: `[Character A] says: "short line." Quiet [environment ambience], [specific SFX], [music/rhythm cue]. Lip movement synchronized to the spoken line; camera and body motion remain simple enough to preserve sync.`

Legacy details moved to `references/migrated/seedance-audio-original.md`.
