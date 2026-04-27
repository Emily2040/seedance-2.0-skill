---
name: seedance-interview
description: 'Guide users through a multi-stage creative journey to craft cinematic stories and single clips for Seedance 2.0. Use when a user has a vague idea, needs a script, or wants to elevate a simple prompt into a professional production brief. Follow the "Director\\'s Journey" workflow: Vision → Narrative → Visuals → Technical → Final Brief.'
license: MIT
user-invocable: true
user-invokable: true
tags: ["storytelling", "creative-writing", "directing", "pre-production", "scriptwriting", "narrative-design", "cinematography", "seedance-20"]
metadata: {"version": "5.0.0", "updated": "2026-03-03", "openclaw": {"emoji": "🎭", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "antigravity": {"emoji": "🎭", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "gemini-cli": {"emoji": "🎭", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "author": "Emily (@iamemily2050)", "repository": "https://github.com/Emily2040/seedance-2.0"}
  "parent": "seedance-20",
---

# seedance-interview · The Director\'s Journey (v5.0)

This skill transforms a simple idea into a professional Seedance 2.0 production brief. It uses a structured, multi-stage interview process that prioritizes genre and reference media to create effective, concise prompts.

## The Workflow

### Stage 1: The Vision & Genre

- **Action:** Get a 1-sentence concept from the user.
- **AI:** Immediately ask the user to choose a genre from the [ref:genre-guides].
- **AI:** Ask if they have any reference media (images, videos, audio).

### Stage 2: The "Quick Mode" Exit

- **If the user has strong reference media and a clear genre (e.g., Product Ad, Music Video), do not force them through the full interview.**
- **AI Output:** `"It looks like you have a clear vision and strong references. I recommend we move directly to prompt construction using the [skill:seedance-prompt] Director\'s Formula. Would you like to do that?"`
- This provides an off-ramp for users who do not need a deep narrative exploration.

### Stage 3: The Narrative Core (for Drama/Narrative genres)

- **If the user chose a narrative genre and has a vague idea, proceed with the "Attack & Deconstruct" method.**
- **AI:** Build a generic version of the scene.
- **AI Output:** `"I have built a Safe version of your scene: *[A woman in a red dress walks down a rainy street at night.]* Now, let\'s attack it. What is the one thing in this scene that *shouldn\'t* be there? What is the *friction*?"`

### Stage 4: Visual & Technical Layering

- Based on the user\'s answers, layer in the visual and technical details using the Director\'s Formula from [skill:seedance-prompt].
- Prioritize elements based on the chosen genre.

### Stage 5: The Final Production Brief

- **Action:** Output a structured brief that includes the final prompt (30-100 words), a list of the `@reference` assets, and director\'s notes.

---

## Why This Works

- **Efficiency:** The "Quick Mode" exit respects the user\'s time and prevents unnecessary over-specification.
- **Genre-Aware:** The process is tailored to the user\'s chosen content category from the start.
- **Reference-First:** It prioritizes the most powerful tool in the Seedance 2.0 arsenal: the `@reference` system.

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
