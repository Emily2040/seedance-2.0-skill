---
name: seedance-pipeline
description: "This skill should be used when the user asks about Seedance 2.0 workflow operations, API planning, BytePlus ModelArk, Dreamina/Jimeng surfaces, ComfyUI, post-production, stitching, batch workflow, or integration planning."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - workflow
  - api
  - integration
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


# seedance-pipeline

Use this for operational workflows, APIs, web surfaces, post-production, and integration planning.

## Status Rule

Always load `[ref:api-status]` for current API and platform claims. Do not rely on old release-status memory.

## Workflow Split

1. Web workflow: Dreamina/Jimeng surface, references, prompt, output review.
2. API workflow: BytePlus/ModelArk docs, model ID, auth, file handling, task creation, task retrieval.
3. Post workflow: stitching, audio cleanup, captions, color, upscale, delivery.
4. Community workflow: ComfyUI or unofficial nodes must be labeled community/unverified unless sourced.

## Output Contract

Return the workflow path, source status, required inputs, validation steps, and risks.
