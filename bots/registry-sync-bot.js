#!/usr/bin/env node
/**
 * registry-sync-bot.js — Nexus Protocol DAO Registry Sync Bot
 * ------------------------------------------------------------
 * One of Todd's personal DAO bots. Deterministic, zero AI credits.
 *
 * Duty: Keep the dashboard's Agents & Bots panel fed with live data.
 * Reads the MCP agent registry and bot duty definitions, then writes a
 * single unified payload the dashboard fetches. No AI, no manual edits.
 *
 * Usage:  node bots/registry-sync-bot.js
 * Output: reports/agents.json
 */

"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const REPORTS_DIR = path.join(ROOT, "reports");

function readJson(p) {
  return JSON.parse(fs.readFileSync(path.join(ROOT, p), "utf8"));
}

function main() {
  const registry = readJson("mcp/nexus-agent-registry.json");
  const botsDef = readJson("mcp/agents/financial-ops-bots.json");

  // MCP agents — flatten duties for the dashboard
  const agents = (registry.agents || []).map((a) => ({
    id: a.id,
    domain: a.domain,
    duties: a.primaryExpertise || [],
    scope: a.scope || [],
    authority: a.authorityLevel,
    tools: a.tools || [],
    notes: a.notes || "",
  }));

  // Personal DAO bots — financial ops bots + this repo's deterministic bots
  const finBots = (botsDef.financialOpsBots && botsDef.financialOpsBots.bots) || [];
  const localBots = [
    {
      id: "dao-health-bot",
      name: "Health Bot",
      role: "Pre-flight the repository: validate configs, verify script targets, detect junk files, confirm git identity so commits never prompt. Replaces routine AI review.",
      runs: "npm run bots:health — also runs in CI on every push",
      creditsUsed: "0 (deterministic Node.js)",
    },
    {
      id: "dao-accounting-bot",
      name: "File-Accounting Bot",
      role: "Account for every tracked file — especially loose root files — in reports/file-accounting.json/.md. The DAO file set stays complete without any AI audit.",
      runs: "npm run bots:accounting — also runs in CI on every push",
      creditsUsed: "0 (deterministic Node.js)",
    },
    {
      id: "dao-registry-sync-bot",
      name: "Registry Sync Bot",
      role: "Feed the dashboard Agents & Bots panel from the MCP registries. Updates flow to the UI with zero manual editing.",
      runs: "npm run bots:sync — also runs in CI on every push",
      creditsUsed: "0 (deterministic Node.js)",
    },
    ...finBots.map((b) => ({
      id: b.id,
      name: b.name,
      role: b.role,
      outputs: b.outputs || [],
      runs: "GitHub Actions — financial-ops-automation workflow (human-gated)",
      creditsUsed: "0 (scripted checks; approvals stay human-gated)",
    })),
  ];

  const payload = {
    generatedBy: "registry-sync-bot",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    agentCount: agents.length,
    botCount: localBots.length,
    agents,
    bots: localBots,
  };

  fs.mkdirSync(REPORTS_DIR, { recursive: true });
  fs.writeFileSync(path.join(REPORTS_DIR, "agents.json"),
    JSON.stringify(payload, null, 2) + "\n");

  console.log(`✓ agents.json written: ${agents.length} MCP agents, ${localBots.length} DAO bots`);
  console.log("  reports/agents.json — dashboard fetches this for the Agents & Bots tab");
}

main();
