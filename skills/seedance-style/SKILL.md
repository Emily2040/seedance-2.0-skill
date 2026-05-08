---
name: seedance-style
description: "This skill should be used when the user asks for visual style, art direction, render feel, period aesthetic, texture, animation style, realism level, or style-safe alternatives to studio or franchise references."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - style
  - art-direction
  - ip-safe
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


# seedance-style

Translate style requests into production descriptors.

## Style Safety Rule

Do not use studio, franchise, artist, or living-creator names as style anchors unless the user has a clearly authorized workflow. Preserve the intended visual function by describing medium, texture, palette, lighting, composition, and era.

Example replacement: `hand-painted 2D animation, soft watercolor backgrounds, gentle rounded character shapes, low-contrast pastel palette`.

## Output Contract

Return a safe style descriptor and one integrated prompt sentence.
