#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
# Nexus Protocol — Local Stack Launcher
#
# Starts the dashboard server in NEXUS_ENV=local mode.
# Loads .env if present (copy .env.example to get started).
# ═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail
cd "$(dirname "$0")/.."

if [ ! -f .env ] && [ -f .env.example ]; then
  echo "▸ No .env found — copying .env.example to .env (fill in secrets there, never commit it)"
  cp .env.example .env
fi

# Load .env without requiring extra tooling
set -a; [ -f .env ] && . ./.env; set +a

echo "▸ Starting Nexus dashboard (local) on port ${PORT:-3000}"
exec env NEXUS_ENV=local PORT="${PORT:-3000}" node server.js
