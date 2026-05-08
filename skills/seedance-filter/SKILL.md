---
name: seedance-filter
description: "This skill should be used when a Seedance 2.0 prompt is blocked, rejected, silently degraded, or likely to trigger a content filter; or when the user asks for a safer rewrite without losing the creative intent."
license: MIT
user-invocable: true
tags:
  - content-filter
  - safe-rewrite
  - seedance-20
metadata:
  version: "5.3.0"
  updated: "2026-05-08"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-filter

Use this when a prompt is blocked, degraded, likely to trigger moderation, or needs a safer rewrite without losing creative intent. This skill does not help evade safety systems. It rewrites risky surface wording into professional, non-graphic production language and preserves the safe creative core.

## Repair Method

1. Identify the creative intent: action, mood, camera, subject, and final beat.
2. Identify risky surface wording: graphic harm, protected identity, sexualized framing, real-person likeness, weapons, self-harm, hate, evasion language, or exact IP copying.
3. Replace risky terms with professional, non-graphic, production-context language.
4. Preserve composition, action, mood, camera logic, and authorized references.
5. Do not help bypass safety systems or provide evasion tactics.

## Safer Rewrite Patterns

| Intent | Safer direction |
|---|---|
| Conflict | `staged confrontation, choreographed action beat, no graphic injury` |
| Aftermath | `non-graphic distress, torn fabric, scattered props, dramatic silence` |
| Suspense | `threat implied by shadow, locked door, heavy breathing, low light` |
| Weapon-like prop | `prop object handled safely within a staged action scene` |
| Horror mood | `eerie atmosphere, flickering practical light, off-screen sound cue` |
| Protected identity | `original character with broad genre archetype traits` |

## Boundary Rule

If the user's request is unsafe, refuse or redirect to a safe alternative. If it is safe but poorly worded, repair the wording. When uncertain, state the risk class and offer a conservative prompt that keeps the non-harmful scene function.

Load `[ref:filter-vocab]` for safer substitutions.

## Output Contract

Return likely trigger class, safer wording, final prompt, what changed, and any content boundary that still applies.
