# Image-to-Video Guide

## Core Rule

Prompt only what the image cannot show. A still image already contains subject identity, product form, wardrobe, palette, composition, and background. Re-describing those static details often causes drift. Add motion, camera, timing, transformation, lighting change, audio, and preservation constraints.

## Minimal Template

`[Image1] is the reference; preserve [identity/product/scene] exactly. Only [motion] changes. Camera: [one move]. Lighting: [source or transition]. Sound: [cue]. Constraint: [what must not change].`

## Preservation Language

Use precise locks for fragile anchors: `preserve face identity`, `preserve logo and label`, `preserve bottle shape and cap geometry`, `preserve outfit and hairstyle`, `preserve room layout`. Do not lock everything if the scene needs natural motion; lock only what must remain stable.

## Good I2V Additions

| Add | Example |
|---|---|
| Micro-expression | `subject blinks once and lowers their eyes` |
| Product light | `thin highlight travels across the label` |
| Weather | `rain streaks behind the subject; droplets bead on the surface` |
| Camera | `slow dolly-in from current composition to tighter detail` |
| Atmosphere | `dust catches the doorway beam and settles` |
| Audio | `soft room tone, one key click at the endpoint` |

## Failure Fixes

- If identity drifts: reduce new visual description and strengthen preservation constraints.
- If camera jumps: use one camera move with start and endpoint.
- If product warps: say preserved, static identity, no shape change, no transformation of the product.
- If output is still: add one physical action and one time cue.
- If background changes: preserve environment layout and animate only light, weather, or atmosphere.
- If hands deform: simplify hand motion or keep hands outside the main action.
