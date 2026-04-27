---
name: seedance-troubleshoot
description: 'Diagnose and fix failing or low-quality Seedance 2.0 prompts using a 5-step diagnostic tree. Use when a prompt is consistently failing, producing generic output, or being rejected. Covers blurry/jittery output, camera chaos, character drift, stiff action, and ambiguous results.'
license: MIT
user-invocable: true
user-invokable: true
tags: ["debugging", "troubleshooting", "prompt-engineering", "quality-control", "root-cause-analysis", "seedance-20"]
metadata: {"version": "5.0.0", "updated": "2026-03-03", "openclaw": {"emoji": "🔧", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "antigravity": {"emoji": "🔧", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "gemini-cli": {"emoji": "🔧", "homepage": "https://github.com/Emily2040/seedance-2.0"}, "author": "Emily (@iamemily2050)", "repository": "https://github.com/Emily2040/seedance-2.0"}
  "parent": "seedance-20",
---

# seedance-troubleshoot · Diagnostic Tree (v5.0)

This skill diagnoses and fixes the most common Seedance 2.0 failure modes. It uses a simple diagnostic tree to identify the root cause and provides a specific, actionable solution.

## The Diagnostic Tree

Start at the top and work your way down.

### 1. Is the output blurry, jittery, or morphing?

- **Root Cause:** Overspecification. Your prompt is too long, has too many competing details, or too many actions in a short time (violating beat density).
- **Solution:**
    1.  **Cut the prompt length** to 30-100 words.
    2.  **Use a reference.** Find an `@Image` or `@Video` that shows the style or action you want and replace 50+ words of description with a single `@reference` tag.
    3.  **Simplify the action.** Reduce the number of distinct movements in the shot.

### 2. Is the camera chaotic, spinning, or ignoring your instructions?

- **Root Cause:** You have violated the **One-Move Rule** by stacking multiple camera moves in a single shot.
- **Solution:**
    1.  Rewrite the camera instruction to include only **ONE** primary move (e.g., `slow dolly push`, `handheld tracking`, `static wide shot`).
    2.  If you need multiple moves, use the `[Cut to:]` syntax to create a sequence of shots, each with its own single move.
    3.  For complex moves, use a `@Video` reference and tell the model to `Match the camera movement from @Video1`.

### 3. Is the character not looking like your reference image?

- **Root Cause:** The prompt is re-describing the character, which competes with and overrides the `@Image` reference.
- **Solution:**
    1.  **Delete all physical descriptions** of the character from the prompt (hair color, clothing, face).
    2.  The prompt should only describe the character's **action and emotion**.
    3.  Ensure the `@Image` reference is a clear, well-lit shot of the character.

### 4. Is the action stiff, slow, or lacking impact?

- **Root Cause:** Lack of intent and physics language. The model doesn\'t know *how* to perform the action.
- **Solution:**
    1.  **Add degree adverbs:** `violently`, `gracefully`, `frantically`, `dramatically`.
    2.  **Add physics consequences:** `dust erupts`, `sparks fly`, `the character staggers`, `sweat flies off in slow motion`.
    3.  **Use an `@Video` reference** of a similar action to give the model a clear example.

### 5. Is the output just not what you wanted?

- **Root Cause:** Your prompt is ambiguous. Words like `cinematic`, `epic`, and `beautiful` are subjective and mean nothing to the model.
- **Solution:**
    1.  Run the prompt through the **Anti-Slop Check** in the [skill:seedance-prompt] skill.
    2.  Replace every subjective adjective with a measurable, observable detail.
    3.  **Iterate.** Make small changes to your prompt and re-roll 3-5 times. Do not expect a perfect result on the first try.

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
