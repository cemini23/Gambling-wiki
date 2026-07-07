---
title: K149 — policy SSL embeddings + ADVENT ILP poker steals
type: source
tags: [source, brief, poker, opponent-modeling, k149]
keywords: [policy-embedding, ssl, advent, predicate-invention, leduc, kuhn]
related:
  - sources/daily-digest-batch-k149-2026-07-07.md
  - sources/arxiv-2607.01498-policy-representation-ssl-poker-2026-07-07.md
  - sources/arxiv-2607.01585-advent-ilp-poker-predicate-invention-2026-07-07.md
  - concepts/opponent-modeling-imperfect-info.md
  - concepts/poker-hl-analyst-loop.md
  - entities/tools/rlcard.md
  - sources/brief-k130-rlcard-offline-baseline-adopt-2026-06-26.md
maturity: validated
read_status: deep-read
created: 2026-07-07
updated: 2026-07-07
cross-wiki-source: "briefs/2026-07-07_k149-policy-ssl-advent-poker-steals.md"
---

## Relations

- OSINT arena brief: `agents/devfun-poker-arena/briefs/2026-07-07_k149-policy-ssl-advent-poker-steal.md`
- Private brief: `briefs/2026-07-07_k149-policy-ssl-advent-poker-steals.md`

## Narrative

### Policy SSL steal (2607.01498)

| Idea | David adoption |
|------|----------------|
| **Compact policy embeddings** | Leduc/Kuhn opponent clustering before NLHE — pairs RLCard K130 baselines |
| **Downstream tasks** | Test decode-to-policy + payoff prediction on sandbox selfplay logs |
| **Dataset methods** | Three policy corpus builders — pick one for private opponent archive |
| Phase-0 | **No LICENSE** on `VitamintK/ssl-project` — read paper/methods only until fixed |

### ADVENT steal (2607.01585)

| Idea | David adoption |
|------|----------------|
| **LLM + Prolog verify loop** | Offline invent **named** regression-spot predicates from analyze failures |
| **Knowledge pool** | Reuse verified spot taxonomies across HL epochs (+31pp in paper) |
| **Not hand-ranking** | Poker tasks are ILP benchmark — don't port flush/straight rules to `decide()` |

### Operator checklist

- [ ] Leduc: experiment policy embedding on RLCard selfplay exports (research venv)
- [ ] HL loop: draft Prolog-verifiable spot predicate template for one recurring leak class
- [ ] Phase-0: re-check ssl-project LICENSE before any fork

## Dead Ends

- Embedding k-NN as Playground qualification
- ADVENT 80% hand-ranking as NLHE exploit proof
