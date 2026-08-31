#!/usr/bin/env python3
"""Free RSS/Atom discovery for the gambling-wiki daily digest.

Discovery-only: list recent items in the sweep report. Does not write inbox
files or fetch article bodies (OSINT Substack poller already dumps EH / Closing
Line / Outlier into the OSINT inbox with cross_wiki: gambling-wiki).

Presence of this file is the federation-sync guard: OSINT
`sync_federation_digest_bundle.sh` will not overwrite
`daily_research_digest_run.py` while this module exists.
"""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from wiki_source_index import normalize_url  # noqa: E402


DEFAULT_UA = "CeminiGambling-RSSDigest/1.0 (+local research wiki)"


@dataclass
class RssItem:
    feed_id: str
    feed_name: str
    cluster: str
    title: str
    url: str
    published: datetime | None
    wiki_hit: str | None = None  # path if already in wiki


@dataclass
class FeedOutcome:
    feed_id: str
    feed_name: str
    cluster: str
    url: str
    items: list[RssItem] = field(default_factory=list)
    error: str | None = None
    raw_count: int = 0


def _local(tag: str) -> str:
    return tag.split("}")[-1].lower() if tag else ""


def parse_feed_datetime(raw: str | None) -> datetime | None:
    text = (raw or "").strip()
    if not text:
        return None
    try:
        dt = parsedate_to_datetime(text)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except (TypeError, ValueError, OverflowError):
        pass
    iso = text.replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(iso)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except ValueError:
        return None


def _el_text(el: ET.Element | None) -> str:
    if el is None:
        return ""
    return "".join(el.itertext()).strip()


def parse_feed_xml(xml_bytes: bytes) -> list[tuple[str, str, datetime | None]]:
    """Return (title, url, published) for RSS 2.0 or Atom entries."""
    root = ET.fromstring(xml_bytes)
    out: list[tuple[str, str, datetime | None]] = []
    for el in root.iter():
        kind = _local(el.tag)
        if kind not in ("item", "entry"):
            continue
        title = ""
        link = ""
        published: datetime | None = None
        guid = ""
        for child in list(el):
            ct = _local(child.tag)
            if ct == "title":
                title = _el_text(child)
            elif ct == "link":
                href = (child.attrib.get("href") or _el_text(child)).strip()
                rel = (child.attrib.get("rel") or "alternate").lower()
                if href and (rel in ("alternate", "") or not link):
                    link = href
                    if rel == "alternate" and href:
                        pass
            elif ct in ("pubdate", "published", "updated", "date"):
                if published is None:
                    published = parse_feed_datetime(_el_text(child))
            elif ct == "guid":
                guid = _el_text(child)
        url = link or guid
        if not url:
            continue
        out.append((title or "(no title)", url, published))
    return out


def fetch_feed_bytes(url: str, user_agent: str, timeout: int = 20) -> bytes:
    req = Request(
        url,
        headers={
            "User-Agent": user_agent,
            "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
        },
    )
    with urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _matches_any(text: str, needles: list[str] | None) -> bool:
    if not needles:
        return False
    hay = text.lower()
    return any(n.lower() in hay for n in needles)


def filter_items(
    rows: list[tuple[str, str, datetime | None]],
    *,
    cutoff: datetime,
    include_any: list[str] | None,
    exclude_any: list[str] | None,
    max_items: int,
) -> list[tuple[str, str, datetime | None]]:
    kept: list[tuple[str, str, datetime | None]] = []
    for title, url, published in rows:
        if published is not None and published < cutoff:
            continue
        blob = f"{title} {url}"
        if exclude_any and _matches_any(blob, exclude_any):
            continue
        if include_any and not _matches_any(blob, include_any):
            continue
        kept.append((title, url, published))
        if len(kept) >= max_items:
            break
    return kept


def run_rss_feeds(
    cfg: dict[str, Any],
    *,
    from_date: datetime,
    wiki_urls: dict[str, list[str]] | None = None,
    seen_urls: set[str] | None = None,
) -> list[FeedOutcome]:
    rss_cfg = dict(cfg.get("rss") or {})
    if not rss_cfg.get("enabled", True):
        return []
    ua = str(rss_cfg.get("user_agent") or DEFAULT_UA)
    default_max = int(rss_cfg.get("max_items_per_feed", 5))
    seen = seen_urls if seen_urls is not None else set()
    outcomes: list[FeedOutcome] = []

    for row in rss_cfg.get("feeds") or []:
        if not row.get("enabled", True):
            continue
        feed_id = str(row.get("id") or "unknown")
        name = str(row.get("name") or feed_id)
        cluster = str(row.get("cluster") or feed_id)
        feed_url = str(row.get("url") or "")
        outcome = FeedOutcome(
            feed_id=feed_id, feed_name=name, cluster=cluster, url=feed_url
        )
        if not feed_url:
            outcome.error = "missing url"
            outcomes.append(outcome)
            continue
        try:
            raw = fetch_feed_bytes(feed_url, ua)
            parsed = parse_feed_xml(raw)
            outcome.raw_count = len(parsed)
        except HTTPError as e:
            outcome.error = f"HTTP {e.code}"
            outcomes.append(outcome)
            print(f"WARNING: rss {feed_id} HTTP {e.code}", file=sys.stderr)
            continue
        except (URLError, TimeoutError, OSError, ET.ParseError) as e:
            outcome.error = str(e)[:120]
            outcomes.append(outcome)
            print(f"WARNING: rss {feed_id} {e}", file=sys.stderr)
            continue

        max_items = int(row.get("max_items") or default_max)
        include_any = list(row["include_any"]) if row.get("include_any") else None
        exclude_any = list(row["exclude_any"]) if row.get("exclude_any") else None
        filtered = filter_items(
            parsed,
            cutoff=from_date,
            include_any=include_any,
            exclude_any=exclude_any,
            max_items=max_items,
        )
        for title, url, published in filtered:
            key = normalize_url(url)
            if not key or key in seen:
                continue
            seen.add(key)
            wiki_hit = None
            if wiki_urls and key in wiki_urls:
                wiki_hit = wiki_urls[key][0]
            outcome.items.append(
                RssItem(
                    feed_id=feed_id,
                    feed_name=name,
                    cluster=cluster,
                    title=title,
                    url=url,
                    published=published,
                    wiki_hit=wiki_hit,
                )
            )
        outcomes.append(outcome)
    return outcomes


def render_rss_section(outcomes: list[FeedOutcome]) -> tuple[list[str], int]:
    lines = [
        "---",
        "",
        "## RSS & practitioner feeds (not auto-downloaded)",
        "",
        "_Free RSS/Atom — no Exa credits. Discovery-only; check a row then **full ingest**. "
        "Event Horizon / Closing Line / Outlier also land in the OSINT inbox (`cross_wiki: gambling-wiki`)._",
        "",
    ]
    total = 0
    row_id = 0
    if not outcomes:
        lines.append("_Skipped — `rss.enabled: false`._")
        lines.append("")
        return lines, 0

    for outcome in outcomes:
        n = len(outcome.items)
        status = outcome.error or f"{n} hits"
        lines.append(f"### {outcome.feed_name} (`{outcome.cluster}` · {status})")
        lines.append("")
        if outcome.error:
            lines.append(f"_Feed error: `{outcome.error}` — `{outcome.url}`_")
            lines.append("")
            continue
        lines.append("| Pick | Date | Title | Feed | URL |")
        lines.append("|------|------|-------|------|-----|")
        if not outcome.items:
            lines.append("| — | | _no new items in window_ | | |")
            lines.append("")
            continue
        for item in outcome.items:
            row_id += 1
            d = item.published.date().isoformat() if item.published else ""
            title = item.title.replace("|", "\\|")[:100]
            url = item.url
            mark = "x" if item.wiki_hit else " "
            wiki = f" _(wiki: `{item.wiki_hit}`)_" if item.wiki_hit else ""
            url_cell = f"{url[:60]}…" if len(url) > 60 else url
            lines.append(
                f"| [{mark}] S{row_id} | {d} | [{title}]({url}){wiki} | {item.feed_id} | {url_cell} |"
            )
            if not item.wiki_hit:
                total += 1
        lines.append("")
    return lines, total


def main() -> int:
    """Dry-run from repo root: python3 scripts/rss_digest.py"""
    from pathlib import Path

    import yaml

    repo = Path(__file__).resolve().parent.parent
    cfg_path = repo / "scripts" / "daily_research_config.yaml"
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    window = int((cfg.get("rss") or {}).get("max_age_days") or 7)
    cutoff = datetime.now(timezone.utc) - timedelta(days=window)
    outcomes = run_rss_feeds(cfg, from_date=cutoff)
    lines, new_n = render_rss_section(outcomes)
    print("\n".join(lines))
    print(f"# new (not already in wiki): {new_n}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
