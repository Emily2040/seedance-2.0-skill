---
name: seedance-motion
description: "This skill should be used when the user asks for body action, choreography, physics, object movement, movement timing, action continuity, stunt direction, or motion-reference mapping in Seedance 2.0."
license: MIT
user-invocable: true
tags:
  - motion
  - choreography
  - physics
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

# seedance-motion

Use physical verbs and consequences. Motion should be observable on screen, timed within the clip, and assigned to a subject or object. Prefer one strong action with a visible endpoint over several vague actions competing for attention.

## Motion Contract

State: actor/object, action, force level, timing, physical consequence, continuity requirement, and endpoint.

| Motion type | Strong phrase | Weak phrase |
|---|---|---|
| Subtle acting | `Character A inhales, grips the cup tighter, then sets it down without looking away` | `she feels nervous` |
| Product material | `condensation beads gather, merge, and slide down the bottle neck` | `the product looks refreshing` |
| Choreography | `Character B ducks under the swinging bag, pivots left, and stops in a guarded stance` | `fast action fight scene` |
| Object physics | `paper receipt lifts in the fan breeze, flips once, and lands face-up` | `papers move dynamically` |
| Environmental motion | `rain streaks diagonally across the backlight while puddle ripples spread from footsteps` | `stormy weather atmosphere` |

## Timing Pattern

Use a three-beat structure for short clips: setup, action, changed end state. Example: `0-2s: candle flame steady; 2-4s: door opens and flame bends; 4-6s: smoke trail curls toward the hallway`. Time segmentation is useful for action, VFX, lip-sync, and product demonstrations, but avoid frame-perfect overload unless the user truly needs it.

## Reference Motion Rules

For reference footage, use only owned, licensed, public-domain, stock, mocap, rehearsal, or self-recorded material. Map `[Video1]` to motion, camera, timing, or blocking, not identity, unless the identity is authorized. If a reference contains a real person, transfer only general motion or camera behavior and explicitly exclude likeness transfer.

## Stability Rules

Hands, faces, logos, and product geometry drift when too many actions occur. Reduce motion around fragile details: lock the camera for lip-sync, keep hands in simple poses, ask product parts to remain rigid, and move light or environment instead of the core identity anchor.

## Output Contract

Return the motion phrase, timing pattern, reference role map if any, and repaired prompt language.
