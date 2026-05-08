---
name: seedance-interview
description: "This skill should be used when the user has a vague Seedance 2.0 video idea and asks for creative guidance, story development, scene planning, a director interview, or help turning an undeveloped concept into a production-ready prompt."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - creative-direction
  - interview
  - brief
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


# seedance-interview

Use this as the full director interview when the user has a rough idea rather than a ready scene.

## Process

1. Build a safe draft premise immediately from the user input.
2. Ask only the missing questions that materially affect the prompt: subject, action, reference assets, camera feel, emotional direction, duration, and risk constraints.
3. Identify the genre path: product, lifestyle, drama, music video, landscape, commercial, animation, UGC, or experimental.
4. End with a concise creative brief and route to `[skill:seedance-prompt]` or `[skill:seedance-prompt-short]`.

## Output Contract

Return: concept summary, reference asset request, core scene, mood, camera intent, sound intent, safety notes, and next prompt path.

Do not ask a long questionnaire when the user already supplied enough information to write the prompt.
