#!/usr/bin/env node
/**
 * health-bot.js — Nexus Protocol DAO Health Bot
 * ----------------------------------------------
 * One of Todd's personal DAO bots. Deterministic, zero AI credits.
 *
 * Duty: Pre-flight the repository so no AI (and no human) has to.
 *   1. Validate every JSON config parses.
 *   2. Verify every script referenced in package.json exists.
 *   3. Scan for accidental junk files (empty files, DLLs, VS metadata).
 *   4. Check git identity is configured (so commits never prompt).
 *   5. Emit reports/health-report.json for the dashboard.
 *
 * Usage:  node bots/health-bot.js [--ci]
 */

"use strict";

const fs = require("fs");
const path = require("path");
const { execSync } = require("child_process");

const ROOT = path.resolve(__dirname, "..");
const REPORTS_DIR = path.join(ROOT, "reports");
const ci = process.argv.includes("--ci");

// Change-aware write: skip the file when only the timestamp would differ —
// keeps local hook runs from churning reports on every commit.
function writeIfChanged(filePath, content) {
  let existing = null;
  try { existing = fs.readFileSync(filePath, "utf8"); } catch { /* absent */ }
  const strip = (s) => s.replace(/"generatedAt": "[^"]+"/, '"generatedAt": "<ts>"');
  if (existing !== null && strip(existing) === strip(content)) return false;
  fs.writeFileSync(filePath, content);
  return true;
}

const errors = [];
const warnings = [];

function check(label, ok, detail = "", isWarning = false) {
  if (ok) {
    console.log(`  ✓ ${label}`);
  } else if (isWarning) {
    console.log(`  ⚠ ${label}${detail ? ` — ${detail}` : ""}`);
    warnings.push(`${label}${detail ? ` — ${detail}` : ""}`);
  } else {
    console.log(`  ✗ ${label}${detail ? ` — ${detail}` : ""}`);
    errors.push(`${label}${detail ? ` — ${detail}` : ""}`);
  }
}

// ── 1. JSON configs parse ─────────────────────────────────────────────────────
console.log("▸ Validating JSON configuration files");
const jsonFiles = [
  "package.json",
  "dao-data-source-manifest.json",
  "mcp/nexus-agent-registry.json",
  "mcp/agents/financial-ops-bots.json",
  "network-registry.json",
  "remix.config.json",
  "vercel.json",
  ".solhint.json",
];
for (const f of jsonFiles) {
  const p = path.join(ROOT, f);
  if (!fs.existsSync(p)) { check(`exists: ${f}`, false, "missing"); continue; }
  try {
    JSON.parse(fs.readFileSync(p, "utf8"));
    check(`parses: ${f}`, true);
  } catch (e) {
    check(`parses: ${f}`, false, e.message);
  }
}

// ── 2. package.json script targets exist ──────────────────────────────────────
console.log("▸ Verifying npm script targets");
const pkg = JSON.parse(fs.readFileSync(path.join(ROOT, "package.json"), "utf8"));
for (const [name, cmd] of Object.entries(pkg.scripts || {})) {
  if (!cmd) continue;
  const nodeMatch = cmd.match(/node\s+(bots\/[\w-]+\.js|server\.js)/);
  const shMatch = cmd.match(/bash\s+(scripts\/[\w.-]+\.sh)/);
  const targets = [];
  if (nodeMatch) targets.push(nodeMatch[1]);
  if (shMatch) targets.push(shMatch[1]);
  for (const t of targets) {
    check(`${name} -> ${t}`, fs.existsSync(path.join(ROOT, t)), "file missing");
  }
}

// ── 3. Junk / empty files among tracked loose files ─────────────────────────────
console.log("▸ Scanning for junk files");
const tracked = execSync("git ls-files", { cwd: ROOT, encoding: "utf8" }).split("\n").filter(Boolean);
const junkPatterns = [/\.dll$/i, /\.exe$/i, /^\.vs\//, /^index\.html1$/, /^as-is\.$/];
for (const f of tracked) {
  if (junkPatterns.some((re) => re.test(f))) check(`no junk: ${f}`, false, "junk file tracked");
}
const emptyLoose = tracked.filter((f) => {
  if (f.includes("/")) return false;
  try { return fs.statSync(path.join(ROOT, f)).size === 1; } catch { return false; }
});
check("no empty 1-byte loose files", emptyLoose.length === 0,
  emptyLoose.length ? `found: ${emptyLoose.join(", ")}` : "");

// ── 4. Git identity configured (no prompt on commit) ────────────────────────────
console.log("▸ Verifying git identity (frictionless commits)");
try {
  const name = execSync("git config user.name", { cwd: ROOT, encoding: "utf8" }).trim();
  const email = execSync("git config user.email", { cwd: ROOT, encoding: "utf8" }).trim();
  check(`git user.name = ${name}`, Boolean(name));
  check(`git user.email = ${email}`, Boolean(email) && !email.includes("users.noreply.github.com@"));
} catch (e) {
  check("git identity", false, e.message);
}

// ── 5. Agent registry shape ─────────────────────────────────────────────────────
console.log("▸ Validating MCP agent registry");
try {
  const reg = JSON.parse(fs.readFileSync(path.join(ROOT, "mcp/nexus-agent-registry.json"), "utf8"));
  const agents = reg.agents || [];
  check(`agent registry: ${agents.length} agents defined`, agents.length > 0);
  const missingDuty = agents.filter((a) => !a.domain || !a.primaryExpertise || !a.authorityLevel);
  check("every agent has domain + expertise + authority", missingDuty.length === 0,
    missingDuty.map((a) => a.id).join(", "));
} catch (e) {
  check("agent registry readable", false, e.message);
}

// ── Report ─────────────────────────────────────────────────────────────────────
fs.mkdirSync(REPORTS_DIR, { recursive: true });
const report = {
  generatedBy: "health-bot",
  generatedAt: new Date().toISOString(),
  owner: "@FuzzysTodd",
  status: errors.length ? "FAIL" : (warnings.length ? "WARN" : "PASS"),
  errors, warnings,
};
const healthChanged = writeIfChanged(path.join(REPORTS_DIR, "health-report.json"),
  JSON.stringify(report, null, 2) + "\n");

console.log(`\n${report.status === "PASS" ? "✓" : "✗"} Health: ${report.status}` +
  ` (${errors.length} errors, ${warnings.length} warnings)`);
if (report.status !== "PASS" && !ci) process.exit(1);
if (ci && errors.length) process.exit(1);
