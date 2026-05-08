---
name: seedance-troubleshoot
description: "This skill should be used when a Seedance 2.0 output is blurry, jittery, off-prompt, morphing, blocked, visually generic, unstable, desynced, inconsistent, or otherwise fails and needs root-cause diagnosis."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - diagnostics
  - troubleshooting
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


# seedance-troubleshoot

Diagnose failure before rewriting.

## Diagnostic Tree

1. Mode mismatch: T2V/I2V/V2V/R2V prompt is using the wrong assumptions.
2. Overload: too many actions, characters, camera moves, or style anchors.
3. Ambiguity: unclear subject, pronouns, reference roles, or timing.
4. Unsupported or volatile platform behavior.
5. Safety/filter/IP conflict.

## Output Contract

Return root cause, evidence from the prompt, repaired prompt, and one conservative retry variant.
