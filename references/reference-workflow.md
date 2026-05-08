# Reference Workflow

## Asset Role Map

Before writing prompt prose, assign every uploaded asset a role.

| Asset | Good Roles | Avoid |
|---|---|---|
| Image | identity, product, pose, costume, environment | asking it to define unseen motion |
| Video | motion, camera, pacing, blocking | copying protected identity or scene ownership |
| Audio | rhythm, voice tone, ambience, music texture | assuming voice/likeness authorization |

## Rules

- Preserve reference tags exactly.
- Do not ask one reference to control incompatible roles.
- Use owned, licensed, public-domain, or clearly authorized references.
- Write what should transfer and what should not transfer.

## Template

`[Image1] controls product identity. [Video1] controls camera pace only. Preserve the subject from [Image1]; do not copy characters, logos, or environment from [Video1].`
