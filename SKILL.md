---
name: seedance-20
description: "This skill should be used when the user needs Seedance 2.0 AI-video workflows: T2V, I2V, V2V, R2V, audio, character consistency, camera, lighting, VFX, prompt compression, safe rewrites, filter recovery, or platform/API planning."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - ai-video
  - filmmaking
  - bytedance
  - seedance
  - multimodal
  - agent-skills
metadata:
  version: "5.2.0"
  updated: "2026-05-08"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-20

Intent-first Seedance 2.0 router. Direct with subject, action, camera, lighting, references, audio, and constraints.

## Load

| Need | Load |
|---|---|
| Vague idea | `[skill:seedance-interview]` |
| Fast brief | `[skill:seedance-interview-short]` |
| Clear scene/references | `[skill:seedance-prompt]` |
| Compressed prompt | `[skill:seedance-prompt-short]` plus vocabulary skill |
| I2V | `[ref:i2v-guide]` |
| R2V/V2V | `[ref:reference-workflow]` |
| Craft detail | Matching specialist skill |
| Bad output | `[skill:seedance-troubleshoot]` |
| IP, celebrity, real-person, voice, or likeness risk | `[skill:seedance-copyright]` |
| Blocked prompt | `[skill:seedance-filter]` |
| Platform/API | `[skill:seedance-pipeline]` plus `[ref:api-status]` |

Before API, pricing, upload-limit, model-ID, portrait, or region claims, load `[ref:api-status]`.

## Prompt Rules

Use reference tags before adjectives. Use one main camera move unless asked otherwise. Assign multi-character actions to named tags. For I2V, add motion instead of static details. Replace hollow boosters with observable production language. Rewrite protected IP and real-person content unless clearly authorized.
