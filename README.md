# Gambling & Betting Wiki

> Public knowledge hub for **sports betting, casino games, poker, DFS, best ball, and prediction-market wagering** (consumer/strategy angle). LLM-managed, human-read.

## What this is

This workspace is a **librarian** for betting and gambling research. It:

- **Manages** raw sources (books, PDFs, course notes, repo snapshots, transcripts) you drop into `research to be indexed/`
- **Curates** them into an interlinked wiki under `wiki/` — platforms, tools, games, sports, and strategy concepts
- **Applies** them via briefs in `briefs/` for slate prep, study plans, and bankroll frameworks

## Quick start

1. Read `CLAUDE.md` — schema the LLM follows each session
2. Read `ROADMAP.md` — active workstreams
3. Copy `.env.example` → `.env` (optional Exa/Brave keys for external research)
4. Drop a source into `research to be indexed/` and ask Claude/Cursor to ingest it
5. Lint: `python3 scripts/wiki_lint.py`

## Folder layout

```
Gambling-wiki/
  CLAUDE.md
  README.md
  LESSONS.md
  ROADMAP.md
  wiki/
    index.md              # catalog
    log.md                # operations log
    entities/
      platforms/          # sportsbooks, DFS sites, PM venues, poker rooms
      tools/              # odds services, optimizers, trackers
      games/              # poker, blackjack, craps, …
      sports/             # NFL, NBA, …
      people/
    concepts/             # bankroll, Kelly, DFS, house edge, …
    sources/
  scripts/                # wiki_lint.py, preingest_check.py
  prompts/
```

## Cemini wiki federation

**Seven** wikis + private **Cemini Financial Suite**. Cross-links: `@<alias>/path/to/page.md` (`CLAUDE.md` → Related Wikis).

| Alias | Repository | Focus |
|-------|------------|--------|
| **`gambling-wiki`** | **This repo** | Sports betting, casino, poker, DFS, best ball |
| `osint-wiki` | *private* | Prediction-market bots, CeminiSuite, quant OSINT |
| `ccc-wiki` | [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC) | Agent workflow, MCP, skills |
| `cybersecurity-wiki` | [Cybersecurity-wiki](https://github.com/cemini23/Cybersecurity-wiki) | Pentest, SOC |
| `seo-wiki` | [SEO-GEO-B-M-Wiki](https://github.com/cemini23/SEO-GEO-B-M-Wiki) | Local SEO, creator ops |
| `3d-printing-wiki` | [3D-Printing-Wiki](https://github.com/cemini23/3D-Printing-Wiki) | FDM/print farms |
| `image-gen-wiki` | [uncensored-image-gen-wiki](https://github.com/cemini23/uncensored-image-gen-wiki) | ComfyUI, LoRA |

Cross-links: `@gambling-wiki/concepts/bankroll-management.md` ↔ `@osint-wiki/concepts/kelly-sizing-quarter.md`

```bash
git clone https://github.com/cemini23/Gambling-wiki.git
```

## Privacy

- `.env`, `raw-sources/`, `briefs/`, `hot.md` are gitignored
- Never commit API keys, account credentials, or sportsbook PII

## Related

- Wiki federation hub: [cemini-claude-code-CCC](https://github.com/cemini23/cemini-claude-code-CCC)
- Tooling: [wikilint](https://github.com/cemini23/wikilint) · [vet](https://github.com/cemini23/vet)

## License

MIT — see `LICENSE`.
