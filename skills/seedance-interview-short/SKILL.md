---
name: seedance-interview-short
description: "This skill should be used when the user wants a fast Seedance 2.0 creative brief, a short interview, a compressed intake flow, or a quick director-style clarification before prompt writing."
license: MIT
user-invocable: true
tags:
  - creative-direction
  - brief
  - compression
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

# seedance-interview-short

Use this when speed matters more than exhaustive creative discovery. The goal is to turn a vague idea into a compact director brief with no more than three questions, then route to prompt writing.

## Process

Ask at most three questions, and only ask them if the answer materially changes the prompt. Prioritize:

1. What is the subject doing, and what changes by the final frame?
2. What should it feel like: product polish, drama, comedy, realism, animation, action, or atmosphere?
3. Are there image, video, or audio references, and what should each one control?

If the user already supplied enough information, do not ask. Produce a brief immediately.

## Compact Brief Pattern

`Mode: [T2V/I2V/V2V/R2V]. Subject: [anchor]. Beat: [before -> action -> final state]. Camera: [one move]. Light/style: [physical source and safe descriptor]. Sound: [dialogue/ambience/SFX/music/silence]. Constraints: [identity, IP, safety, product, prompt budget].`

## Routing Rule

Route to `[skill:seedance-prompt]` for a full production prompt, `[skill:seedance-prompt-short]` for a compact prompt, `[skill:seedance-copyright]` for IP/likeness risk, or `[skill:seedance-troubleshoot]` when the user starts from a bad result.

## Output Contract

Return one compact brief under 150 words, any missing high-impact question, and a recommended skill route.
