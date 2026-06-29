---
title: K133 — RQGM co-evolving evaluator steals for arena harness
type: source
tags: [source, brief, agents, evaluator, k133, rqgm]
keywords: [red-queen-godel-machine, utility-evolution, epoch, agent-as-judge, sandbox]
related:
  - sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md
  - sources/daily-digest-reject-cluster-k133-2026-06-29.md
  - sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md
  - sources/arxiv-2606.25819-toolbench-x-tool-unreliability-2026-06-26.md
  - sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md
  - sources/devfun-sandbox-researcher-guide-2026-06-26.md
  - concepts/custom-agent-methodology.md
  - concepts/poker-hl-analyst-loop.md
  - concepts/gambling-bot-architecture.md
maturity: validated
read_status: deep-read
created: 2026-06-29
updated: 2026-06-29
cross-wiki-source: "briefs/2026-06-29_k133-rqgm-co-evolving-evaluator-steals.md"
---

## Relations

- @sources/arxiv-2606.26294-red-queen-godel-machine-2026-06-29.md — RQGM framework
- @sources/arxiv-2606.20785-fara-computer-use-agents-2026-06-27.md — fixed verifier triad (K132)
- Private brief: `briefs/2026-06-29_k133-rqgm-co-evolving-evaluator-steals.md`
- OSINT arena brief: `agents/devfun-poker-arena/briefs/2026-06-29_k133-rqgm-co-evolving-evaluator-steal.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K133 RQGM evaluator co-evolution steals |
| **Date** | 2026-06-29 |
| **Batch** | K133 daily digest (3 PDFs) |

## Narrative

### RQGM steal (2606.26294) — non-stationary eval for HL + sandbox

| RQGM idea | Arena analogue |
|-----------|----------------|
| **Epoch + fixed within-epoch utility** | Version private regression gates per HL patch generation; change eval weights only at epoch boundary |
| **Co-evolved agent-as-judge** | Cheap single-pass reviewer alongside pytest/regression (pairs K132 Fara verifiers) |
| **Adversarial utility epoch** | When PvE panel over-accepts weak bundles, add epoch objective penalizing AI/human asymmetry |
| **Token efficiency** | Prefer one-shot judge over multi-turn harness replay when screening bundles |

| Idea | Action |
|------|--------|
| Controlled utility evolution | Document eval-epoch changelog in private HL loop — don't silently drift gates mid-competition |
| Phase-0 | **Paper-only** — watch for Cambridge official release; community MIT repro **unvalidated** |
| CELEUS (K129) | Pair epoch boundaries with anytime-valid CI reporting on judge agreement |

### Rejects

| arXiv | Reason |
|-------|--------|
| 2606.22922 | Commutative algebra HRL — math conjecture search |
| 2606.26397 | Academic MOMDP Pareto synthesis — no DFS lineup hook |

### Operator checklist addendum

- [ ] Define **eval epoch** ID in private preflight metadata (utility vector frozen within epoch)
- [ ] After major `decide()` refactors, review whether regression corpus still discriminates (Red Queen drift)
- [ ] Optional: lightweight agent-as-judge pass on sandbox `reasoning_text` before full bundle sim
- [ ] Do **not** recursive self-edit `decide()` via RQGM during live event

## Dead Ends

- RQGM on prod wagering bots
- Chebyshev MOMDP for pydfs objective weights
- HRL options for preflop chart discovery
