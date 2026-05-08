---
name: seedance-vocab-ru
description: "This skill should be used when the user asks for Russian Seedance 2.0 prompt wording, Russian cinematic vocabulary, or translation of camera, lighting, action, VFX, audio, and production terms into Russian."
license: MIT
user-invocable: true
tags:
  - russian
  - vocabulary
  - seedance-20
metadata:
  version: "5.3.0"
  updated: "2026-05-08"
  parent: "seedance-20"
  author: "Iamemily2050 (@iamemily2050)"
  repository: "https://github.com/Emily2040/seedance-2.0"
  openclaw:
    emoji: "🎬"
    homepage: "https://github.com/Emily2040/seedance-2.0"
---

# seedance-vocab-ru

Use Russian cinematic vocabulary when the user asks for Russian prompt wording, bilingual delivery, compact translation, or production vocabulary for camera, lighting, action, VFX, audio, and constraints. Preserve reference tags exactly: `[Image1]`, `[Video1]`, and `[Audio1]` stay unchanged.

## Usage Rule

Translate production intent, not every English word. Russian prompts should stay compact, concrete, and ordered by subject, action, camera, light, sound, and constraint.

| Function | Russian wording |
|---|---|
| Camera | `медленный наезд камеры`, `боковое сопровождение`, `фиксированный средний план`, `низкий ракурс`, `крупный план` |
| Lighting | `контровой свет`, `мягкий свет из окна`, `теплый практический источник`, `холодный лунный свет`, `контурная подсветка` |
| Motion | `медленно поворачивается`, `быстро проходит через кадр`, `капли стекают вниз`, `дым мягко рассеивается` |
| Audio | `тихий фон помещения`, `короткая реплика`, `мягкий металлический щелчок`, `без музыки` |
| Constraints | `сохранить логотип, этикетку и форму без изменений` |

## Compact Pattern

`[Image1] — референс; сохранить лицо/форму продукта/логотип точно без изменений. Меняются только [движение/свет/камера]. Камера: [одно движение]. Звук: [аудио-сигнал].`

## Output Contract

Return Russian prompt wording, optional English gloss when useful, and unchanged reference tags.
