# Audio Guide

Use this reference for detailed audio, dialogue, beat-sync, ambience, and lip-sync workflows. Keep audio roles explicit and avoid promising exact platform behavior unless the active surface documents it.

## Dialogue

- Keep lines short, preferably one sentence per speaker turn.
- Put spoken dialogue in quotes.
- Assign the speaker by tag.
- Use stable framing for lip-sync.
- Avoid head turns, large face movement, extreme camera moves, or busy hand action while mouth accuracy matters.
- If the line matters more than the environment, reduce music and SFX during the line.

## Audio reference mapping

`[Audio1]` can be used for rhythm, pacing, mood, voice tone, ambience, music texture, or beat timing. Do not promise exact audio playback unless the active platform documents exact playback behavior. If the source contains a real voice or recognizable song, treat it as authorization-sensitive and convert it into broad sonic descriptors when rights are unclear.

| Role | Good wording | Avoid |
|---|---|---|
| Tempo | `[Audio1] provides tempo only; foot taps match the downbeat` | copying a protected performance |
| Mood | `[Audio1] provides calm sparse atmosphere` | exact replay claim |
| Voice tone | `soft, breathy, close-mic delivery` | imitating a named real voice |
| Ambience | `rainy street room tone, distant traffic bed` | dense competing sound layers |

## Multi-character dialogue

Use separate speaker turns when reliability matters. For two-person exchanges, generate controlled single-speaker clips and composite in post when necessary. If two speakers remain in one prompt, write: `Character A says... pause. Character B answers...` and keep the camera locked or gently motivated.

## Sound layer syntax

`Dialogue: Character A says "I found it." Sound: low room tone + distant rain. SFX: cup lands on table at 2s. Music: no music until after the line.`

## Beat-sync syntax

`[Audio1] provides tempo only. On each downbeat: back wall light pulses once, dancer hits one pose, camera remains locked wide.` Use visible beat changes rather than asking the model to understand an abstract groove.

## Troubleshooting

- Desync: shorten dialogue, stabilize camera, remove head motion, reduce competing sound, and clean source audio role.
- Wrong speaker: split lines by speaker and use explicit character tags.
- Audio ignored: remove competing music/SFX instructions and make `[Audio1]` role explicit.
- Overbusy mix: choose ambience plus one key SFX; remove music if dialogue matters.
- Lip-sync drift: use a locked medium close-up, no head turn, short quoted line, and simple expression.
