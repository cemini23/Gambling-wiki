"""rss_digest: XML parsing, filtering, and inbox stub writing. No network calls."""

from __future__ import annotations

import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))

from rss_digest import (  # noqa: E402
    FeedOutcome,
    RssItem,
    filter_items,
    parse_feed_datetime,
    parse_feed_xml,
    slugify_title,
    write_inbox_stubs,
)

DAY = datetime(2026, 9, 1, 12, 0, tzinfo=timezone.utc)
CUTOFF = datetime(2026, 8, 1, tzinfo=timezone.utc)


def _item(
    *,
    feed_id: str = "legal-sports-report",
    title: str = "Kalshi Expands Sports Markets",
    url: str = "https://example.com/a",
    published: datetime | None = DAY,
    wiki_hit: str | None = None,
) -> RssItem:
    return RssItem(
        feed_id=feed_id,
        feed_name=feed_id.replace("-", " ").title(),
        cluster="us-sports-betting-legal",
        title=title,
        url=url,
        published=published,
        wiki_hit=wiki_hit,
    )


def _outcome(feed_id: str = "legal-sports-report", items: list[RssItem] | None = None) -> FeedOutcome:
    return FeedOutcome(
        feed_id=feed_id,
        feed_name=feed_id.replace("-", " ").title(),
        cluster="us-sports-betting-legal",
        url=f"https://example.com/{feed_id}/feed",
        items=list(items or []),
    )


# --- parsing / filtering (no network) --------------------------------------


def test_parse_feed_datetime_rfc822_and_iso():
    assert parse_feed_datetime("Tue, 01 Sep 2026 12:00:00 GMT") == DAY
    assert parse_feed_datetime("2026-09-01T12:00:00Z") == DAY
    assert parse_feed_datetime("not-a-date") is None
    assert parse_feed_datetime(None) is None


def test_parse_feed_xml_rss_and_atom():
    rss = (
        b'<?xml version="1.0"?><rss version="2.0"><channel>'
        b"<item><title>Alpha</title><link>https://example.com/alpha</link>"
        b"<pubDate>Tue, 01 Sep 2026 12:00:00 GMT</pubDate></item>"
        b"</channel></rss>"
    )
    rows = parse_feed_xml(rss)
    assert rows == [("Alpha", "https://example.com/alpha", DAY)]

    atom = (
        b'<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom">'
        b'<entry><title>Beta</title><link href="https://example.com/beta"/>'
        b"<updated>2026-09-01T12:00:00Z</updated></entry></feed>"
    )
    rows = parse_feed_xml(atom)
    assert rows == [("Beta", "https://example.com/beta", DAY)]


def test_filter_items_respects_cutoff_and_excludes():
    rows = [
        ("Keep me", "https://example.com/keep", DAY),
        ("Drop old", "https://example.com/old", datetime(2026, 1, 1, tzinfo=timezone.utc)),
        ("Fantasy Football Rankings", "https://example.com/rank", DAY),
    ]
    kept = filter_items(
        rows,
        cutoff=CUTOFF,
        include_any=None,
        exclude_any=["Fantasy Football Rankings"],
        max_items=5,
    )
    assert [row[0] for row in kept] == ["Keep me"]


def test_filter_items_max_items():
    rows = [(f"Story {i}", f"https://example.com/{i}", DAY) for i in range(10)]
    kept = filter_items(rows, cutoff=CUTOFF, include_any=None, exclude_any=None, max_items=3)
    assert len(kept) == 3


# --- inbox stubs ------------------------------------------------------------


def test_slugify_title():
    assert slugify_title("Kalshi's Big Win!") == "kalshi-s-big-win"
    assert slugify_title("") == "untitled"


def test_write_inbox_stubs_creates_markdown_pointer(tmp_path):
    written = write_inbox_stubs(tmp_path, [_outcome(items=[_item()])], max_files=8)
    assert len(written) == 1
    path = written[0]
    assert path.parent == tmp_path / "research to be indexed"
    assert path.name == "rss-legal-sports-report-2026-09-01-kalshi-expands-sports-markets.md"
    text = path.read_text(encoding="utf-8")
    assert "Kalshi Expands Sports Markets" in text
    assert "https://example.com/a" in text
    assert "legal-sports-report" in text
    assert "2026-09-01" in text
    assert "discovery stub" in text.lower()
    assert "<" not in text  # no HTML


def test_write_inbox_stubs_uses_tempfile_module():
    with tempfile.TemporaryDirectory() as tmp:
        written = write_inbox_stubs(Path(tmp), [_outcome(items=[_item(title="Temp Story")])])
        assert len(written) == 1
        assert written[0].is_file()
        assert (Path(tmp) / "research to be indexed").is_dir()


def test_write_inbox_stubs_skips_wiki_hits(tmp_path):
    outcome = _outcome(items=[_item(wiki_hit="wiki/sources/kalshi.md")])
    assert write_inbox_stubs(tmp_path, [outcome]) == []
    inbox = tmp_path / "research to be indexed"
    assert list(inbox.iterdir()) == []


def test_write_inbox_stubs_skips_configured_feed_ids(tmp_path):
    outcome = _outcome(feed_id="event-horizon", items=[_item(feed_id="event-horizon")])
    written = write_inbox_stubs(
        tmp_path,
        [outcome],
        skip_ids=["event-horizon", "the-closing-line", "outlier-weekly"],
    )
    assert written == []


def test_write_inbox_stubs_caps_files(tmp_path):
    items = [_item(title=f"Story {i}", url=f"https://example.com/{i}") for i in range(10)]
    written = write_inbox_stubs(tmp_path, [_outcome(items=items)], max_files=8)
    assert len(written) == 8


def test_write_inbox_stubs_is_idempotent(tmp_path):
    outcome = _outcome(items=[_item()])
    first = write_inbox_stubs(tmp_path, [outcome])
    second = write_inbox_stubs(tmp_path, [outcome])
    assert len(first) == 1
    assert second == []


def test_write_inbox_stubs_handles_missing_date(tmp_path):
    written = write_inbox_stubs(tmp_path, [_outcome(items=[_item(published=None)])])
    assert len(written) == 1
    assert "unknown" in written[0].read_text(encoding="utf-8")


def test_write_inbox_stubs_max_files_zero_is_noop(tmp_path):
    assert write_inbox_stubs(tmp_path, [_outcome(items=[_item()])], max_files=0) == []


# --- config wiring ----------------------------------------------------------


def test_config_enables_inbox_stubs():
    import yaml

    cfg_path = Path(__file__).resolve().parents[1] / "scripts" / "daily_research_config.yaml"
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    rss = cfg["rss"]
    assert rss["write_inbox"] is True
    assert int(rss["inbox_max_files"]) == 8
    skip = list(rss["inbox_skip_feed_ids"])
    assert "event-horizon" in skip
    assert "the-closing-line" in skip
    assert "outlier-weekly" in skip


if __name__ == "__main__":
    import pytest

    raise SystemExit(pytest.main([__file__, "-q"]))
