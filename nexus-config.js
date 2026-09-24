/**
 * nexus-config.js — Nexus Protocol Runtime Configuration
 *
 * Reads from environment variables so secrets are never hard-coded.
 * Set NEXUS_ENV=local (default) or NEXUS_ENV=remote.
 */

"use strict";

const env = process.env.NEXUS_ENV || "local";

module.exports = {
  env,

  // ── Ports ──────────────────────────────────────────────────────────────────
  ports: {
    dashboard:   Number(process.env.PORT                    || 3000),
    approval:    Number(process.env.APPROVAL_SERVICE_PORT   || 8787),
    financialOps:Number(process.env.FINANCIAL_OPS_REST_PORT || 8788),
    withdraws:   Number(process.env.WITHDRAWS_PORT          || 8789),
    signalBus:   Number(process.env.NEXUS_SIGNAL_BUS_PORT   || 8790),
  },

  // ── RPC / blockchain ───────────────────────────────────────────────────────
  rpc: {
    primary:  process.env.RPC_URL_PRIMARY || process.env.NEXUS_RPC_URL    || null,
    fallback: process.env.RPC_URL_FALLBACK|| process.env.NEXUS_WS_RPC_URL || null,
  },

  // ── Contract addresses ─────────────────────────────────────────────────────
  contracts: {
    builderFund: process.env.NEXUS_BUILDER_FUND_ADDRESS || null,
    governor:    process.env.NEXUS_GOVERNOR_ADDRESS      || null,
    treasury:    process.env.NEXUS_TREASURY_ADDRESS      || null,
    token:       process.env.NEXUS_TOKEN_ADDRESS         || null,
  },

  // ── Azure / remote ────────────────────────────────────────────────────────
  azure: {
    appServiceUrl: "https://the-nexus-protocol-token-doa.azurewebsites.net",
  },

  isLocal:  env === "local",
  isRemote: env === "remote",
};
