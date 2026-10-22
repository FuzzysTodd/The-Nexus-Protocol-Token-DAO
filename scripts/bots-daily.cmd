@echo off
REM bots-daily.cmd — Daily DAO bot run WITHOUT GitHub Actions (Windows)
REM
REM GitHub Actions is blocked while the account has a billing lock. This does
REM what the 'DAO Bots' workflow did, from your PC. Push is NOT affected by
REM the billing lock, so updated reports still reach GitHub.
REM
REM Schedule it ONCE (Windows Task Scheduler, daily 6:00 AM) — run this from
REM an ELEVATED command prompt inside the repo folder (path is picked up
REM automatically from the current directory):
REM
REM   schtasks /Create /TN "Nexus DAO Bots" /TR "%CD%\scripts\bots-daily.cmd" /SC DAILY /ST 06:00
REM
REM Or run manually:  scripts\bots-daily.cmd
REM
REM Exit codes: 0 = clean run, 1 = failure. The script refuses to run when
REM you have staged changes, so it can never commit your work-in-progress.

setlocal
cd /d "%~dp0.."

echo --- %DATE% %TIME% DAO bots (Actions-free mode) ---

REM Preflight: refuse when the index has staged changes
git diff --cached --quiet
if not errorlevel 1 goto :bots
echo REFUSING TO RUN: you have STAGED changes. Commit or stash them first.
exit /b 1

:bots
git config user.name  "Todd Stephens"
git config user.email "157565446+FuzzysTodd@users.noreply.github.com"

node bots\fleet-runner.js
if errorlevel 1 goto :fail

REM Commit ONLY reports (explicit pathspec), then push
git add reports
git diff --cached --quiet -- reports
if not errorlevel 1 (
  echo No report changes - nothing to commit.
  exit /b 0
)

git commit -m "DAO bots (Actions-free): deterministic upkeep report (zero AI credits)" -- reports
if errorlevel 1 goto :fail
git push
if errorlevel 1 (
  echo PUSH FAILED - reports are committed locally; push manually when ready.
  exit /b 1
)
echo Reports committed and pushed.
exit /b 0

:fail
echo DAO bots found problems - see output above.
exit /b 1
