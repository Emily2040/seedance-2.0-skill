---
name: seedance-examples-zh
description: "This skill should be used when the user asks for Chinese Seedance 2.0 examples, Chinese prompt patterns, example rewrites, or safe versions of working Chinese video-generation prompts."
license: MIT
user-invocable: true
user-invokable: true
tags:
  - chinese
  - examples
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


# seedance-examples-zh

Use examples as patterns, not as content to copy blindly.

## Example Labels

- `safe`: original, no protected identity.
- `needs-owned-reference`: relies on user-owned or licensed asset.
- `rewrite-required`: contains protected identity, brand, celebrity, or exact scene.

## Safe Example Pattern

`[Image1]为产品主体，镜头缓慢推进，玻璃瓶身在柔和侧逆光下出现高光流动，背景保持低调深色，细微金色粒子从瓶底上升，环境声安静，最后0.5秒定格产品标志位置但不生成文字。`

## Output Contract

Return the example, label, risk note, and a safer variant if needed.
