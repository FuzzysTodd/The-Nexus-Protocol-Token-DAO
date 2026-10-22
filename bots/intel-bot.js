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
// Explicit mode via NEXUS_THINK: "off" | "local" | "remote"
//   local  : your GPUs via Ollama — free of API credits (electricity only).
//            If the server is unreachable, reports UNAVAILABLE — NEVER falls
//            back to a paid provider.
//   remote : paid cloud API — ONLY when explicitly set. Requires
//            NEXUS_MODEL_API_KEY; a stray key alone never enables it.
//   off    : deterministic, $0.
// Default (NEXUS_THINK unset): local if a server answers, otherwise off.
// A paid request can only ever happen when NEXUS_THINK=remote AND a key is set.
async function resolveThinking() {
  const mode = (process.env.NEXUS_THINK || "auto").toLowerCase();
  const key = process.env.NEXUS_MODEL_API_KEY || "";
  const url = process.env.NEXUS_MODEL_URL || "";

  if (mode === "remote") {
    if (!key) {
      return { mode: "error", error: "NEXUS_THINK=remote but no NEXUS_MODEL_API_KEY set — paid calls stay disabled" };
    }
    return {
      mode: "remote-api",
      url: url || "https://api.openai.com/v1/chat/completions",
      model: process.env.NEXUS_MODEL_NAME || "gpt-4o-mini",
      key,
    };
  }

  if (mode === "off") return { mode: "off" };

  // "auto" or "local": local GPU only — a paid fallback is never used
  const localUrl = url || "http://localhost:11434/v1/chat/completions";
  let serverUp = false;
  try {
    const probe = await fetch(localUrl.replace("/v1/chat/completions", "/api/tags"), {
      signal: AbortSignal.timeout(2000),
    });
    serverUp = probe.ok;
  } catch { /* not reachable */ }

  if (mode === "local" && !serverUp) {
    return { mode: "unavailable", error: "NEXUS_THINK=local but no model server at " + localUrl.replace("/v1/chat/completions", "") + " — thinking skipped, NO paid fallback" };
  }
  if (serverUp) {
    return {
      mode: "local-gpu",
      url: localUrl,
      model: process.env.NEXUS_MODEL_NAME || "llama3.1:8b",
    };
  }
  // auto + no server + (maybe a stray key) → still off, never paid
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

// ── Thinking step (local-gpu free / remote-api paid / off) ────────────────
async function think(intel, engine) {
  if (engine.mode === "error" || engine.mode === "unavailable") {
    return { enabled: false, mode: engine.mode, error: engine.error };
  }
  if (engine.mode === "off") {
    return {
      enabled: false,
      mode: "off",
      note: "Thinking off — deterministic mode, $0. To think on your own GPUs set NEXUS_THINK=local and run Ollama (see README). Paid cloud models require NEXUS_THINK=remote AND a key.",
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
    ` (thinking: ${engine.mode}${engine.mode === "local-gpu" ? " — your GPUs, no API credits" : engine.mode === "remote-api" ? " — PAID API" : engine.mode === "unavailable" || engine.mode === "error" ? " — PROBLEM (see report)" : " — $0"})`);
  if (thinking && thinking.error) console.log(`    ⚠ ${thinking.error}`);
  if (errors.length) errors.forEach((e) => console.log(`    ⚠ ${e}`));
  // Network failures are recorded, never fatal — a daily run must not die
  // just because the internet was down.
}

main().catch((e) => {
  console.error(`  ✗ Intel Bot failed: ${e.message}`);
  process.exit(1);
});
