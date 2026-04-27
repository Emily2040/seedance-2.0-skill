---
name: seedance-camera
description: "This skill should be used when the user asks for camera movement, lens language, shot design, framing, tracking, dolly, crane, handheld, POV, one-take direction, or camera-transfer guidance for a Seedance 2.0 prompt."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - video-generation
  - camera
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

# seedance-camera · The One-Move Rule (v5.0)

This skill covers camera movement, framing, and multi-shot techniques for Seedance 2.0, centered on the most important principle for avoiding camera chaos: **The One-Move Rule**.

## The One-Move Rule

> **For any single shot, specify only ONE primary camera move.** Do not stack multiple moves (e.g., `dolly push` + `pan left` + `tilt up`). This is the most common cause of jitter, unwanted camera rotation, and failed generations.

---

## 1. The Camera Contract

Every shot should have a camera contract, but the `Move` parameter should only contain one item.

```
Framing:   [wide / medium / close-up / etc.]
Move:      [CHOOSE ONE: locked-off / dolly / pan / tilt / orbit / handheld / crane / tracking]
Speed:     [slow / moderate / fast / "over 8 seconds"]
Angle:     [eye level / low angle / high angle / etc.]
```

---

## 2. Genre-Based Camera Presets

Different genres have different camera languages. Use these presets as a starting point.

| Genre | Recommended Moves | Avoid |
| :--- | :--- | :--- |
| **Product/E-commerce** | `orbit`, `slow push-in`, `static` | `handheld`, `whip pan` |
| **Lifestyle/Social** | `handheld`, `static`, `slow pan` | `crane`, `dolly zoom` |
| **Drama/Narrative** | `slow push-in`, `dolly pull-out`, `tracking`, `static` | `fast orbit`, `snap zoom` |
| **Music Video** | `whip pan`, `snap zoom`, `fast tracking`, `orbit` | `slow pan` (unless for effect) |
| **Landscape/Travel** | `slow aerial pullback`, `slow pan`, `static wide` | `handheld`, `fast moves` |
| **Commercial/Brand** | `tracking`, `crane up`, `slow push-in` | `shaky handheld` |
| **Anime/Artistic** | `dynamic low-angle`, `fast push-in`, `whip pan` | `subtle, slow moves` |

---

## 3. Reliable Phrasing Library (The One-Move Edition)

Use these phrases to ensure clarity.

- `locked-off static camera, no movement`
- `slow dolly push from medium shot to tight close-up over 8 seconds`
- `slow dolly pull back revealing the full environment`
- `slow pan left revealing [new element]`
- `slow tilt up from [foreground] to [sky]`
- `slow orbit left around the subject, constant distance`
- `handheld tracking following the subject, subtle shake, not chaotic`
- `crane shot rising from ground level to overhead`

---

## 4. Advanced Techniques (Use with Caution)

These techniques can break the One-Move Rule but are powerful when used correctly.

- **Multi-Shot Within One Clip:** Use `[Cut to:]` to create a sequence of shots. Each shot in the sequence should still follow the One-Move Rule.
    - `[Shot 1: Wide, static] Description. [Cut to: Close-up, slow push-in] Description.`
- **One-Take Technique (一镜到底):** Use a sequence of reference images (`@Image1 @Image2 @Image3`) to define a continuous camera path. The prompt should describe the journey, not individual moves.
    - `@Image1 @Image2 @Image3, one continuous tracking shot, following the runner from the street, up the stairs, and onto the rooftop.`
- **Camera Transfer:** Use `@Video1` to copy the camera work from a reference clip. This is the safest way to achieve complex camera motion.
    - `Match the camera movement and editing from @Video1.`

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
