"""Cold-start HUD — no fake rock reads on tiny samples."""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from private import opponent_hud_exploit as hud  # noqa: E402


def test_low_sample_ignores_playing_style_rock():
    stats = {
        "sampleSize": 3,
        "vpip": 0.08,
        "playingStyle": {"archetype": "rock"},
    }
    assert hud.classify_archetype(stats) == "unknown"


def test_cold_start_until_hero_and_villain_samples():
    table = {
        "selfSeatNumber": 1,
        "seats": [{"seatNumber": 1, "stackChips": 950}],
    }
    profiles = [{"sampleSize": 5, "confidence": 0.0, "agentId": "v1"}]
    mode, margins, cold, reason = hud._apply_cold_start_guard(
        table=table,
        competition_id="cmp_test",
        conf=0.0,
        profiles=profiles,
        mode="rock",
        margins=hud.exploit_margins("rock"),
    )
    assert cold is True
    assert reason in ("hero_sample", "villain_sample", "low_conf")
    assert mode == "unknown"
    assert margins["open_steal_equity"] >= 0.99
