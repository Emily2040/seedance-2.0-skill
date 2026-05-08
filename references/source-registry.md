# Source Registry

last_verified: 2026-05-08

Use this registry before making factual claims about Seedance 2.0 platform behavior. Prefer primary public sources, attach a verification date, and mark volatile claims as recheck-required. This file is a claim-boundary map, not a guarantee of access on every product surface or region.

## Evidence labels

| Label | Meaning | Required wording |
|---|---|---|
| `confirmed` | Directly visible in a primary public source at the verification date. | `Public sources state... as of [date].` |
| `volatile` | Likely to change by surface, account, region, pricing page, or model update. | `Recheck before giving numbers or promises.` |
| `field-observed` | Repeated creator/practitioner pattern but not official platform truth. | `Field observation, not guaranteed platform behavior.` |
| `unverified` | Plausible but not confirmed by a primary source. | `Requires testing or owner confirmation.` |
| `internal` | Repository guidance derived from this skill package. | `Use as workflow guidance, not external fact.` |

## Primary source hierarchy

| Topic | Preferred source | Evidence label | Verification note | Claim boundary |
|---|---|---|---|---|
| Core model capabilities | ByteDance Seedance 2.0 official page: https://seed.bytedance.com/en/seedance2_0 | confirmed | Recheck before release notes, API claims, or marketing copy. | Use for broad public capability framing only. |
| Launch capabilities and known limits | ByteDance Seedance 2.0 launch blog: https://seed.bytedance.com/en/blog/seedance2_0 | confirmed | Recheck when discussing multimodal reference, editing, audio, and platform examples. | Do not turn launch examples into guaranteed behavior on every surface. |
| API tutorial | BytePlus ModelArk Dreamina Seedance 2.0 series tutorial: https://docs.byteplus.com/en/docs/ModelArk/2291680 | confirmed | Recheck before procedural API guidance. | Tutorial existence is not the same as account access. |
| Video-generation API | BytePlus ModelArk Seedance video-generation API reference: https://docs.byteplus.com/en/docs/ModelArk/1544106 | confirmed | Recheck endpoints, request fields, model IDs, and task retrieval path. | API shape may differ by region, account, or release channel. |
| Pricing and region | BytePlus pricing and region pages | volatile | Always recheck immediately before quoting numbers. | Never invent price, quota, upload limit, or region availability. |
| Face, portrait, and voice behavior | Active product surface, official policy, and user authorization | volatile | Recheck current surface behavior and authorization context. | Do not infer consent from an uploaded asset. |
| Community practice | Douyin, Bilibili, CSDN, creator notes, workflow screenshots | field-observed | Use only as practitioner guidance. | Mark as non-official; do not state as model guarantee. |
| Repository guidance | README, SKILL.md, references, evals | internal | Keep aligned with source registry and API status. | Workflow guidance, not an external source of platform facts. |

## Required claim patterns

When answering platform-status questions, say: `As of 2026-05-08, public official sources describe Seedance 2.0 as supporting text, image, audio, and video inputs, and BytePlus ModelArk publishes video-generation API documentation. Access, pricing, model IDs, upload limits, regions, and authorization behavior remain surface-specific and should be rechecked.`

When answering pricing, quota, upload-limit, model-ID, or regional-availability questions, do not guess. State that those values are volatile and require checking the current official surface.

When answering likeness, portrait, or voice questions, separate three things: technical surface support, rights/authorization, and prompt safety. Do not infer consent from a file upload.
