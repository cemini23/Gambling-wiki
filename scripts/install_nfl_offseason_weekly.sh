#!/usr/bin/env bash
# install_nfl_offseason_weekly.sh — Sunday NFL offseason weekly research LaunchAgent
set -euo pipefail

WIKI_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.cemini.nfl-offseason-weekly.gambling"
PLIST="$HOME/Library/LaunchAgents/${LABEL}.plist"
BIN_DIR="$HOME/bin"
WRAPPER="$BIN_DIR/cemini-nfl-offseason-weekly-gambling"
LOG_DIR="$HOME/Library/Logs/cemini"
PYTHON="${PYTHON:-python3}"

mkdir -p "$BIN_DIR" "$LOG_DIR" "$WIKI_ROOT/briefs/offseason"

cat > "$WRAPPER" <<EOF
#!/usr/bin/env bash
set -euo pipefail
cd "$WIKI_ROOT"
exec "$PYTHON" scripts/nfl_offseason_weekly_run.py "\$@"
EOF
chmod +x "$WRAPPER"

cat > "$PLIST" <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>${LABEL}</string>
  <key>ProgramArguments</key>
  <array>
    <string>${WRAPPER}</string>
  </array>
  <key>WorkingDirectory</key>
  <string>${WIKI_ROOT}</string>
  <key>StartCalendarInterval</key>
  <dict>
    <key>Weekday</key>
    <integer>0</integer>
    <key>Hour</key>
    <integer>9</integer>
    <key>Minute</key>
    <integer>15</integer>
  </dict>
  <key>StandardOutPath</key>
  <string>${LOG_DIR}/nfl-offseason-weekly-gambling.out.log</string>
  <key>StandardErrorPath</key>
  <string>${LOG_DIR}/nfl-offseason-weekly-gambling.err.log</string>
</dict>
</plist>
EOF

launchctl bootout "gui/$(id -u)/${LABEL}" 2>/dev/null || true
launchctl bootstrap "gui/$(id -u)" "$PLIST"
launchctl enable "gui/$(id -u)/${LABEL}"

echo "Installed ${LABEL} — Sundays 09:15 local"
echo "  Wrapper: ${WRAPPER}"
echo "  Output:  ${WIKI_ROOT}/briefs/offseason/"
echo "  Manual:  ${WRAPPER}"
echo ""
echo "In-season: use install_nfl_slate_prefetch.sh (Sep+) instead of this cadence."
