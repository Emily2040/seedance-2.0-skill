---
name: seedance-prompt
description: "This skill should be used when the user asks to write, improve, compress, translate, or debug a Seedance 2.0 video prompt; mentions text-to-video, image-to-video, reference-to-video, camera direction, prompt quality, or a direct generation prompt; or provides reference assets and wants a production-ready Seedance prompt."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - video-generation
  - prompt
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

# seedance-prompt · The Director\'s Formula (v5.0)

This skill translates a user\'s creative vision into a production-ready prompt for Seedance 2.0. It uses a genre-aware, intent-driven workflow based on community-proven best practices.

## The Governing Philosophy

> Seedance 2.0 is an AI director. Tell it **WHAT** you want and **HOW** it should **FEEL**, not every micro-detail of **HOW** to execute it. Trust the model.

## The Director\'s Formula

All prompts should follow this structure. The default target length is **30–100 words**.

`[Subject] + [Action] + [Scene] + [Camera] + [Style] + [Constraints]`

---

## The Workflow

### 1. Genre Router

First, ask the user to identify their content category. This determines the prompt\'s skeleton, length, and emphasis.

| Genre | Lead With | Length Target | Key Sections |
| :--- | :--- | :--- | :--- |
| **Product/E-commerce** | Subject | 30-50 words | Subject, Camera, Style |
| **Lifestyle/Social** | Action | 40-60 words | Action, Scene, Style |
| **Drama/Narrative** | Scene | 60-100 words | Scene, Action, Camera |
| **Music Video** | Style | 50-80 words | Style, Action, Camera |
| **Landscape/Travel** | Scene | 30-60 words | Scene, Camera, Style |
| **Commercial/Brand** | Style | 40-70 words | Style, Scene, Action |
| **Anime/Artistic** | Style | 50-90 words | Style, Action, Scene |
| **UGC (User-Generated)** | Action | 20-40 words | Action, Scene, Camera (handheld) |

*For detailed templates per genre, see [ref:genre-guides].*

### 2. I2V vs. T2V Gate

Ask if the user has reference images. This fundamentally changes the prompt.

- **If YES (I2V Mode):** The prompt should **only describe motion and camera movement.** Do not re-describe static visual elements that the model can already see in the image.
- **If NO (T2V Mode):** The prompt must describe all visual elements from scratch.

*For detailed I2V guidance, see [ref:i2v-guide].*

### 3. Build with the Formula

Construct the prompt using the `Subject + Action + Scene + Camera + Style + Constraints` formula, tailored to the chosen genre.

### 4. Physics & Degree Adverbs

Instead of vague mood words, use concrete physics and intensity descriptors.

- **Physics Language:** `tires smoke`, `gravel sprays`, `sweat flies off in slow motion`, `dust erupts violently`, `fat renders slowly, oil bubbles form`.
- **Degree Adverbs:** `slowly`, `dramatically`, `violently`, `gently`, `frantically`. The model cannot infer intensity from images; it must be stated.

### 5. Anti-Slop Check (Expanded)

Scan the prompt for slop words that conceal a lack of specific information. This now includes action and camera slop.

- **Visual Slop:** `beautiful`, `stunning`, `epic`, `amazing`
- **Action/Camera Slop:** `dynamic`, `energetic`, `cinematic camera movement`, `cool transition`

Replace all slop with measurable, observable details.

---

## Why This Works

- **Aligns with Model Behavior:** This workflow is based on extensive analysis of community-proven prompts that have the highest success rates.
- **Reduces Failure Rate:** By avoiding overspecification and using the model\'s preferred prompt structure, this method drastically reduces errors like jitter, morphing, and camera chaos.
- **Genre-Specific:** Provides tailored guidance for the most common real-world use cases, not just one expert-level workflow.

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
