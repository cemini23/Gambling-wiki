---
title: K125 — Eval gate discipline (distribution shift + sandbox bundle)
type: source
tags: [source, brief, poker, devfun, evaluation, k125]
keywords: [distribution shift, eval cadence, bundle submit, trueskill, selfplay]
related:
  - sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md
  - sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md
  - sources/brief-k123-researcher-jun21-checklist-2026-06-20.md
  - sources/brief-k118-poker-agent-research-gaps-2026-06-17.md
  - concepts/poker-hl-analyst-loop.md
  - entities/bots/cemini-devfun-poker-agent.md
  - sources/daily-digest-reject-cluster-k125-2026-06-22.md
  - sources/brief-k126-garip-selfplay-pm-forecast-steals-2026-06-23.md
  - sources/brief-k129-celeus-tmax-eval-steals-2026-06-25.md
  - sources/arxiv-2606.20820-celeus-llm-eval-eprocesses-2026-06-25.md
maturity: validated
read_status: deep-read
created: 2026-06-22
updated: 2026-06-25
cross-wiki-source: "briefs/2026-06-22_k125-eval-gate-discipline-sandbox-bundle.md"
---

## Relations

- @sources/devfun-researcher-sandbox-bundle-discord-2026-06-20.md — bundle submit + no runtime LLM (K123 Discord)
- @sources/arxiv-2606.14506-distribution-shift-model-eval-2026-06-22.md — shift/selective-label eval steal

## Raw Concept

| Field | Value |
|-------|-------|
| **Brief** | K125 eval discipline + sandbox bundle posture |
| **Date** | 2026-06-22 |

## Narrative

### Sandbox bundle (Discord K123 — confirmed)

- Submit **agent bundle** to researcher sandbox eval — not Playground lobby chips as primary path
- **Pure-code heuristic** aligned with dev recommendation; **avoid LLM BYOK** at this stage (cost + poor performance in their tests)
- **WAIT** on exact bundle layout until follow-up Discord spec — diff against `devfun-org/poker-arena-starter-kit` when published

### Distribution-shift eval steal (2606.14506)

| Pitfall | Mitigation |
|---------|------------|
| Selfplay panel ≠ sandbox pool | Separate HU selfplay locals; don't tune on Playground fish |
| Metrics on analyzed worst hands only | Track **full-session** freq gates + axis summary, not cherry-picked spots |
| Single bb/100 number | Regime table: Playground / Eval S1 / TrueSkill HU — each with own gate |

### Operator checklist addendum

- [ ] Re-read Discord thread for **bundle interface** drop
- [ ] Package `cemini_decide` as bundle when schema published — keep zero runtime LLM
- [ ] Document opponent distribution for each eval gate (shift awareness)

## Dead Ends

- Assuming lobby `pokerkit run` qualifies researcher submit without bundle upload
- Merging selfplay bb/100 into TrueSkill optimization target
