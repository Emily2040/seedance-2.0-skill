---
name: seedance-vfx
description: "This skill should be used when the user asks for VFX, particles, energy, destruction, transformation, weather effects, magical effects, explosions, smoke, fire, water, or physically plausible effects in Seedance 2.0."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - vfx
  - particles
  - effects
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


# seedance-vfx

VFX prompts need material behavior, source, timing, and consequence.

## Effects Contract

State: effect source, material, motion, interaction with light, interaction with objects, dissipation, and endpoint.

Good: `gold dust particles spiral from the logo, catch the backlight, then settle onto the table surface`.

## Output Contract

Return the VFX contract and a compact prompt-ready phrase.
