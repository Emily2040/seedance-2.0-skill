# Seedance Prompt JSON Schema

Use this schema when the user wants structured output or when an automation pipeline needs stable fields.

```json
{
  "mode": "t2v | i2v | v2v | r2v | audio-led",
  "duration": "string",
  "aspect_ratio": "string",
  "references": [
    {"tag": "Image1", "role": "identity | product | pose | environment | style"},
    {"tag": "Video1", "role": "motion | camera | pacing | blocking"},
    {"tag": "Audio1", "role": "voice | rhythm | ambience | music"}
  ],
  "characters": [],
  "scene": "",
  "camera": "",
  "motion": "",
  "lighting": "",
  "style": "",
  "audio": "",
  "safety_notes": [],
  "final_prompt": ""
}
```

The JSON wrapper is for planning. The final prompt still needs to read naturally.
