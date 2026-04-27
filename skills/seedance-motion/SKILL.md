---
name: seedance-motion
description: "This skill should be used when the user asks for action choreography, body movement, physics, animation timing, performance motion, video-reference motion transfer, dance, fight, vehicle movement, or dynamic scene control in Seedance 2.0."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - video-generation
  - motion
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

# seedance-motion · Intent-First Choreography (v5.0)

This skill covers motion control, action choreography, and video extension for Seedance 2.0, prioritizing intent-driven descriptions over micro-management.

## The Guiding Philosophy

> For action, describe the **intent** and **consequence**, not the precise timestamps. Let the AI director handle the interpolation.

---

## 1. The Recommended Workflow: Intent + @Video Reference

This is the most reliable method for all action and fight scenes.

### Step 1: Find a Reference Video

Find a real-world video clip (e.g., from a movie, a stunt performance, or a video game) that captures the style of action you want. Upload it as `@Video1`.

### Step 2: Write an Intent-Based Prompt

Describe the high-level action in 1-3 sentences. Use degree adverbs and physics consequences. Then, explicitly tell the model to reference the uploaded video.

```
// Recommended Prompt Structure

Characters: A references @Image1; B references @Image2.

Choreography: The archer fires two arrows; the mage deflects them with a violet energy shield, then closes distance and blasts the archer into a tree with a shockwave. The archer draws a short blade and counter-attacks in close combat.

Reference: Reference the fight actions, character movements, and camera work from @Video1.

Style: Match the gritty, handheld style of @Video1.
```

**Why this works:** The `@Video1` reference provides the model with a rich, dense, and unambiguous understanding of the desired motion, physics, and camera language, which consistently outperforms any text-only description.

*For more on the @reference system, see [ref:reference-workflow].*

---

## 2. The Text-Only Workflow: Intent-Based Description

Use this when you don't have a reference video. The key is to keep it simple and enforce the **"One Action Per Shot"** rule.

```
// Text-Only Fight Scene Example

Characters: A references @Image1; B references @Image2.

Shot 1: A throws a right hook at B's jaw.
Shot 2: B ducks under the punch and sweeps A's legs.
Shot 3: A jumps, landing a spinning back kick to B's shoulder.
Shot 4: B staggers backward two steps, recovering his balance.

Camera: Medium shot, tracking the action. Slight handheld shake on impacts.
Physics: Dust puffs up from the ground on the leg sweep. A wet impact sound accompanies each hit.
```

### Key Principles for Text-Only Action

- **One Action Per Shot:** Do not chain multiple distinct actions (e.g., punch, block, kick) into a single sentence or shot. Break them down.
- **Degree Adverbs:** Use words like `violently`, `gracefully`, `slowly`, `frantically` to guide the model's interpretation of the action.
- **Physics Consequences:** Describe the results of the action. `Dust erupts`, `sparks fly`, `water sprays`, `the character staggers`.

---

## 3. Experimental Workflow: Micro-Choreography

> **⚠️ Warning:** This is an advanced, experimental technique that is unreliable for most users and often results in jitter, morphing, and failed generations. Use the Intent-Based workflows above for production.

Micro-choreography involves specifying actions with timestamps or in a grid format. While it offers the highest potential for control, it is also the most likely to fail.

### The Grid Method (25宫格)

| Beat | Camera | Action | SFX |
| :--- | :--- | :--- | :--- |
| 1 | Full shot, locked | B right punch → A face | drum "dong" + wind |
| 2 | Close-up | A crossguard block | impact "peng" |
| 3 | Medium | A wrist flip counter | ground crack |

### Timestamp Method

`0-1s: A throws a punch. 1-2s: B blocks. 2-3s: A follows with a kick.`

**When to use:** Only for short, highly technical sequences where the exact timing of each beat is critical and you are prepared to iterate many times to get a usable result.

---

## Diagnostic Tools

Use these concepts to diagnose failing motion prompts, not as prescriptive rules for building them.

- **Beat Density:** If your output is blurry or jittery, you may have too many actions packed into a short duration. The model can typically handle 1-2 distinct beats every 5 seconds. High-density prompts require the experimental micro-choreography format.
- **Timing Language:** Use relative terms (`eases in over 2 seconds`) or descriptive adverbs (`accelerates into a run`) instead of hard timestamps for smoother, more natural motion.

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
