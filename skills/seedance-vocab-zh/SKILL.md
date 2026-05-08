---
name: seedance-vocab-zh
description: "This skill should be used when the user asks for Chinese Seedance 2.0 prompt wording, Mandarin cinematic vocabulary, Chinese prompt compression, or translation of camera, lighting, action, VFX, audio, and production terms into Chinese."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - chinese
  - vocabulary
  - seedance-20
metadata:
  version: "5.2.0"
  updated: "2026-05-08"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---


# seedance-vocab-zh

Use Chinese vocabulary when the user asks for Chinese prompts or maximum compactness.

## Core Terms

- Camera: 推镜, 拉镜, 环绕, 跟拍, 低角度, 特写, 中景, 远景
- Motion: 慢慢转身, 快速掠过, 轻微颤动, 稳定推进, 节奏卡点
- Lighting: 逆光, 侧光, 柔光, 冷色月光, 暖色实用灯, 体积光
- Audio: 环境声, 低沉鼓点, 风声, 脚步声, 人声清晰, 口型同步

## Output Contract

Return concise Chinese prompt text and preserve reference tags such as `[Image1]`, `[Video1]`, and `[Audio1]`.
