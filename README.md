<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/hero-light.svg">
  <img alt="Seedance 2.0 Skill OS — intent-first quad-modal AI filmmaking" src="assets/hero-light.svg">
</picture>

# Seedance 2.0 Skill OS

**Intent-first AI filmmaking for Seedance 2.0.**

Text-to-video · Image-to-video · Video-to-video · Reference-to-video · Audio-aware prompting · Copyright-safe rewrites · Agent Skills

[![Version](https://img.shields.io/badge/version-5.3.0-111827?labelColor=0f172a)](#changelog)
[![Skills](https://img.shields.io/badge/sub--skills-23-0ea5e9?labelColor=0f172a)](#skill-map)
[![References](https://img.shields.io/badge/references-22-8b5cf6?labelColor=0f172a)](#reference-library)
[![Evals](https://img.shields.io/badge/evals-26-22c55e?labelColor=0f172a)](#validation)
[![License](https://img.shields.io/badge/license-MIT-f59e0b?labelColor=0f172a)](LICENSE)

Author: [Iamemily2050 (@iamemily2050)](https://github.com/Emily2040) · [Instagram](https://instagram.com/iamemily2050) · [X](https://x.com/iamemily2050) · [Website](https://iamemily2050.com)

Platform context: [ByteDance Seedance 2.0](https://seed.bytedance.com/en/seedance2_0) · [Dreamina](https://dreamina.capcut.com) · [Jimeng](https://jimeng.jianying.com) · [BytePlus ModelArk](https://docs.byteplus.com/en/docs/ModelArk/2291680)

Updated: **2026-05-08** · **v5.3.0 production-depth, multilingual, source, and eval coverage release**

---

## Why this repository exists

Seedance 2.0 Skill OS is a modular agent-skill package for directing Seedance 2.0 video generations. It is built around a simple principle: **direct the model, do not micro-manage the frame**.

The repository gives an AI assistant a public, auditable operating system for Seedance work. It defines when to interview, when to write a compact prompt, when to load a technical reference, when to rewrite unsafe IP content, and when to troubleshoot a bad generation.

## Start Here

| User situation | Load first | Output |
|---|---|---|
| “I have a vague idea.” | [`seedance-interview`](skills/seedance-interview/SKILL.md) | A focused creative brief and next prompt path. |
| “I know the scene I want.” | [`seedance-prompt`](skills/seedance-prompt/SKILL.md) | A production-ready Seedance prompt. |
| “Make it short and strong.” | [`seedance-prompt-short`](skills/seedance-prompt-short/SKILL.md) | A compressed 30–100 word prompt. |
| “I have an image/video/audio reference.” | [`reference-workflow`](references/reference-workflow.md) | A role map for every reference asset. |
| “It failed or looks bad.” | [`seedance-troubleshoot`](skills/seedance-troubleshoot/SKILL.md) | A root-cause diagnosis and repaired prompt. |
| “This uses a character, brand, celebrity, or real person.” | [`seedance-copyright`](skills/seedance-copyright/SKILL.md) | A safer rewrite preserving the creative function. |

## Current Status Rule

Seedance platform behavior changes quickly. Before making factual claims about API availability, face or portrait authorization, upload limits, pricing, regional availability, or model names, load [`references/api-status.md`](references/api-status.md) and check its `last_verified` date.

As of 2026-05-08, public official sources describe Seedance 2.0 as supporting text, image, audio, and video inputs, and BytePlus ModelArk publishes Seedance video-generation API documentation. Access, pricing, model IDs, upload limits, and authorization requirements remain surface-specific.

## Skill Map

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/skill-map.svg">
  <img alt="Seedance 2.0 skill constellation map" src="assets/skill-map.svg">
</picture>

### Core Pipeline

| Skill | Use when |
|---|---|
| [`seedance-interview`](skills/seedance-interview/SKILL.md) | The idea is vague, undeveloped, or needs creative direction. |
| [`seedance-interview-short`](skills/seedance-interview-short/SKILL.md) | The user wants a fast brief, not a long interview. |
| [`seedance-prompt`](skills/seedance-prompt/SKILL.md) | The user needs a complete prompt from a clear concept. |
| [`seedance-prompt-short`](skills/seedance-prompt-short/SKILL.md) | The prompt must be compressed for stronger Seedance performance. |
| [`seedance-camera`](skills/seedance-camera/SKILL.md) | Camera behavior, lens feel, shot scale, or movement must be specified. |
| [`seedance-motion`](skills/seedance-motion/SKILL.md) | Body movement, object motion, choreography, or physical action matters. |
| [`seedance-lighting`](skills/seedance-lighting/SKILL.md) | Mood, time of day, atmosphere, or light transition drives the shot. |
| [`seedance-characters`](skills/seedance-characters/SKILL.md) | Character identity, multi-character blocking, or consistency matters. |
| [`seedance-style`](skills/seedance-style/SKILL.md) | The user needs a visual style without unsafe studio/franchise borrowing. |
| [`seedance-vfx`](skills/seedance-vfx/SKILL.md) | Particles, destruction, energy, weather, magic, or transformation effects matter. |
| [`seedance-audio`](skills/seedance-audio/SKILL.md) | Dialogue, lip-sync, music, ambience, or audio-reference behavior matters. |
| [`seedance-pipeline`](skills/seedance-pipeline/SKILL.md) | The user asks about API, web workflow, ComfyUI, post-production, or integration. |
| [`seedance-recipes`](skills/seedance-recipes/SKILL.md) | The user wants a genre template or repeatable production recipe. |
| [`seedance-troubleshoot`](skills/seedance-troubleshoot/SKILL.md) | Output quality is poor, unstable, blurry, off-prompt, or blocked. |

### Governance and Quality

| Skill | Use when |
|---|---|
| [`seedance-copyright`](skills/seedance-copyright/SKILL.md) | Protected IP, public figures, real people, brands, logos, songs, or exact scenes appear. |
| [`seedance-antislop`](skills/seedance-antislop/SKILL.md) | Prompt language is generic, bloated, or filled with empty quality boosters. |
| [`seedance-filter`](skills/seedance-filter/SKILL.md) | A prompt is blocked, degraded, or likely to trigger a content filter. |

### Multilingual Vocabulary

| Skill | Use when |
|---|---|
| [`seedance-vocab-zh`](skills/seedance-vocab-zh/SKILL.md) | Chinese prompt compression or Mandarin cinematic vocabulary is needed. |
| [`seedance-vocab-ja`](skills/seedance-vocab-ja/SKILL.md) | Japanese cinematic vocabulary is needed. |
| [`seedance-vocab-ko`](skills/seedance-vocab-ko/SKILL.md) | Korean cinematic vocabulary is needed. |
| [`seedance-vocab-es`](skills/seedance-vocab-es/SKILL.md) | Spanish cinematic vocabulary is needed. |
| [`seedance-vocab-ru`](skills/seedance-vocab-ru/SKILL.md) | Russian cinematic vocabulary is needed. |
| [`seedance-examples-zh`](skills/seedance-examples-zh/SKILL.md) | Chinese working examples or example-safe rewrites are needed. |

## Reference Library

| Reference | Purpose |
|---|---|
| [`api-status.md`](references/api-status.md) | Current dated platform and API status. |
| [`source-registry.md`](references/source-registry.md) | Source hierarchy and evidence labels. |
| [`platform-constraints.md`](references/platform-constraints.md) | Stable platform-risk rules. |
| [`quick-ref.md`](references/quick-ref.md) | Compact routing and prompt checklist. |
| [`reference-workflow.md`](references/reference-workflow.md) | How to map image, video, audio, and storyboard references. |
| [`i2v-guide.md`](references/i2v-guide.md) | Image-to-video best practices. |
| [`prompt-examples.md`](references/prompt-examples.md) | Safe copy-paste prompt examples. |
| [`genre-guides.md`](references/genre-guides.md) | Genre-specific prompt patterns. |
| [`storytelling-framework.md`](references/storytelling-framework.md) | Narrative design and visual layering. |
| [`intent-vs-precision.md`](references/intent-vs-precision.md) | The intent-first philosophy. |
| [`audio-guide.md`](references/audio-guide.md) | Audio, dialogue, beat-sync, and lip-sync guidance. |
| [`anti-slop-lexicon.md`](references/anti-slop-lexicon.md) | Weak phrase replacement table. |
| [`filter-vocab.md`](references/filter-vocab.md) | Safer wording for blocked/degraded prompts. |
| [`frontend-design-system.md`](references/frontend-design-system.md) | README and SVG design standards. |
| [`json-schema.md`](references/json-schema.md) | Structured prompt wrapper for pipelines. |
| [`eval-rubric.md`](references/eval-rubric.md) | How to judge eval outputs. |
| [`progressive-disclosure.md`](references/progressive-disclosure.md) | Root, sub-skill, and reference boundaries. |
| [`vocab/zh.md`](references/vocab/zh.md) | Chinese cinematic vocabulary for compact prompts. |
| [`vocab/ja.md`](references/vocab/ja.md) | Japanese cinematic vocabulary for compact prompts. |
| [`vocab/ko.md`](references/vocab/ko.md) | Korean cinematic vocabulary for compact prompts. |
| [`vocab/es.md`](references/vocab/es.md) | Spanish cinematic vocabulary for compact prompts. |
| [`vocab/ru.md`](references/vocab/ru.md) | Russian cinematic vocabulary for compact prompts. |

## Install

Client support for Agent Skills is still tool-specific. If your client supports installing a skill directly from a GitHub repository, use this repository URL:

```text
https://github.com/Emily2040/seedance-2.0
```

For manual installation, copy this repository into the skill directory used by your agent client. The directory name should match the root skill name, `seedance-20`.

| Platform | Typical workspace path |
|---|---|
| Claude Code / OpenClaw | `.claude/skills/seedance-20/` |
| Codex-style agent workspace | `.agents/skills/seedance-20/` |
| Gemini CLI-style workspace | `.gemini/skills/seedance-20/` |
| GitHub Copilot workspace | `.github/skills/seedance-20/` |
| Cursor workspace | `.cursor/skills/seedance-20/` |
| Windsurf workspace | `.windsurf/skills/seedance-20/` |

## Validation

Run these checks before every release:

```bash
python scripts/validate_skills.py --strict
python scripts/content_audit.py --strict
python scripts/eval_schema_check.py --strict
python scripts/design_audit.py --strict
```

The CI workflow runs the same checks on push and pull request.

## Design Standard

The v5.3 frontend intentionally keeps the cleaned v5.2 design language while adding deeper production guidance, multilingual coverage, and eval breadth. The README should stay readable in GitHub mobile, dark mode, and narrow widths. SVG assets must include `<title>` and `<desc>` elements, use internal CSS only, and avoid external fonts or scripts. See [`docs/frontend-redesign.md`](docs/frontend-redesign.md).

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md). Current release: **v5.3.0**.

## License

MIT © 2026 Iamemily2050 (@iamemily2050)
