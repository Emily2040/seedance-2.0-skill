---
name: seedance-camera
description: "This skill should be used when the user asks for camera movement, shot scale, lens feel, framing, one-take direction, dolly, pan, tilt, push-in, handheld, aerial, macro, or camera-transfer guidance for Seedance 2.0."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - camera
  - cinematography
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


# seedance-camera

Use one clear camera idea per short clip unless the user asks for a multi-shot sequence.

## Camera Contract

State: shot scale, movement, speed, subject relationship, and endpoint.

Good: `slow dolly-in from medium shot to tight close-up as the character realizes the truth`.

Weak: `cinematic dynamic camera movement`.

## Conflict Rule

If the user gives several incompatible moves, choose one primary camera move and put the rest into optional variants.

## Output Contract

Return the camera phrase, reason, and a prompt-ready version.
