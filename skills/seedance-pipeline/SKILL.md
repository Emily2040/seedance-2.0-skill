---
name: seedance-pipeline
description: "This skill should be used when the user asks how to run Seedance 2.0 through a web workflow, official API, BytePlus/Volcengine ModelArk, ComfyUI, Firebase Studio, third-party integration, post-processing chain, or production pipeline."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - pipeline
  - api
  - byteplus
  - volcengine
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

# seedance-pipeline

Use this skill for web UI, official API, BytePlus/Volcengine ModelArk, ComfyUI/community nodes, third-party surfaces, and post-production chains.

First rule: always check `[ref:api-status]` before giving API, pricing, upload-limit, face/portrait, or regional-availability advice. Do not repeat stale Feb. 2026 API-delay claims.

Workflow split:
- Creator/web workflow: prompt, upload references, iterate manually.
- Official API workflow: use current BytePlus/ModelArk docs; avoid hardcoding endpoints unless docs are loaded.
- Third-party workflow: label as unofficial or third-party and warn that pricing/limits/safety may diverge.
- Post-production workflow: edit, upscale, interpolate, mix sound, subtitle, and assemble shots.

Return: recommended surface, required assets, prompt mode, operational steps, verification checks, safety/IP checks, and fallback plan.

Legacy details moved to `references/migrated/seedance-pipeline-original.md`.
