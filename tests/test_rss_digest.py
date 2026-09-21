#!/usr/bin/env python3
"""Unit tests for gambling RSS inbox stubs. No network."""

from __future__ import annotations

import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _add_sys_path(path: Path) -> None:
    if path.is_dir() and str(path) not in sys.path:
        sys.path.insert(0, str(path))


_add_sys_path(HERE)
_add_sys_path(HERE.parent / "scripts")
for parent in HERE.parents:
    if (parent / "wiki_source_index.py").is_file():
        _add_sys_path(parent)
        break
    if (parent / "scripts" / "wiki_source_index.py").is_file():
        _add_sys_path(parent / "scripts")
        break

from rss_digest import FeedOutcome, RssItem, inbox_slug, write_inbox_stubs  # noqa: E402


def _item(
    feed_id: str,
    title: str,
    *,
    wiki_hit: str | None = None,
    day: str = "2026-09-16",
) -> RssItem:
    published = datetime.fromisoformat(f"{day}T12:00:00+00:00").astimezone(timezone.utc)
    return RssItem(
        feed_id=feed_id,
        feed_name=feed_id.replace("-", " ").title(),
        cluster=feed_id,
        title=title,
        url=f"https://example.test/{feed_id}/{title}",
        published=published,
        wiki_hit=wiki_hit,
    )


def _outcome(feed_id: str, items: list[RssItem]) -> FeedOutcome:
    return FeedOutcome(
        feed_id=feed_id,
        feed_name=feed_id,
        cluster=feed_id,
        url=f"https://example.test/{feed_id}/feed",
        items=items,
    )


class TestRssInboxStubs(unittest.TestCase):
    def test_inbox_slug_shape(self):
        slug = inbox_slug("NFL DFS: 50% Off — Late Swap!!!")
        self.assertRegex(slug, r"^[a-z0-9-]+$")
        self.assertLessEqual(len(slug), 60)

    def test_skip_list_and_filename_shape(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            outcomes = [
                _outcome(
                    "event-horizon",
                    [_item("event-horizon", "Kalshi volume record")],
                ),
                _outcome(
                    "legal-sports-report",
                    [_item("legal-sports-report", "New Jersey betting handle")],
                ),
            ]
            written = write_inbox_stubs(
                repo,
                outcomes,
                max_files=8,
                skip_ids=["event-horizon", "the-closing-line", "outlier-weekly"],
            )
            self.assertEqual(len(written), 1)
            name = written[0].name
            self.assertRegex(
                name,
                r"^rss-legal-sports-report-2026-09-16-[a-z0-9-]+\.md$",
            )
            self.assertTrue((repo / "research to be indexed" / name).is_file())
            body = written[0].read_text(encoding="utf-8")
            self.assertIn("discovery stub — fetch body at ingest", body)
            self.assertIn("https://example.test/legal-sports-report/", body)

    def test_cap(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            items = [_item("lsr", f"Story {i}") for i in range(10)]
            written = write_inbox_stubs(
                repo,
                [_outcome("lsr", items)],
                max_files=8,
                skip_ids=[],
            )
            self.assertEqual(len(written), 8)

    def test_existing_file_skip(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            inbox = repo / "research to be indexed"
            inbox.mkdir(parents=True)
            item = _item("lsr", "Already Here")
            name = f"rss-lsr-2026-09-16-{inbox_slug(item.title)}.md"
            existing = inbox / name
            existing.write_text("keep-me\n", encoding="utf-8")
            written = write_inbox_stubs(
                repo,
                [_outcome("lsr", [item, _item("lsr", "Brand New Item")])],
                max_files=8,
                skip_ids=[],
            )
            self.assertEqual(len(written), 1)
            self.assertIn("brand-new-item", written[0].name)
            self.assertEqual(existing.read_text(encoding="utf-8"), "keep-me\n")

    def test_wiki_hit_skip(self):
        with tempfile.TemporaryDirectory() as td:
            repo = Path(td)
            written = write_inbox_stubs(
                repo,
                [
                    _outcome(
                        "lsr",
                        [
                            _item("lsr", "Old wiki item", wiki_hit="sources/foo.md"),
                            _item("lsr", "Fresh item"),
                        ],
                    )
                ],
                max_files=8,
                skip_ids=[],
            )
            self.assertEqual(len(written), 1)
            self.assertIn("fresh-item", written[0].name)


if __name__ == "__main__":
    unittest.main()
