@echo off
REM bots-daily.cmd — Daily DAO bot run WITHOUT GitHub Actions (Windows)
REM
REM GitHub Actions is blocked while the account has a billing lock. This does
REM what the 'DAO Bots' workflow did, from your PC. Push is NOT affected by the
REM billing lock, so updated reports still reach GitHub.
REM
REM Schedule it ONCE (Windows Task Scheduler, daily 6:00 AM) — run this in an
REM elevated Command Prompt, adjusting the path to your clone:
REM   schtasks /Create /TN "Nexus DAO Bots" /TR "C:\Users\fuzzy\The-Nexus-Protocol-Token-DAO\scripts\bots-daily.cmd" /SC DAILY /ST 06:00
REM
REM Or run manually:  scripts\bots-daily.cmd

setlocal
cd /d "%~dp0.."

echo --- %DATE% %TIME% DAO bots (Actions-free mode) ---

git config user.name  "Todd Stephens"
git config user.email "157565446+FuzzysTodd@users.noreply.github.com"

node bots\health-bot.js
if errorlevel 1 goto :fail
node bots\dao-accounting-bot.js
if errorlevel 1 goto :fail
node bots\registry-sync-bot.js
if errorlevel 1 goto :fail

git add reports
git diff --cached --quiet
if errorlevel 1 (
  git commit -m "DAO bots (Actions-free): deterministic upkeep report (zero AI credits)"
  git push
  echo Reports committed and pushed.
) else (
  echo No report changes - nothing to commit.
)
exit /b 0

:fail
echo DAO bots found problems - see output above.
exit /b 1
