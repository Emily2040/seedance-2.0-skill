# Reference Workflow

## Asset Role Map

Before writing prompt prose, assign every uploaded asset a role. Role mapping prevents accidental transfer of identity, logos, scene ownership, or incompatible camera and motion instructions.

| Asset | Good Roles | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment, first frame, last frame | asking it to define unseen motion |
| Video | motion, camera, pacing, blocking, timing, gesture rhythm | copying protected identity, logo, or scene ownership |
| Audio | rhythm, tempo, mood, ambience, delivery tone, music texture | assuming voice, song, or likeness authorization |
| Text brief | action, genre, camera plan, constraints | replacing concrete reference roles with vague mood words |

## Rules

- Preserve reference tags exactly.
- Give every reference one primary role before writing style language.
- Do not ask one reference to control incompatible roles unless the tradeoff is explicit.
- Use owned, licensed, public-domain, or clearly authorized references.
- Write what should transfer and what should not transfer.
- When authorization is unclear, transfer broad motion, tempo, mood, or production function rather than protected identity.

## Role Examples

| Situation | Strong map |
|---|---|
| Product ad | `[Image1] controls product identity; [Audio1] controls tempo only.` |
| Motion transfer | `[Video1] controls side-step choreography only; do not transfer performer, costume, room, or logo.` |
| Style reference | `[Image2] controls warm bar atmosphere only; product identity remains from [Image1].` |
| First-last frame | `[Image1] is first frame; [Image2] is target end frame; transition occurs through light sweep, not product deformation.` |

## Template

`[Image1] controls product identity. [Video1] controls camera pace only. [Audio1] controls tempo only. Preserve the subject from [Image1]; do not copy characters, logos, music, voice, or environment from [Video1]/[Audio1].`
