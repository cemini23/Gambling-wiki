---
title: Brief K167 — self-fictitious-play MFG shelf
type: source
tags: [brief, k167, game-theory, fictitious-play, mean-field]
keywords: [k167, 2608.15258, sfp, mfg, shelf]
related:
  - meta/daily-research-digest-cadence.md
  - sources/daily-digest-batch-k167-2026-08-18.md
  - sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - sources/brief-k157-fbsde-fictitious-play-shelf-2026-07-16.md
  - sources/brief-k166-regret-learning-games-shelf-2026-08-12.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - sweeps/2026-08-18-daily.md
maturity: validated
read_status: deep-read
created: 2026-08-18
updated: 2026-08-18
wire_status: wont_wire
cross-wiki-source: "briefs/2026-08-18_k167-sfp-mfg-shelf.md"
---

## Relations

- Wiki: `briefs/2026-08-18_k167-sfp-mfg-shelf.md`
- OSINT arena: `agents/devfun-poker-arena/briefs/2026-08-18_k167-sfp-mfg-shelf.md`
- Phase-1: `wont_wire` — REFERENCE-only; no ADOPT-GO runtime

## Raw Concept

K167 shelf — ergodic MFG **self-fictitious-play** (own occupation-measure belief; `O(√λ)` to Nash). **Do not** import into decide()/HL. Phase-0 REFERENCE; FOSS none.

**Dual-ID:** gambling digest K167 ≠ OSINT K167 (Jul 15 Kalshi-flight brief).

## Narrative

1. 2608.15258 Bai / Laurière / Ren / Wang: SFP couples optimal feedback to a slowly evolving self-occupation belief `d m_t = λ (δ_{X_t} − m_t) dt` — not population McKean–Vlasov. Contractive on monotone potential ergodic MFGs on `T^d`; unique invariant law; Wasserstein neighborhood `O(√λ)` of MFG Nash, sharp on LQ §4.1.
2. Shelf next to K157 (continuous FBSDE-FP), K166 (FTRL/FP literacy), K124 (discrete MAFP). Continuous torus MFG ≠ HU poker.
3. No FOSS; no atto / GuruWatcher / CeminiDFS / TipDrop / prod scp.

## Sources

- @sources/arxiv-2608.15258-self-fictitious-play-mfg-2026-08-18.md
