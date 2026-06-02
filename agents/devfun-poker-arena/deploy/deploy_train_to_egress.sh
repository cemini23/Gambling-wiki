#!/usr/bin/env bash
# Deploy offline poker training batch to cemini-egress-fi (no Arena API / no lobby).
#
# Usage:
#   ./agents/devfun-poker-arena/deploy/deploy_train_to_egress.sh
#   ./agents/devfun-poker-arena/deploy/deploy_train_to_egress.sh --run-now
#
# Manual run on server:
#   ssh cemini-egress-fi systemctl start cemini-poker-train.service
#   ssh cemini-egress-fi tail -50 /opt/devfun-poker-arena-train/reports/train/latest.txt
set -euo pipefail

HOST="${CEMINI_EGRESS_HOST:-cemini-egress-fi}"
REMOTE_DIR="/opt/devfun-poker-arena-train"
RUN_NOW=false
for arg in "$@"; do
  case "$arg" in
    --run-now) RUN_NOW=true ;;
  esac
done

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AGENT_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ ! -f "${AGENT_DIR}/private/opponent_hud_exploit.py" ]]; then
  echo "ERROR: missing ${AGENT_DIR}/private/opponent_hud_exploit.py" >&2
  echo "Training HUD exploits require the private module on your machine." >&2
  exit 1
fi

echo "==> Deploy training tree to ${HOST}:${REMOTE_DIR}"

rsync -avz --delete \
  --exclude '.venv/' \
  --exclude 'venv/' \
  --exclude 'venv-pokerskill/' \
  --exclude '.git/' \
  --exclude '__pycache__/' \
  --exclude 'reports/' \
  --exclude '.pytest_cache/' \
  --exclude '.arena-credentials' \
  --exclude '.arena-credentials.*' \
  --exclude '.arena-poker-state' \
  --exclude '.env' \
  "${AGENT_DIR}/" "${HOST}:${REMOTE_DIR}/"

echo "==> Remote venv + systemd timer"
ssh "${HOST}" bash -s <<REMOTE
set -euo pipefail
REMOTE_DIR="/opt/devfun-poker-arena-train"
PY=/usr/bin/python3

chmod +x "\${REMOTE_DIR}/examples/run_train_batch.sh"
chmod +x "\${REMOTE_DIR}/examples/run_train_sweep.sh"
chmod +x "\${REMOTE_DIR}/examples/run_train_sweep_mixed.sh"
chmod +x "\${REMOTE_DIR}/examples/wait_then_run_mixed_sweep.sh"
chmod +x "\${REMOTE_DIR}/examples/wait_then_run_latest_sweep.sh"
chmod +x "\${REMOTE_DIR}/examples/run_train_cemini.sh"

if [[ ! -x "\${REMOTE_DIR}/venv/bin/python" ]]; then
  echo "Creating venv with \${PY}..."
  "\${PY}" -m venv "\${REMOTE_DIR}/venv"
fi

"\${REMOTE_DIR}/venv/bin/pip" install -q --upgrade pip
"\${REMOTE_DIR}/venv/bin/pip" install -q httpx python-dotenv treys pokerkit

mkdir -p "\${REMOTE_DIR}/reports/train" "\${REMOTE_DIR}/reports/sweep" "\${REMOTE_DIR}/reports/sweep-mixed"

install -m 644 "\${REMOTE_DIR}/deploy/cemini-poker-train.service" \
  /etc/systemd/system/cemini-poker-train.service
install -m 644 "\${REMOTE_DIR}/deploy/cemini-poker-train-mixed.service" \
  /etc/systemd/system/cemini-poker-train-mixed.service
install -m 644 "\${REMOTE_DIR}/deploy/cemini-poker-train-followup.service" \
  /etc/systemd/system/cemini-poker-train-followup.service
install -m 644 "\${REMOTE_DIR}/deploy/cemini-poker-train-latest-followup.service" \
  /etc/systemd/system/cemini-poker-train-latest-followup.service
install -m 644 "\${REMOTE_DIR}/deploy/cemini-poker-train.timer" \
  /etc/systemd/system/cemini-poker-train.timer

systemctl daemon-reload
systemctl enable cemini-poker-train.timer
systemctl start cemini-poker-train.timer
systemctl --no-pager status cemini-poker-train.timer || true

# Optional: queue or start sweep only when operator passes --run-now locally.
if [[ "${RUN_NOW}" == "true" ]]; then
  if pgrep -f 'run_train_sweep' >/dev/null 2>&1; then
    echo "Sweep process in flight — queueing latest followup"
    systemctl start --no-block cemini-poker-train-latest-followup.service
  else
    for u in cemini-poker-train.service cemini-poker-train-mixed.service; do
      st="\$(systemctl show "\$u" -p ActiveState --value 2>/dev/null || echo inactive)"
      if [[ "\$st" == "activating" || "\$st" == "active" ]]; then
        echo "Sweep unit \$u active — queueing latest followup"
        systemctl start --no-block cemini-poker-train-latest-followup.service
        exit 0
      fi
    done
    echo "Starting latest sweep pipeline (--run-now)"
    systemctl start --no-block cemini-poker-train.service
  fi
else
  echo "Deploy only — no sweep started (pass --run-now to start on egress)."
fi
REMOTE

if [[ "$RUN_NOW" == true ]]; then
  echo "==> Starting parameter sweep now (may take 1–3 hours on egress)..."
  ssh "${HOST}" "systemctl start --no-block cemini-poker-train.service"
  echo "Tail: ssh ${HOST} journalctl -u cemini-poker-train.service -f"
else
  echo ""
  echo "Timer enabled (03:00 UTC daily). To run immediately:"
  echo "  ssh ${HOST} systemctl start --no-block cemini-poker-train.service"
fi

echo ""
echo "6-max leaderboard:  ssh ${HOST} cat ${REMOTE_DIR}/reports/sweep/latest/leaderboard.txt"
echo "Mixed leaderboard:  ssh ${HOST} cat ${REMOTE_DIR}/reports/sweep-mixed/latest/leaderboard.txt"
echo "Mixed-only manual:  ssh ${HOST} systemctl start --no-block cemini-poker-train-mixed.service
Queue after current: ssh ${HOST} systemctl start --no-block cemini-poker-train-latest-followup.service"
