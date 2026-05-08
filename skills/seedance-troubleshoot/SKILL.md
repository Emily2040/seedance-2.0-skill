---
name: seedance-troubleshoot
description: "This skill should be used when a Seedance 2.0 output is blurry, jittery, off-prompt, morphing, blocked, visually generic, unstable, desynced, inconsistent, or otherwise fails and needs root-cause diagnosis."
license: MIT
user-invocable: true
tags:
  - diagnostics
  - troubleshooting
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

# seedance-troubleshoot

Diagnose failure before rewriting. Do not simply add more adjectives. Identify whether the failure came from mode mismatch, overload, ambiguity, fragile identity, unsafe wording, unsupported platform behavior, or missing preservation constraints.

## Diagnostic Tree

| Symptom | Likely cause | First repair |
|---|---|---|
| Product or face changes | I2V prompt re-described visible identity or overloaded motion. | Add preservation constraints; remove duplicate static detail. |
| Camera jumps | Several incompatible moves or no endpoint. | Choose one move with start and finish. |
| Generic output | Hollow style words and weak action. | Replace with physical action, source light, material, and sound. |
| Motion ignored | Static prompt or no visible consequence. | Add actor, verb, timing, and changed end state. |
| Lip-sync poor | Moving head/camera, long dialogue, unassigned speaker. | Lock framing, shorten line, assign speaker. |
| VFX noisy | Effect has no source, physics, or dissipation. | Add source, material, path, interaction, and endpoint. |
| Prompt blocked | Protected IP, real-person, graphic, or bypass-like wording. | Rewrite intent in safe production language without evasion. |

## Repair Process

First quote the failing phrase or missing element. Then name the root cause. Next, remove conflicts rather than adding complexity. Finally, produce one conservative retry prompt and one optional creative variant only if the user wants exploration.

## Conservative Retry Pattern

`[Reference role if any]. Preserve [identity/product/environment] exactly. One visible action: [specific verb and consequence]. Camera: [single move]. Lighting: [physical source]. Sound: [ambient/SFX/dialogue]. Constraints: [what must not change].`

## Escalation Rules

If the same error repeats, split the scene into shorter clips, reduce characters, simplify hand or face motion, use stronger reference role mapping, or change the mode. For unstable text/logos, keep them static, centered, and protected; do not ask the model to redraw small text during motion.

## Output Contract

Return root cause, evidence from the prompt or result, repaired prompt, and one conservative retry variant.
