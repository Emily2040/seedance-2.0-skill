---
name: seedance-style
description: "This skill should be used when the user asks for visual style, period aesthetics, render look, texture, animation style, film stock, production design, style transfer, or IP-safe style descriptors for Seedance 2.0."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - seedance-20
  - video-generation
  - style
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

# seedance-style

Style anchors, CGI material specification, and aesthetic control for Seedance 2.0.

## Scope

- Style tokens that work (film language vs. trend words)
- Render-engine references as style bias
- Animation and anime control
- Period/historical material specification
- CGI material contract (avoiding plastic sheen)
- Style transfer via @Video reference

## Out of scope

- Lighting color and contrast — see [skill:seedance-lighting]
- Character clothing identity — see [skill:seedance-characters]
- VFX particle and energy effects — see [skill:seedance-vfx]

---

## Style Anchors That Work

Anchor with physical film language, not trend words.

```
Lens feel:   anamorphic / vintage softness / spherical / fisheye
Texture:     subtle film grain / digital clean / noise as character
Palette:     muted / desaturated / warm highlights cold shadows / neon-saturated
Contrast:    low-key / high-key / deep blacks / crushed shadows
```

**Style budget: **ONE primary style anchor** is recommended. Add a secondary anchor only if necessary.**
`"anamorphic, subtle grain, muted palette"` — done.

---

## Render-Engine Style Tokens

These function as legitimate style bias (not confirmed universal — test and document):

- `Unreal Engine 5 rendering` — game-engine realism, ray-traced reflections, SSS
- `Blender render` — 3D animation aesthetics
- `Octane render` — high-end material rendering

Use with specific material descriptions (see CGI section below). Render-engine tokens alone without material context produce inconsistent results.

**Still delete:** `8K` (empty filler), `masterpiece`, `award-winning`, `ultra-real`.

---

## Animation / Anime Control

Use production descriptors, never studio or series names:

```
clean linework, limited shading, 2D animation, motion on twos, smear frames on fast turns
watercolor wash backgrounds, ink outline characters
3D cel-shaded, bold outlines, flat color fills
stop-motion texture, visible material grain
```

---

## Period / Historical Control

Specify materials and lighting of the era rather than decade labels alone:

```
1920s:  oil lamp practicals, soot-stained plaster, handwoven wool, iron hardware
1970s:  film stock warm yellows, faded contrast, wide collars, grain heavy
1990s:  VHS scan lines, oversaturated color, handheld shake
feudal: rough-hewn timber, candle light, raw silk, bronze fittings
```

---

## CGI Material Contract

CGI fails when materials are unspecified → "plastic sheen."

Specify 2–4 properties per material:

```
Base:        metal / painted metal / glass / ceramic / rubber / fabric / wood / stone
Roughness:   matte / satin / glossy / mirror
Imperfection: micro-scratches / dust / fingerprints / wear marks / patina
Edge:        slightly beveled / razor sharp / rounded / chipped
```

**Example:**
```
brushed aluminum, satin roughness, fine micro-scratches, subtle edge wear
aged leather, matte surface, visible grain, creased at flex points
```

---

## Motion Physics for Materials

The material contract extends into motion:

```
Heavy objects: slow acceleration, slow deceleration
Cloth: lags behind motion, catches up with overshoot
Glass: reflections shift with camera movement
Liquid: sloshes with inertia, settles slowly
```

State mass when needed: `"feels heavy, slow inertia."`

---

## Style Transfer via Reference

Most reliable method. Upload a reference and describe the extraction:

```
Match the visual style, color grading, and film texture of @Video1
Apply @Image1's artistic style and color palette to the scene
```

The model extracts: color grade, contrast, film grain, lighting mood, compositional style, editing rhythm.

---

## Agent gotchas

1. Style tokens are consumed before generation. Keep to 2–3. Beyond that, the model's attention dilutes.
2. "Cinematic" does nothing. Every generated video is "cinematic" by default. Replace it with a lens or contrast description.
3. Render-engine tokens work best when paired with specific material descriptions. Alone they are inconsistent.
4. For CGI: always specify imperfections. Perfect surfaces look fake. Real objects have dust, scratches, wear.
5. Style transfer via reference beats 10 style-descriptor words. If you have a reference clip, use it.
