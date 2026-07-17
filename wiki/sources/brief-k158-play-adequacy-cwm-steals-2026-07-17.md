---
title: Brief K158 — play-adequacy Code World Model steals
type: source
tags: [brief, k158, poker, agents, eval, world-models]
keywords: [k158, play-adequacy, danger-law, cwm, verified-vs-correct]
related:
  - sources/daily-digest-batch-k158-2026-07-17.md
  - sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md
  - entities/tools/code-world-models.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/custom-agent-methodology.md
  - concepts/opponent-modeling-imperfect-info.md
  - sweeps/2026-07-17-daily.md
maturity: validated
read_status: deep-read
created: 2026-07-17
updated: 2026-07-17
cross-wiki-source: "briefs/2026-07-17_k158-play-adequacy-cwm-steals.md"
---

## Relations

- Wiki: `briefs/2026-07-17_k158-play-adequacy-cwm-steals.md`
- OSINT arena: `agents/devfun-poker-arena/briefs/2026-07-17_k158-play-adequacy-gate-steal.md`
- CCC prod: `briefs/2026-07-17_k158-play-adequacy-world-model-eval-prod.md`

## Raw Concept

K158 steals — **play-adequacy over transition accuracy**, **danger law**, **imperfect-info inference coverage**.

## Narrative

1. Ship gates: prefer play / search-distribution checks over sampling transition accuracy.
2. Rare-but-pivotal omissions: `danger = play_cost × (1−rarity)^N` — enlarge N or adversarially sample pivotal regions.
3. Completing the specification beats more example transitions (translation ≠ inference).
4. Belief/`infer_states` functions need their own identifying gates (Kuhn covered; Leduc not fully).

## Sources

- @sources/arxiv-2607.14169-play-adequacy-code-world-models-2026-07-17.md
