---
title: StreamMemBench — streaming agent memory evaluation (arXiv 2606.14571)
type: source
tags: [source, arxiv, agent-memory, evaluation, k124, k118]
keywords: [streammembench, agent memory, feedback reuse, evidence recall, future-oriented]
related:
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/custom-agent-methodology.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - sources/brief-k124-mafp-memory-poker-steals-2026-06-21.md
  - sources/arxiv-2606.19308-mafp-multi-agent-fictitious-play-2026-06-21.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/daily-digest-reject-cluster-k124-2026-06-21.md
  - sweeps/2026-06-21-daily.md
maturity: draft
read_status: skimmed
created: 2026-06-21
updated: 2026-06-21
location: cemini-egress-fi:/opt/cemini-bulk/research/gambling/arxiv-2606.14571-2606-14571v1-streammembench-streaming-evaluation.pdf
phase_0_verdict: REFERENCE 2026-06-21 — memory eval benchmark; not poker domain
---

## Relations

- @sources/brief-k118-poker-agent-research-gaps-2026-06-17.md — F6 thin session memory gap
- @concepts/poker-hl-analyst-loop.md — offline patch loop vs streaming memory carry-forward

## Raw Concept

| Field | Value |
|-------|-------|
| **arXiv** | [2606.14571](https://arxiv.org/abs/2606.14571) |
| **Domain** | Personal-agent memory from egocentric (EgoLife) streams |
| **Verdict** | **REFERENCE** — eval methodology for memory reuse, not NLHE content |

## Narrative

StreamMemBench tests whether agent memory turns **stored observations + feedback** into **future-task assistance** — two-step task sequences per evidence anchor. Metrics: evidence recall, initial evidence use, feedback incorporation, follow-up reuse.

Eight memory systems tested: systems often **store evidence but fail follow-up reuse** even when local feedback is incorporated.

### K118 F6 steal (poker arena)

Map to **session_memory / showdown queue** spec:

| StreamMemBench metric | Arena analog |
|-----------------------|--------------|
| Evidence recall | Villain hand history in HUD |
| Feedback incorporation | HL patch from analyze worst hand |
| Follow-up reuse | Next session vs same villain_id exploits prior leak |

Not a poker paper — use as **eval rubric** when expanding F6 beyond aggression counts.

## Snippets

> "Useful cues must be carried forward from the current request to similar future tasks." [Source: arxiv:2606.14571 abstract]

## Dead Ends

- Ingesting as NLHE strategy source — wrong domain (personal assistant / egocentric video)
