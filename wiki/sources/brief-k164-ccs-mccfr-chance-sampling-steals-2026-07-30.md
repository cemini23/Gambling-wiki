---
title: Brief K164 — CCS-MCCFR chance-sampling steals
type: source
tags: [brief, k164, poker, mccfr, cfr, steals]
keywords: [k164, 2607.27035, ccs-mccfr, weyl, external-sampling, linear-cfr]
related:
  - meta/daily-research-digest-cadence.md
  - sources/daily-digest-batch-k164-2026-07-30.md
  - sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/bots/poker-bot-tooling.md
  - entities/tools/rlcard.md
  - sweeps/2026-07-30-daily.md
maturity: validated
read_status: deep-read
created: 2026-07-30
updated: 2026-07-30
cross-wiki-source: "briefs/2026-07-30_k164-ccs-mccfr-chance-sampling-steals.md"
---

## Relations

- Wiki: `briefs/2026-07-30_k164-ccs-mccfr-chance-sampling-steals.md`
- OSINT arena: `agents/devfun-poker-arena/briefs/2026-07-30_k164-ccs-mccfr-chance-sampling-steal.md`

## Raw Concept

K164 steals — **persistent Weyl chance streams** for offline MCCFR; compose with **Linear CFR**; do not touch `decide()`.

## Narrative

1. If any research-branch MCCFR / OpenSpiel / TexasSolver bake uses i.i.d. chance draws, evaluate CCS (per-node persistent randomized Weyl) as a one-line sampler swap.
2. Prefer Linear CFR + CCS when composing update rules (paper’s best Leduc cell).
3. Re-measure on target game class — gains strong on Kuhn/Leduc, muted on HUNL endgames in paper.
4. Keep as offline blueprint / exploitability hygiene; never a Playground submit gate alone.

## Sources

- @sources/arxiv-2607.27035-ccs-mccfr-2026-07-30.md
