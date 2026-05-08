# Audio Guide

Use this reference for detailed audio, dialogue, beat-sync, and lip-sync workflows.

## Dialogue

- Keep lines short.
- Put dialogue in quotes.
- Assign the speaker.
- Use stable framing for lip-sync.
- Avoid head turns, large face movement, or extreme camera moves while mouth accuracy matters.

## Audio reference mapping

`[Audio1]` can be used for rhythm, pacing, mood, voice reference, or beat timing. Do not promise exact audio playback unless the active platform documents exact playback behavior.

## Multi-character dialogue

Use separate speaker turns when reliability matters. For two-person exchanges, generate controlled single-speaker clips and composite in post when necessary.

## Sound layer syntax

`Sound: low room tone + distant rain. SFX: cup lands on table at 2s. Music: low pulse enters after the cut.`

## Troubleshooting

- Desync: shorten dialogue, stabilize camera, remove head motion, clean source audio.
- Wrong speaker: split lines by speaker and use explicit character tags.
- Audio ignored: remove competing music/SFX instructions and make `[Audio1]` role explicit.
