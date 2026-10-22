#!/usr/bin/env bash
# bots-daily.sh — Daily DAO bot run WITHOUT GitHub Actions
#
# GitHub Actions is blocked while the account has a billing lock. This script
# does what the 'DAO Bots' workflow did, from any machine with this repo:
#   1. Runs all three deterministic bots (zero AI credits)
#   2. Commits updated reports under Todd's pre-configured identity
#   3. Pushes if anything changed (push is NOT affected by the billing lock)
#
# Schedule it (choose one):
#   Linux/macOS cron:      crontab -e
#     0 6 * * *  cd /path/to/repo && bash scripts/bots-daily.sh >> .bots-daily.log 2>&1
#   Or run manually:       bash scripts/bots-daily.sh

set -euo pipefail
cd "$(dirname "$0")/.."

echo "── $(date -u +%Y-%m-%dT%H:%MZ) DAO bots (Actions-free mode) ──"

# Identity is already pre-configured by scripts/setup-identity.sh (idempotent)
git config user.name  "Todd Stephens" 2>/dev/null || true
git config user.email "157565446+FuzzysTodd@users.noreply.github.com" 2>/dev/null || true

node bots/health-bot.js
node bots/dao-accounting-bot.js
node bots/registry-sync-bot.js

git add reports/ || true
if git diff --cached --quiet; then
  echo "✓ No report changes — nothing to commit."
else
  git commit -m "🤖 DAO bots (Actions-free): deterministic upkeep report (zero AI credits)"
  git push
  echo "✓ Reports committed and pushed."
fi
