#!/usr/bin/env node
/**
 * intel-bot.js — Nexus DAO Internet Intelligence Bot
 * ---------------------------------------------------
 * Todd's internet-connected fleet member. Fetches PUBLIC, no-key APIs so it
 * costs $0 — no API keys, no paid services, no model calls by default.
 *
 * Fetches:
 *   • ETH-USD spot price      (Coinbase public API)
 *   • BTC-USD spot price      (Coinbase public API)
 *   • Repo stats (stars/forks/issues) (GitHub public API)
 *
 * Optional THINKING step (opt-in, costs money):
 *   If NEXUS_MODEL_API_KEY is set in your environment (.env), the bot sends
 *   the gathered intel to a model API for analysis. That call costs whatever
 *   your provider charges — it is OFF by default and never automatic.
 *   Without a key, the bot is a deterministic data collector: $0.
 *
 * Usage:  node bots/intel-bot.js        (also part of: npm run agents:run)
 * Output: reports/intel.json
 */

"use strict";

const fs = require("fs");
const path = require("path");

const ROOT = path.resolve(__dirname, "..");
const OUT = path.join(ROOT, "reports", "intel.json");

// ── .env loader (so 'set it in .env' actually works — no dependencies) ───────
function loadEnv() {
  const envPath = path.join(ROOT, ".env");
  if (!fs.existsSync(envPath)) return;
  for (const line of fs.readFileSync(envPath, "utf8").split("\n")) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2];
  }
}
loadEnv();

const TIMEOUT_MS = 10000;

// ── Thinking mode resolution ──────────────────────────────────────────────────
// Priority: explicit remote key → local GPU (Ollama) → off.
//   local-gpu   : free of API credits — your own hardware + electricity only
//   remote-api  : paid — billed by your provider per call
//   off         : deterministic, $0
async function resolveThinking() {
  const key = process.env.NEXUS_MODEL_API_KEY;
  const url = process.env.NEXUS_MODEL_URL || "";
  if (key) {
    return {
      mode: "remote-api",
      url: url || "https://api.openai.com/v1/chat/completions",
      model: process.env.NEXUS_MODEL_NAME || "gpt-4o-mini",
      key,
    };
  }
  // Local GPU inference (Ollama's OpenAI-compatible endpoint). No key, no
  // API charges — your RTX cards + electricity only. Works over the LAN too
  // (point NEXUS_MODEL_URL at http://<gpu-machine-ip>:11434/v1/chat/completions).
  const localUrl = url || "http://localhost:11434/v1/chat/completions";
  try {
    const probe = await fetch(localUrl.replace("/v1/chat/completions", "/api/tags"), {
      signal: AbortSignal.timeout(2000),
    });
    if (probe.ok) {
      return {
        mode: "local-gpu",
        url: localUrl,
        model: process.env.NEXUS_MODEL_NAME || "llama3.1:8b",
      };
    }
  } catch { /* no local server — fall through to off */ }
  return { mode: "off" };
}

async function fetchJson(url) {
  const resp = await fetch(url, {
    signal: AbortSignal.timeout(TIMEOUT_MS),
    headers: { "User-Agent": "nexus-dao-intel-bot" },
  });
  if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
  return resp.json();
}

// ── Thinking step (mode-resolved: local-gpu free / remote-api paid) ─────────
async function think(intel, engine) {
  if (engine.mode === "off") {
    return {
      enabled: false,
      mode: "off",
      note: "Thinking off — deterministic mode, $0. To think for free on your own GPUs, run Ollama on your machine (see README); for paid cloud models set NEXUS_MODEL_API_KEY in .env.",
    };
  }
  try {
    const headers = { "Content-Type": "application/json" };
    if (engine.key) headers["Authorization"] = `Bearer ${engine.key}`;
    const resp = await fetch(engine.url, {
      method: "POST",
      signal: AbortSignal.timeout(60000),
      headers,
      body: JSON.stringify({
        model: engine.model,
        messages: [
          { role: "system", content: "You are the Nexus DAO analyst. Be brief and factual." },
          { role: "user", content: "Analyze this DAO intel snapshot in 3 bullets:\n" + JSON.stringify(intel.data, null, 2) },
        ],
      }),
    });
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const body = await resp.json();
    return {
      enabled: true,
      mode: engine.mode,
      cost: engine.mode === "local-gpu" ? "your electricity/hardware only — no API credits" : "billed by your provider per call",
      analysis: (body.choices && body.choices[0] && body.choices[0].message && body.choices[0].message.content) || "(empty response)",
    };
  } catch (e) {
    return { enabled: true, mode: engine.mode, error: `model call failed: ${e.message}` };
  }
}

// ── Run ───────────────────────────────────────────────────────────────────────
async function main() {
  const fetched = { ETH: null, BTC: null, repo: null };
  const errors = [];

  // Prices (parallel)
  const priceJobs = [
    fetchJson("https://api.coinbase.com/v2/prices/ETH-USD/spot").then((d) => { fetched.ETH = d.data && d.data.amount; }).catch((e) => errors.push(`ETH price: ${e.message}`)),
    fetchJson("https://api.coinbase.com/v2/prices/BTC-USD/spot").then((d) => { fetched.BTC = d.data && d.data.amount; }).catch((e) => errors.push(`BTC price: ${e.message}`)),
    fetchJson("https://api.github.com/repos/FuzzysTodd/The-Nexus-Protocol-Token-DAO").then((d) => {
      fetched.repo = { stars: d.stargazers_count, forks: d.forks_count, openIssues: d.open_issues_count, pushedAt: d.pushed_at };
    }).catch((e) => errors.push(`repo stats: ${e.message}`)),
  ];
  await Promise.all(priceJobs);

  const data = {
    fetchedAt: new Date().toISOString(),
    ethUsd: fetched.ETH,
    btcUsd: fetched.BTC,
    repo: fetched.repo,
  };

  const engine = await resolveThinking();
  const thinking = await think({ data }, engine);

  const report = {
    generatedBy: "intel-bot",
    generatedAt: new Date().toISOString(),
    owner: "@FuzzysTodd",
    networkStatus: errors.length ? "degraded (some fetches failed — recorded below)" : "online",
    data,
    fetchErrors: errors,
    thinking,
  };

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, JSON.stringify(report, null, 2) + "\n");

  console.log(`  ${errors.length ? "⚠" : "✓"} Intel Bot: online=${!errors.length}` +
    ` ETH=$${data.ethUsd || "?"} BTC=$${data.btcUsd || "?"}` +
    ` stars=${data.repo ? data.repo.stars : "?"}` +
    ` (thinking: ${engine.mode}${engine.mode === "local-gpu" ? " — your GPUs, no API credits" : engine.mode === "remote-api" ? " — paid API" : " — $0"})`);
  if (errors.length) errors.forEach((e) => console.log(`    ⚠ ${e}`));
  // Network failures are recorded, never fatal — a daily run must not die
  // just because the internet was down.
}

main().catch((e) => {
  console.error(`  ✗ Intel Bot failed: ${e.message}`);
  process.exit(1);
});
