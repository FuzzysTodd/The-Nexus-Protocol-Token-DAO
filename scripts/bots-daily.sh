#!/usr/bin/env bash
# bots-daily.sh — Daily DAO bot run WITHOUT GitHub Actions
#
# GitHub Actions is blocked while the account has a billing lock. This script
# does what the 'DAO Bots' workflow did, from any machine with this repo:
#   1. Preflight: refuses to run if you have staged changes (so it can
#      never commit your work-in-progress by accident).
#   2. Runs all three deterministic bots (zero AI credits) — they write
#      reports/ files.
#   3. Commits ONLY reports/ (explicit pathspec) under your pre-configured
#      identity, then pushes. Push is NOT affected by the billing lock.
#
# Schedule it (choose one):
#   Linux/macOS cron:      crontab -e
#     0 6 * * *  cd /path/to/repo && bash scripts/bots-daily.sh >> .bots-daily.log 2>&1
#   Or run manually:       bash scripts/bots-daily.sh
#
# Exit codes: 0 = clean run (nothing to do or pushed OK), 1 = failure.

set -euo pipefail
cd "$(dirname "$0")/.."

echo "── $(date -u +%Y-%m-%dT%H:%MZ) DAO bots (Actions-free mode) ──"

# ── Preflight: never touch a checkout with staged work ────────────────────────
if ! git diff --cached --quiet; then
  echo "✗ Refusing to run: you have STAGED changes. Commit or stash them first"
  echo "  (this guard prevents the bots from committing your work-in-progress)."
  exit 1
fi

# ── Identity (pre-configured by scripts/setup-identity.sh; idempotent) ────────
git config user.name  "Todd Stephens"
git config user.email "157565446+FuzzysTodd@users.noreply.github.com"

# ── Run bots (they write reports/) ────────────────────────────────────────────
node bots/health-bot.js
node bots/dao-accounting-bot.js
node bots/registry-sync-bot.js

# ── Commit ONLY the reports, then push ────────────────────────────────────────
# Explicit pathspec commit: nothing outside reports/ is ever included,
# even if something else somehow got staged.
if git diff --quiet -- reports/ && git diff --cached --quiet -- reports/; then
  echo "✓ No report changes — nothing to commit."
  exit 0
fi

git add reports/
git commit -m "🤖 DAO bots (Actions-free): deterministic upkeep report (zero AI credits)" -- reports/

if git push; then
  echo "✓ Reports committed and pushed."
else
  echo "✗ Push failed — reports are committed locally; push manually when ready."
  exit 1
fi
