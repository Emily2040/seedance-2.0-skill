---
name: seedance-lighting
description: "This skill should be used when the user asks for lighting design, atmosphere, time of day, color temperature, shadow, reflections, weather light, practical lights, or mood transitions in Seedance 2.0."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - lighting
  - atmosphere
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


# seedance-lighting

Lighting should describe sources and transitions, not abstract beauty.

## Lighting Contract

State: key source, direction, color temperature, atmosphere, shadow behavior, and any transition.

Good: `warm practical lamp from frame left, blue moonlight rim on the shoulders, dust visible in the beam`.

## Output Contract

Return a compact lighting block and one prompt-ready integrated sentence.
