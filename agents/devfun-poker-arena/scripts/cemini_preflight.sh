#!/usr/bin/env bash
# Pre-deploy gate for cemini Playground / tournament seasons.
#
# Run before rsync to prod or after any decide() / HUD change:
#   ./scripts/cemini_preflight.sh
#   ./scripts/cemini_preflight.sh --full   # slower self-play audit with --gate
set -euo pipefail
cd "$(dirname "$0")/.."

FULL=0
for arg in "$@"; do
  case "$arg" in
    --full) FULL=1 ;;
  esac
done

echo "==> [1/3] pytest (unit + cemini regression + scenarios)"
uv run python -m pytest tests/ -q --tb=short

echo ""
echo "==> [2/4] anti-profiling deep audit (mix+s sanitize ON)"
uv run python examples/cemini_anti_profiling_audit.py --gate --hands 400 --seed 42

echo ""
echo "==> [3/4] cemini self-play KPI audit (report, mix OFF baseline)"
if [[ "$FULL" -eq 1 ]]; then
  uv run python examples/cemini_selfplay_audit.py --hands 600 --seed 42 --gate
else
  uv run python examples/cemini_selfplay_audit.py --hands 250 --seed 42 --gate
fi

echo ""
echo "==> [4/4] dry-run lobby path (no network)"
uv run examples/agent.py --agent examples/cemini_decide.py --dry-run --max-hands 15

echo ""
echo "PREFLIGHT OK — safe to deploy (rsync + systemctl restart)."
