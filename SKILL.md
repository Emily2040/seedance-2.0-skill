---
name: seedance-20
description: "This skill should be used when the user asks to create, direct, improve, troubleshoot, or operationalize Seedance 2.0 AI-video workflows, including text-to-video, image-to-video, video-to-video, reference-to-video, audio/lip-sync, character consistency, camera motion, lighting, VFX, prompt compression, copyright-safe rewrites, or platform/API planning."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - ai-video
  - filmmaking
  - bytedance
  - seedance
  - multimodal
  - lip-sync
  - agent-skills
metadata:
  version: "5.1.0"
  updated: "2026-04-27"
  author: "Emily (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: ""
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-20

Seedance 2.0 quad-modal AI filmmaking skill for text-to-video, image-to-video, video-to-video, and reference-to-video workflows.

## Operating Principle

Direct the model. Do not micro-manage it. State the intended subject, action, feeling, camera behavior, lighting logic, reference roles, audio layer, and constraints. Use references to show what should be preserved; use text to say what should change.

## Workflow Router

- Vague idea, concept only, or no clear scene: load `[skill:seedance-interview]`.
- Clear concept or reference assets supplied: load `[skill:seedance-prompt]`.
- Need short Chinese prompt or prompt compression: load `[skill:seedance-prompt-short]` and the relevant vocabulary skill.
- Image-to-video: load `[ref:i2v-guide]` and describe only what the image cannot show.
- Video/reference-to-video: load `[ref:reference-workflow]`; map each reference to a role.
- Camera, motion, lighting, character, style, VFX, or audio specialization: load only the matching sub-skill.
- Bad output: load `[skill:seedance-troubleshoot]`; then load the specific failure-area skill.
- Copyright, celebrity, brand, franchise, real-person, or likeness risk: load `[skill:seedance-copyright]` before finalizing.
- Blocked or degraded prompt: load `[skill:seedance-filter]` and preserve intent while changing risky surface wording.
- Platform/API/integration questions: load `[skill:seedance-pipeline]` plus `[ref:api-status]`.

## Current Platform Status Rule

Platform status changes quickly. For API availability, upload limits, face/portrait authorization, pricing, and regional access, do not rely on static memory. Load `[ref:api-status]` and check its `last_verified` date. As of 2026-04-27, official ByteDance/BytePlus sources describe Seedance 2.0 as supporting text plus image, audio, and video references, and BytePlus ModelArk publishes video generation API documentation. Real-person likeness workflows remain authorization-dependent and surface-specific.

## Prompt Construction Rules

1. Preserve reference tags before adjectives: `[Image1]` identity, `[Video1]` motion, `[Audio1]` rhythm or voice.
2. Use one primary camera move per short clip unless the user requests a multi-shot sequence.
3. For multi-character scenes, assign actions to named character tags. Avoid ambiguous pronouns.
4. For I2V, do not re-describe visible static details. Add motion, camera, timing, transformation, lighting change, and audio.
5. Remove hollow quality boosters. Prefer physical, observable, production-specific language.
6. Rewrite protected IP, celebrity, brand, and real-person content into original archetypes unless the user supplies a clearly authorized workflow.

## References

Load references selectively: `[ref:api-status]`, `[ref:platform-constraints]`, `[ref:json-schema]`, `[ref:prompt-examples]`, `[ref:quick-ref]`, `[ref:storytelling-framework]`, `[ref:genre-guides]`, `[ref:reference-workflow]`, `[ref:i2v-guide]`, `[ref:intent-vs-precision]`, `[ref:source-registry]`.
