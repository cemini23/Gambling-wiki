---
title: Tennis betting (retail)
type: entity
tags: [entity, sport, tennis, live-betting]
keywords: [tennis, in-play, grand-slam, live-betting, hawk-eye]
related:
  - concepts/sports-betting-fundamentals.md
  - concepts/live-betting-match-integrity.md
  - sources/arxiv-2609.07617-live-tennis-forecasting-2026-09-11.md
  - sources/daily-digest-batch-k170-2026-09-11.md
maturity: draft
created: 2026-09-11
updated: 2026-09-11
---

## Relations

- @concepts/sports-betting-fundamentals.md — live betting product lane
- @concepts/live-betting-match-integrity.md — in-play integrity context
- @sources/arxiv-2609.07617-live-tennis-forecasting-2026-09-11.md — Trace hybrid live model (REFERENCE)

## Raw Concept

Retail tennis wagering — pre-match and in-play — on regulated sportsbooks and (where legal) prediction markets.

## Narrative

Tennis is a major **in-play** sport: roughly **80%** of tennis handle may be placed live [TENTATIVE — arXiv 2609.07617 cites industry reports]. Point-by-point state (score, serve advantage, break points) feeds live models; Hawk-Eye and similar systems add shot-level context.

**K170 (2609.07617):** hybrid **Trace** model reported 76–88% winner accuracy at 25–75% match progress on Grand Slam test years 2023–2024. Literacy only — not a deployed edge or bot lane in this wiki.

For bot/automation scope: out of W4 first-lane priority unless operator reopens.

## Snippets

> "Approximately 80% of the money wagered on tennis matches has been reported to be placed in-play." [Source: arxiv:2609.07617 §1]
