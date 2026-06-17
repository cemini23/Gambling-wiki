#!/usr/bin/env python3
"""Download non-duplicate research PDFs (arXiv, OpenReview) from digest hits into inbox."""

from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from wiki_source_index import (  # noqa: E402
    arxiv_id_from_url,
    build_wiki_index,
    inbox_paper_ids,
    openreview_id_from_url,
    verdict_for_remote_hit,
)


@dataclass
class FetchOutcome:
    cluster: str
    title: str
    url: str
    paper_id: str | None
    source: str  # arxiv | openreview | —
    status: str  # fetched | skipped-dup | skipped-likely | skipped-unsupported | skipped-cap | failed
    path: str | None = None
    detail: str = ""

    @property
    def arxiv_id(self) -> str | None:
        """Backward-compatible alias for sweep renderers."""
        return self.paper_id if self.source == "arxiv" else None


def safe_slug(title: str, max_len: int = 48) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return (slug[:max_len] or "paper").strip("-")


def inbox_dest(inbox: Path, source: str, paper_id: str, title: str) -> Path:
    return inbox / f"{source}-{paper_id}-{safe_slug(title)}.pdf"


def download_pdf(url: str, dest: Path) -> None:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "cemini-daily-digest/1.0 (gambling-wiki)"},
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read()
    if len(data) < 1024 or not data[:5].startswith(b"%PDF"):
        raise ValueError("response is not a PDF")
    dest.write_bytes(data)


def resolve_paper_hit(url: str, enabled_sources: list[str]) -> tuple[str, str] | None:
    if "arxiv" in enabled_sources:
        aid = arxiv_id_from_url(url)
        if aid:
            return "arxiv", aid
    if "openreview" in enabled_sources:
        oid = openreview_id_from_url(url)
        if oid:
            return "openreview", oid
    return None


def fetch_papers(
    repo: Path,
    paper_sections: list[tuple[str, str, str | None, list[dict]]],
    *,
    max_downloads: int,
    fetch_likely: bool = False,
    sources: list[str] | None = None,
) -> list[FetchOutcome]:
    enabled = [s.lower() for s in (sources or ["arxiv"])]
    inbox = repo / "research to be indexed"
    inbox.mkdir(parents=True, exist_ok=True)
    sources_dir = repo / "wiki" / "sources"
    idx = build_wiki_index(sources_dir)
    pending = inbox_paper_ids(inbox)

    outcomes: list[FetchOutcome] = []
    downloaded = 0
    seen: set[tuple[str, str]] = set()

    for cluster, _query, _category, results in paper_sections:
        for r in results:
            url = (r.get("url") or "").strip()
            title = (r.get("title") or "").strip() or "(no title)"
            resolved = resolve_paper_hit(url, enabled)

            if not resolved:
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, None, "—", "skipped-unsupported",
                        detail=f"not in fetch sources ({', '.join(enabled)})",
                    )
                )
                continue

            source, paper_id = resolved
            key = (source, paper_id)
            if key in seen:
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, paper_id, source, "skipped-dup",
                        detail="duplicate in this run",
                    )
                )
                continue
            seen.add(key)

            verdict, notes = verdict_for_remote_hit(
                url, title, idx, pending, source=source, paper_id=paper_id
            )
            if verdict == "DUPLICATE":
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, paper_id, source, "skipped-dup",
                        detail="; ".join(notes) or verdict,
                    )
                )
                continue
            if verdict == "LIKELY" and not fetch_likely:
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, paper_id, source, "skipped-likely",
                        detail="; ".join(notes) or verdict,
                    )
                )
                continue

            if downloaded >= max_downloads:
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, paper_id, source, "skipped-cap",
                        detail=f"cap {max_downloads}",
                    )
                )
                continue

            dest = inbox_dest(inbox, source, paper_id, title)
            if dest.is_file():
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, paper_id, source, "skipped-dup",
                        dest.name, "file exists",
                    )
                )
                pending[source].add(paper_id)
                continue

            pdf_url = (
                f"https://arxiv.org/pdf/{paper_id}.pdf"
                if source == "arxiv"
                else f"https://openreview.net/pdf?id={paper_id}"
            )
            try:
                download_pdf(pdf_url, dest)
                downloaded += 1
                pending[source].add(paper_id)
                outcomes.append(
                    FetchOutcome(cluster, title, url, paper_id, source, "fetched", dest.name)
                )
            except (urllib.error.URLError, OSError, ValueError) as e:
                outcomes.append(
                    FetchOutcome(
                        cluster, title, url, paper_id, source, "failed", detail=str(e)[:200]
                    )
                )

    return outcomes
