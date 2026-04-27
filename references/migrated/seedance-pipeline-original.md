# Legacy body for `seedance-pipeline`

Migrated on 2026-04-27 during v5.1.0. Treat platform, policy, API, and safety claims here as legacy unless confirmed in `references/api-status.md` or `references/source-registry.md`.

---

# seedance-pipeline

API, ComfyUI, and post-processing for Seedance 2.0.

## Platform Access

| Surface | Endpoint / App | Notes |
|---|---|---|
| Web | jimeng.jianying.com (Dreamina) | 4–15 s, up to 1080p |
| Mobile | CapCut / Jianying · Xiaoyunque | 5–10 s |
| API | Volcengine `Doubao-Seedance-2.0` | See rate limits below |
| Consumer | Doubao app | Standard web limits |

## Volcengine API

```
POST https://ark.cn-beijing.volces.com/api/v3/videos/generations
Authorization: Bearer <API_KEY>
Content-Type: application/json
```

```json
{
  "model": "Doubao-Seedance-2.0",
  "prompt": "<compiled plain-text prompt>",
  "duration": 8,
  "aspect_ratio": "16:9",
  "resolution": "1080p",
  "seed": 42
}
```

**Rules**
- Never send raw JSON schema — compile to plain text first.
- `seed` is optional; omit for variation, set for reproducibility.
- Check `status` field in response: `queued → processing → completed | failed`.
- Poll at 5 s intervals; timeout after 120 s.

## File Budget ("Rule of 12")

| Type | Max count | Max size each | Format |
|---|---|---|---|
| Image | 9 | 30 MB | JPG · PNG · WEBP |
| Video | 3 | **combined ≤ 15 s total** | MP4 · MOV |
| Audio | 3 | total ≤ 15 s | MP3 |
| **Total files** | **12** | — | — |

## ComfyUI Node Workflow

```
[Load Image / Load Video] → [Seedance2 Sampler]
      ↓                           ↓
[CLIP Text Encode]          [Prompt Compiler]
      └────────────────────────→ ↓
                         [Video Output Node]
                                 ↓
                      [Frame Interpolation]
                                 ↓
                         [Upscale Node]
                                 ↓
                       [Color Grade Node]
                                 ↓
                        [Export / Mux Audio]
```

Key node parameters: `duration`, `aspect_ratio`, `resolution`, `seed`, `motion_strength`.

## Post-Processing Chain

### 1 · Upscale
- Tool: Topaz Video AI · Real-ESRGAN · ffmpeg `scale=iw*2:ih*2`
- Target: 720p → 1080p (standard) · 1080p → 2K (premium)

### 2 · Frame Interpolation
- Tool: RIFE v4.x · DAIN
- Standard: 24 fps → 60 fps (smooth motion)
- Fight / fast action: 24 fps → 120 fps

### 3 · Color Grade
- Tools: DaVinci Resolve · FFmpeg LUT
- Workflow: normalize exposure → apply LUT → mask-lift shadows → finalize.
- LUT slots: Rec.709 (web) · Log-C (archive).

### 4 · Audio Mux
- Merge generated stereo audio with video: `ffmpeg -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -shortest out.mp4`

### 5 · Metadata Clean
- Strip generation metadata before distribution: `exiftool -all= output.mp4`
- Rename: `{project}_{shot}_{take}_{date}.mp4`

### 6 · Composite (optional)
- Layer generated clips in After Effects / DaVinci Fusion.
- Match color temperature across cuts before export.

## Output Specs

| Use case | Resolution | FPS | Container | Audio |
|---|---|---|---|---|
| Web / social | 1080p | 30 | MP4 H.264 | AAC 192k stereo |
| Film festival | 2K | 24 | MOV ProRes | PCM 48kHz |
| Archive | 2K | 24 | MKV H.265 | FLAC stereo |

## Routing

For prompt issues → [skill:seedance-prompt]
For camera/storyboard → [skill:seedance-camera]
For QA / errors → [skill:seedance-troubleshoot]
