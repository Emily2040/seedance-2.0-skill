# platform-constraints · Seedance 2.0 (Q1 2026)
# Last verified: 2026-02-26 against ByteDance official launch blog + multiple third-party guides

## Generation Duration

| Platform | Min | Max | Notes |
|---|---|---|---|
| Web (Dreamina/Jimeng) | 4 s | 15 s | User-selectable slider |
| All platforms | 4 s | 15 s | No confirmed mobile-specific cap |

> ⚠️ An earlier version of this file listed "5–10 s mobile" — that distinction is **unconfirmed**. All verified sources say 4–15 s universally.

## Resolution

| Tier | Resolution |
|---|---|
| Default | 720p |
| Standard | 1080p |
| Premium | 2K |

## File Budget — Rule of 12

| Type | Max count | Duration/size limit | Format |
|---|---|---|---|
| Image | 9 | — | JPG · PNG · WEBP |
| Video | 3 | **15 s TOTAL across all 3** | MP4 · MOV |
| Audio | 3 | **15 s TOTAL across all 3** | MP3 |
| **Total files** | **12** | — | — |

> ⚠️ The 15-second video limit is **combined total**, not per-file. Three 5-second clips = 15 s, which hits the ceiling. File size per video not confirmed from primary sources.

## Aspect Ratios

`16:9` · `9:16` · `4:3` · `3:4` · `21:9` · `1:1`

> v3.1.0 and earlier only listed four ratios. 3:4 and 21:9 confirmed via apiyi.com technical guide.

## Audio Output

Dual-channel stereo (synchronized audio-video joint generation).

## Negative Prompts

**NOT SUPPORTED.** Seedance 2.0 does not accept negative prompt syntax (`--no`, `negative:`, etc.).
Use positive constraints instead: describe what you *want*, not what you don't want.

```
❌  --no watermark --no distorted hands
✅  clean background, stable hands, no overlaid text
    [describe the positive constraint in plain language]
```

## API Status (as of 2026-02-26)

| Channel | Status |
|---|---|
| Jimeng / Dreamina web | ✅ Live (paying members) |
| Volcengine console debugging | ✅ Available for testing |
| **Official Volcengine API** | ❌ **Delayed — was planned Feb 24; postponed due to copyright dispute** |
| BytePlus (international) | ❌ Not yet officially launched |
| Third-party proxy APIs (AtlasCloud, APIYI) | Available but unofficial |

> Until the official API launches, do **not** plan production integrations against a Seedance 2.0 API endpoint.

## Platforms

| Surface | URL / App |
|---|---|
| Web | jimeng.jianying.com (Dreamina) |
| Mobile | CapCut · Jianying |
| API (pending) | Volcengine / BytePlus — launch date TBD |

## Prompt Length Guidance

| Language | Simple scene | Complex choreography |
|---|---|---|
| English | 30–100 words | 300–1000+ words |
| Chinese | 50–200 characters | 500–1000+ characters |

Shorter prompts → higher motion quality in most cases.
