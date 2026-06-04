"""Deep regression for anti-profiling — run in pytest before deploy."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def test_anti_profiling_audit_gate():
    """Full deep audit (regression ×2, sanitize, self-play A/B, prod KPI)."""
    env = os.environ.copy()
    env.pop("CEMINI_MIX_POSTFLOP", None)
    env.pop("CEMINI_SANITIZE_OUTPUT", None)
    proc = subprocess.run(
        [sys.executable, str(ROOT / "examples" / "cemini_anti_profiling_audit.py"),
         "--gate", "--hands", "400", "--seed", "42"],
        cwd=str(ROOT),
        env=env,
        capture_output=True,
        text=True,
        timeout=180,
    )
    assert proc.returncode == 0, proc.stdout + proc.stderr


def test_regression_spots_identical_mix_on_off():
    """Hard leak guards must not flip when mixing is enabled (repeat for MC variance)."""
    sys.path.insert(0, str(ROOT / "examples"))
    from cemini_decide import decide  # noqa: WPS433
    from tests.fixtures.regression_spots import regression_spots  # noqa: WPS433

    for spot in regression_spots():
        os.environ["CEMINI_MIX_POSTFLOP"] = "0"
        off = decide(spot.table, deadline_s=10.0)
        for _ in range(8):
            os.environ["CEMINI_MIX_POSTFLOP"] = "1"
            on = decide(spot.table, deadline_s=10.0)
            if spot.forbidden:
                assert on["action"] not in spot.forbidden, spot.id
            if spot.required:
                assert on["action"] in spot.required, spot.id
        if off["action"] in ("fold", "check") and spot.forbidden & {"call", "raise", "all-in"}:
            assert on["action"] == off["action"], f"{spot.id}: {off['action']!r} -> {on['action']!r}"
    os.environ.pop("CEMINI_MIX_POSTFLOP", None)
