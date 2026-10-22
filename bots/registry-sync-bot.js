#!/usr/bin/env node
/**
 * registry-sync-bot.js — Nexus Protocol DAO Registry Sync Bot
 * ------------------------------------------------------------
 * One of Todd's personal DAO bots. Deterministic, zero AI credits.
 *
 * Duty: Feed the dashboard's Agents & Bots panel from the MCP registries.
 * Reads the agent registry and bot duty definitions, then writes a single
 * payload the dashboard fetches. No AI, no manual edits.
 *
 * IMPORTANT: this payload is a *generated snapshot* of registry definitions
 * and duty descriptions — it is not live execution telemetry. The registry
 * agents are defined specialists; the three maintenance bots in this repo
 * are implemented and run deterministically.
 *
 * Usage:  node bots/registry-sync-bot.js
 * Output: reports/agents.json (written only when content changes)
 */

"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const REPORTS_DIR = path.join(ROOT, "reports");

function readJson(p) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, p), "utf8"));
}

// Change-aware write: skip the file when only the timestamp would differ.
function writeIfChanged(filePath, content) {
  let existing = null;
  try { existing = fs.readFileSync(filePath, "utf8"); } catch { /* absent */ }
  const strip = (s) => s.replace(/"generatedAt": "[^"]+"/, '"generatedAt": "<ts>"');
  if (existing !== null && strip(existing) === strip(content)) return false;
  fs.writeFileSync(filePath, content);
  return true;
}

function main() {
  const registry = readJson("mcp/nexus-agent-registry.json");
  const botsDef = readJson("mcp/agents/financial-ops-bots.json");

  // MCP agents — registry definitions (not implementations)
  const agents = (registry.agents || []).map((a) => ({
    id: a.id,
    domain: a.domain,
    status: "defined",   // defined in the registry; implementation is separate
    duties: a.primaryExpertise || [],
    scope: a.scope || [],
    authority: a.authorityLevel,
    tools: a.tools || [],
    notes: a.notes || "",
  }));

  // Personal DAO bots — implemented & exercised in this repo
  const finBots = (botsDef.financialOpsBots && botsDef.financialOpsBots.bots) || [];
  const localBots = [
    {
      id: "dao-health-bot",
      name: "Health Bot",
      status: "implemented",
      role: "Pre-flight the repository: validate configs, verify script targets, detect junk files, confirm git identity is set so commits never prompt.",
      runs: "npm run bots:health — also wired into .github/workflows/dao-bots.yml on push",
      creditsUsed: "0 (deterministic Node.js — makes no model API calls)",
    },
    {
      id: "dao-accounting-bot",
      name: "File-Accounting Bot",
      status: "implemented",
      role: "Account for every tracked file in the repository (full tree, not just root) with category, purpose, and disposition. Unrecognized files are flagged for review, never silently approved.",
      runs: "npm run bots:accounting — also wired into .github/workflows/dao-bots.yml on push",
      creditsUsed: "0 (deterministic Node.js — makes no model API calls)",
    },
    {
      id: "dao-registry-sync-bot",
      name: "Registry Sync Bot",
      status: "implemented",
      role: "Feed the dashboard Agents & Bots panel from the MCP registries. Updates flow to the UI with zero manual editing.",
      runs: "npm run bots:sync — also wired into .github/workflows/dao-bots.yml on push",
      creditsUsed: "0 (deterministic Node.js — makes no model API calls)",
    },
    ...finBots.map((b) => ({
      id: b.id,
      name: b.name,
      status: "defined",  // duty definitions; execution stays human-gated
      role: b.role,
      outputs: b.outputs || [],
      runs: "Duty defined in mcp/agents/financial-ops-bots.json — definition only; execution is human-gated, no autonomous runs",
      creditsUsed: "Not verified — definition only; whether execution uses a model depends on how it is run",
    })),
  ];

  const payload = {
    generatedBy: "registry-sync-bot",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    note: "Generated snapshot of registry definitions and duties — not live execution telemetry.",
    agentCount: agents.length,
    botCount: localBots.length,
    agents,
    bots: localBots,
  };

  fs.mkdirSync(REPORTS_DIR, { recursive: true });
  const changed = writeIfChanged(
    path.join(REPORTS_DIR, "agents.json"),
    JSON.stringify(payload, null, 2) + "\n"
  );

  console.log(`✓ agents.json ${changed ? "updated" : "unchanged"}: ${agents.length} MCP agents (defined), ${localBots.length} DAO bots`);
  console.log("  reports/agents.json — dashboard fetches this for the Agents & Bots tab");
}

main();
