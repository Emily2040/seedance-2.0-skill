---
name: seedance-20
description: 'Generate and direct cinematic AI videos with Seedance 2.0 (ByteDance/Dreamina/Jimeng). Covers text-to-video, image-to-video, video-to-video, and reference-to-video workflows with @Tag asset references, multi-character scenes, audio design, and post-processing. Use when making AI video, writing Seedance prompts, directing a scene, fixing generation errors, or building an AI short film, product ad, or music video.'
license: MIT
user-invocable: true
user-invokable: true
tags: ["ai-video", "filmmaking", "bytedance", "seedance", "multimodal", "lip-sync", "openclaw", "antigravity", "gemini-cli", "firebase", "codex", "cursor", "windsurf", "opencode"]
metadata: {"version": "5.0.0", "updated": "2026-03-03", "openclaw": {"emoji": "🎬", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "antigravity": {"emoji": "🎬", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "gemini-cli": {"emoji": "🎬", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "firebase": {"emoji": "🎬", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "author": "Emily (@iamemily2050)", "repository": "https://github.com/Emily2040/seedance-2.0"}
---

# seedance-20

Seedance 2.0 quad-modal AI filmmaking (T2V · I2V · V2V · R2V).

## The v5.0 Philosophy

> **Direct the model. Don't micro-manage it.** Tell it WHAT you want and HOW it should FEEL, not every pixel of HOW to execute it. Use @references to show, not tell.

This library offers two workflows:

1. **Full Interview**: For users with a vague idea who need creative guidance. Start with [skill:seedance-interview].
2. **Direct Prompt**: For users who know what they want. Start with [skill:seedance-prompt].

> **Note (Feb 2026):** Seedance V2 currently performs best with short (<2000 char) Chinese prompts.

> **Feb 2026 Status**: Seedance 2.0 API global release was delayed (from planned Feb 24) due to copyright enforcement actions by Disney, Paramount Skydance, Netflix, MPA, and SAG-AFTRA. ByteDance paused real-person face uploads Feb 15. Content filters for named franchise characters, anime IPs, and streaming originals have been tightened. The [skill:seedance-copyright] module reflects the current post-enforcement state. Run it before every generation.


## Platform Compatibility

| Platform | Install path | Scope |
|---|---|---|
| **Antigravity** | `.agent/skills/seedance-20/` | workspace |
| **Gemini CLI** | `.gemini/skills/seedance-20/` | workspace |
| **Firebase Studio** | `.idx/skills/seedance-20/` | workspace |
| **Claude Code** | `.claude/skills/seedance-20/` | workspace |
| **OpenClaw / ClawHub** | `.claude/skills/seedance-20/` | workspace |
| **GitHub Copilot** | `.github/skills/seedance-20/` | workspace |
| **Codex** | `.agents/skills/seedance-20/` | workspace |
| **Cursor** | `.cursor/skills/seedance-20/` | workspace |
| **Windsurf** | `.windsurf/skills/seedance-20/` | workspace |
| **OpenCode** | `.opencode/skills/seedance-20/` | workspace |

### One-liner installs

```bash
# Antigravity / Gemini CLI / Firebase Studio
antigravity skills install https://github.com/Emily2040/seedance-2.0
gemini skills install https://github.com/Emily2040/seedance-2.0
# Claude Code / OpenClaw
claude skills install https://github.com/Emily2040/seedance-2.0
# Codex
codex skills install https://github.com/Emily2040/seedance-2.0
# Cursor
cursor skills install https://github.com/Emily2040/seedance-2.0
# Windsurf
windsurf skills install https://github.com/Emily2040/seedance-2.0
# OpenCode
opencode skills install https://github.com/Emily2040/seedance-2.0
```

## Skills

**Core pipeline**
[skill:seedance-interview] / [skill:seedance-interview-short] · [skill:seedance-prompt] / [skill:seedance-prompt-short] · [skill:seedance-camera] · [skill:seedance-motion] · [skill:seedance-lighting] · [skill:seedance-characters] · [skill:seedance-style] · [skill:seedance-vfx] · [skill:seedance-audio] · [skill:seedance-pipeline] · [skill:seedance-recipes] · [skill:seedance-troubleshoot]

**Content quality**
[skill:seedance-copyright] · [skill:seedance-antislop] · [skill:seedance-filter]

**Vocabulary**
[skill:seedance-vocab-zh] · [skill:seedance-vocab-ja] · [skill:seedance-vocab-ko] · [skill:seedance-vocab-es] · [skill:seedance-vocab-ru]

**Working Examples**
[skill:seedance-examples-zh]

## References

[ref:platform-constraints] · [ref:json-schema] · [ref:prompt-examples] · [ref:quick-ref] · [ref:storytelling-framework] · [ref:genre-guides] · [ref:reference-workflow] · [ref:i2v-guide] · [ref:intent-vs-precision]

## Version history

| Version | Date | Changes |
|---|---|---|
| 5.0.0 | 2026-03-03 | **Intent-First Overhaul.** Rewrote seedance-prompt (genre router, 30-100 word target, I2V gate). Restructured seedance-motion (intent-first, @Video reference primary). Updated seedance-camera (One-Move Rule, genre presets). Updated seedance-recipes (7 genre categories). Updated seedance-interview (Quick Mode exit, genre detection). Updated seedance-troubleshoot (diagnostic tree). Added 4 new references: genre-guides, reference-workflow, i2v-guide, intent-vs-precision. Minor updates to seedance-prompt-short, seedance-style, seedance-vfx, seedance-audio. |
| 4.2.0 | 2026-03-03 | Safe Vocabulary Integration: added filter-safe action, weapon, clothing, body, environment, material, VFX, sound, and production-context terms to seedance-filter and all 5 language vocabulary skills (zh, ja, ko, es, ru). Term counts: zh 550+, ja/ko/es/ru 450+ each. |
| 4.1.0 | 2026-03-02 | Added seedance-filter: content filter intelligence, 37% block-rate diagnosis, four-question framework, safe-prompting techniques. |
| 4.0.0 | 2026-02-28 | Cognitive Architecture upgrade: L8 Construction-First interview, L7 Concealment Check prompt, L11 Conservation Law troubleshoot. Inspired by agi-in-md cognitive compression. |
| 3.8.0 | 2026-02-27 | Dual Workflow System: Max Detail + Max Performance. Added seedance-prompt-short and seedance-interview-short. |
| 3.7.0 | 2026-02-26 | Redesigned seedance-interview as "Director's Journey" with 5-stage storytelling workflow. Added storytelling-framework reference. |
| 3.6.1 | 2026-02-26 | Enhanced vocab-zh (400+ terms, 16 categories). Added seedance-examples-zh with 16 battle-tested Chinese prompts across 7 genres. |
| 3.3.0 | 2026-02-25 | Rewrote seedance-interview v4.0: A/B/C/D/E guided stages, 5-flow types (image/video/audio/one-liner/script), 3-option prompt output, language selection |
| 3.2.1 | 2026-02-25 | **Accuracy corrections**: removed negative-prompt support claim (not supported), corrected API availability (no public API yet), fixed aspect ratios (added 3:4 and 21:9), fixed video input limit (15s combined not per-file), removed mobile-only duration claim |
| 3.1.0 | 2026-02-25 | Added copyright, antislop, vocab-ja/ko/es/ru modules. 24 files. |
| 3.0.0 | 2026-02-25 | Initial 12-skill core pipeline. |
