## 5.1.0 — 2026-04-27

Validation, status, and progressive-disclosure repair release.

- Fixed YAML/frontmatter structure across root and all 23 sub-skills.
- Moved `metadata.parent` into `metadata` for sub-skills.
- Rewrote descriptions into third-person trigger format for better skill activation.
- Replaced stale Feb. 2026 API/face-status claims with dated April 2026 source-aware guidance.
- Added `references/api-status.md` and `references/source-registry.md`.
- Added validation scripts, GitHub Actions validation, and `evals/evals.json`.
- Moved oversized legacy skill bodies into `references/migrated/` and replaced active bodies with lean routers.
- Rewrote active studio/franchise/clone wording into IP-safer descriptors.


# Changelog — seedance-20

All notable changes to this project are documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [5.0.0] — 2026-03-03
### Added
- **Intent-First Philosophy** — The entire library now prioritizes intent-based prompting over precision-based micro-management. New governing rule: "Direct the model. Don't micro-manage it."
- **4 new reference files:**
  - `references/genre-guides.md` — 7-genre prompt templates (Product, Lifestyle, Drama, Music Video, Landscape, Commercial, Anime).
  - `references/reference-workflow.md` — Complete `@reference` system guide (Image, Video, Audio, Material tags).
  - `references/i2v-guide.md` — Image-to-Video best practices: motion-only prompts, common mistakes.
  - `references/intent-vs-precision.md` — The philosophical shift from precision to intent.

### Changed
- **`seedance-prompt` (P0 rewrite)** — Replaced Concealment Check with Director's Formula: genre router, 30-100 word target, I2V gate, anti-slop check.
- **`seedance-motion` (P0 restructure)** — Replaced micro-choreography with intent-first motion: degree adverbs, physics consequences, `@Video` reference as primary tool.
- **`seedance-camera` (P1 update)** — Added One-Move Rule as governing principle, genre-based camera presets, camera transfer via `@Video`.
- **`seedance-recipes` (P1 expansion)** — Expanded from cinematic-only to 7 content categories with templates.
- **`seedance-interview` (P1 update)** — Added Quick Mode exit for users with strong references, genre detection from `genre-guides`.
- **`seedance-interview-short` (P1 update)** — Aligned with 30-100 word target, added genre and reference fields.
- **`seedance-troubleshoot` (P1 update)** — Replaced Conservation Law with practical 5-step diagnostic tree.
- **`seedance-prompt-short` (P2 update)** — Aligned budget table with 30-100 word target.
- **`seedance-style` (P2 update)** — Changed style budget from "2-3 tokens" to "ONE primary style anchor."
- **`seedance-vfx` (P2 update)** — Added intent-first framing to FX contract.
- **`seedance-audio` (P2 update)** — Added natural language sound description guidance.
- Root `SKILL.md`, `README.md`, `CHANGELOG.md`, `quick-ref.md` updated for v5.0.0.

---

## [4.2.0] — 2026-03-03
### Added
- **Safe Vocabulary Integration** — Added filter-safe action, weapon, clothing, body, environment, material, VFX, sound, and production-context vocabulary to `seedance-filter` and all 5 language vocabulary skills.
- Term counts expanded: `vocab-zh` 550+, `vocab-ja` 450+, `vocab-ko` 450+, `vocab-es` 450+, `vocab-ru` 450+.
- New categories per language: Safe Action & Combat, Safe Weapon, Safe Clothing & Armor, Safe Body & Physique, VFX Particles & Energy, Diegetic Audio, Safe Environment, Material & Surface, Production Context Tokens.

### Changed
- Root `SKILL.md` version bumped to `4.2.0` with `2026-03-03` date.
- `README.md` updated: version badge `4.2.0`, term counts, architecture tree (23 sub-skills), compliance count.
- All 5 vocabulary sub-skills bumped to `4.2.0`.
- `seedance-filter` safe vocabulary database appended as master English reference.

---

## [4.1.0] — 2026-03-02
### Added
- **New `seedance-filter` skill** — Content filter intelligence module. Explains how the Seedance 2.0 content filter evaluates prompts (language-model-based intent assessment, not keyword matching), documents the 37% false-positive block rate, and provides actionable techniques: four-question framework, high-risk word avoidance, image upload best practices, Chinese prompt trick, and professional-language framing.

### Changed
- Root `SKILL.md` version bumped to `4.1.0` with `2026-03-02` date.
- `README.md` updated: version badge `4.1.0`, skill count `23`, Content Quality table includes `seedance-filter`.
- `CHANGELOG.md` updated with this entry.
- `references/quick-ref.md` skill map updated to include `seedance-filter`.

---

## [4.0.0] — 2026-02-28
### Added
- **Cognitive Architecture Upgrade** — Three core skills redesigned using cognitive opcodes inspired by [agi-in-md](https://github.com/Cranot/agi-in-md).
  - `seedance-interview` **L8 Construction-First**: AI builds a "Safe" draft immediately, then asks the user to "attack" it. The user's attack reveals the true creative intent — the "cinematic friction" — which becomes the foundation of the final prompt.
  - `seedance-prompt` **L7 Concealment Check**: Before building a prompt, the AI scans for "concealment words" (beautiful, stunning, epic) that hide a lack of specific visual information. Each is deconstructed and replaced with measurable, observable detail.
  - `seedance-troubleshoot` **L11 Conservation Law**: When a prompt consistently fails, the AI identifies the fundamental trade-off (e.g., Detail × Motion = Constant) and "inverts" the design to find a creative escape route.
- **Storytelling Framework Reference** — Added `references/storytelling-framework.md` with narrative design, visual layering, and director's toolkit principles.

### Changed
- Root `SKILL.md` version bumped to `4.0.0`.
- All 22 sub-skill `SKILL.md` files synchronized to `4.0.0` with `2026-02-28` date.
- `README.md` updated: version badge, skill descriptions, architecture tree, and CHANGELOG reference.

---

## [3.8.0] — 2026-02-27
### Added
- **Dual Workflow System**: Two distinct prompt engineering workflows now available.
  - `seedance-prompt-short`: New short-form prompt skill with hard 2000-character budget and Compression Engine (4 rules: Verbs > Adjectives, Show Don't Tell, Film Language, Trust the Model).
  - `seedance-interview-short`: New short-form interview skill with live character counter and Director's Notes + Compression Log in final output.
- **Field Note**: Added practitioner note that Seedance V2 performs best with short (<2000 char) Chinese prompts in `README.md` and root `SKILL.md`.
- **README**: New "Two Workflows: Max Detail vs. Max Performance" section with comparison table. Sub-skill count updated to 22.
### Preserved
- `seedance-prompt` and `seedance-interview` (Max Detail, Long Form) fully intact.

---

## [3.7.0] — 2026-02-26
### Changed
- Redesigned `seedance-interview` as **"The Director's Journey"** — a multi-stage storytelling workflow (Vision → Narrative → Visuals → Technical → Final Brief).
- Replaced the A/B/C/D/E guided stages with creative "Director's Questions" for deeper narrative extraction.
- Added `references/storytelling-framework.md` — professional cinematography and narrative design principles.
- Updated root `SKILL.md` to v3.7.0 with storytelling-framework reference and interview in core pipeline.
- Updated README.md: version badge, interview emoji 🎭, skill count 20, references count 5.

## [3.6.1] — 2026-02-26

### Added
- **New `seedance-examples-zh` skill** — 16 production-ready Chinese prompt examples across 7 genres (Short Drama, Advertising, Animation, Product, VFX, Cinematography, Beat Sync).
- **Enhanced Chinese Vocabulary** — Expanded `seedance-vocab-zh` to 400+ terms across 16 categories, including new "Theme & Style" and "Prompt-Ready Phrases".
- **Official Platform Links** — Added official website links for all 10 supported platforms (Antigravity, Gemini CLI, Firebase Studio, Claude Code, OpenClaw, GitHub Copilot, Codex, Cursor, Windsurf, OpenCode) in `README.md`.
- **Author Social Links** — Added clickable 𝕏 and IG links for Emily (@iamemily2050) in `README.md` and `SKILL.md`.

### Changed
- **Universal Version Sync** — All 21 `SKILL.md` files synchronized to `v3.6.1` with updated `2026-02-26` metadata.
- **README Refinement** — Updated version/skill badges, fixed architecture tree flags, and added "Working Examples" collapsible section.
- **Platform Constraints** — Updated `platform-constraints.md` with latest Feb 26 verification and API status.

---

## [3.6.0] — 2026-02-25

### Added
- **Full cross-platform support** — Antigravity, Gemini CLI, Firebase Studio, Codex, Cursor, Windsurf, OpenCode declared in all 20 `SKILL.md` files via `tags` and `metadata` platform blocks.
- `tags:` array added to all 19 sub-skill files (previously missing entirely).
- `metadata.antigravity`, `metadata.gemini-cli`, `metadata.firebase` blocks added to all relevant skills.
- **Platform Compatibility table** injected into root `SKILL.md` body with install paths and one-liner install commands for all 10 supported platforms.
- `seedance-pipeline` tagged with `firebase` for Firebase Studio pipeline integration.
- Author attribution: **Emily (@iamemily2050)** added across `LICENSE`, `README.md`, `CODEOWNERS`, and root `SKILL.md`.
- `README.md` — full GitHub-ready project README with install matrix, skill directory, and badges.
- `LICENSE` — MIT licence with correct copyright holder.
- `CHANGELOG.md` — this file.
- `.github/CODEOWNERS` — ownership declarations.

### Changed
- `metadata.homepage` URLs updated from placeholder `github.com/seedance-2.0` to `github.com/Emily2040/seedance-2.0` across all 20 files.
- Root skill version bumped `3.5.0 → 3.6.0`.
- `seedance-audio` version bumped `4.2.0 → 4.3.0`.
- `seedance-prompt` version bumped `3.3.0 → 3.4.0`.
- `seedance-troubleshoot` version bumped `3.4.0 → 3.5.0`.

---

## [3.5.0] — 2026-02-25

### Added
- OpenClaw / ClawHub full compatibility (`user-invocable: true`, `user-invokable: true` on all 20 skills).
- `metadata.openclaw` blocks with emoji and homepage on all 20 skills.
- `metadata.parent: seedance-20` on all 19 sub-skills.
- Verb-first, single-quoted descriptions with WHEN trigger phrases on all 20 skills.

### Fixed
- Illegal dot in root `name` field: `seedance-2.0` → `seedance-20`.
- Non-standard top-level fields (`last-stress-tested`, `updated`, `last-updated`) migrated into `metadata` JSON block.
- `version:` moved from top-level field into `metadata.version`.
- All 19 sub-skills now explicitly declare `user-invocable: true` and `user-invokable: true`.

---

## [3.4.1] — 2026-02-25

### Added
- `seedance-antislop` skill: anti-slop and filler-language detection for prompt quality.
- `seedance-copyright` skill: live Feb 2026 IP enforcement data (Disney, Paramount, MPA, SAG-AFTRA).
- `seedance-interview` skill v4.0.0: guided A/B/C/D/E multi-stage pre-production workflow.
- Multilingual vocabulary skills: `seedance-vocab-es`, `-ja`, `-ko`, `-ru`, `-zh`.

### Changed
- Root skill version bumped to `3.4.1`.
- Copyright skill updated with post-enforcement state (ByteDance face-upload pause Feb 15 2026).

---

## [3.3.0] — 2026-02-25

### Added
- `seedance-troubleshoot` v3.3.0 with QA checklist and emergency fixes.
- `seedance-pipeline` v3.1.0 with ComfyUI node workflows and post-processing chain.
- `seedance-recipes` v3.1.0 with genre-specific template recipes.

---

## [3.2.1] — 2026-02-25

### Fixed
- Audio skill desync documentation updated with multi-character constraints.
- Camera skill anti-drift lock section added.

---

## [3.2.0] — 2026-02-25

### Added
- `seedance-prompt` v3.2.0 with five-layer stack and `@Tag` delegation levels 1–4.
- `seedance-antislop` v3.2.0.

---

## [3.1.0] — 2026-02-25

### Added
- Initial release of core pipeline skills:  
  `seedance-audio`, `seedance-camera`, `seedance-motion`, `seedance-lighting`,  
  `seedance-characters`, `seedance-style`, `seedance-vfx`.

---

## [3.0.0] — 2026-02-25

### Added
- Initial Seedance 2.0 skill package creation.
- Root `SKILL.md` with quad-modal AI filmmaking framework (T2V · I2V · V2V · R2V).

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
