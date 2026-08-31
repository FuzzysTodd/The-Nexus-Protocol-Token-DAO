/agent
  /tools
    dune.ts
  /prompts
    system.md
  index.ts

import fetch from "node-fetch";

const DUNE_API_KEY = process.env.DUNE_API_KEY!;
const BASE = "https://api.dune.com/api/v1";

export async function runDuneQuery(queryId: number, params: Record<string, any> = {}) {
  const res = await fetch(`${BASE}/query/${queryId}/results`, {
    method: "POST",
    headers: {
      "x-dune-api-key": DUNE_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ query_parameters: params }),
  });

  if (!res.ok) {
    throw new Error(`Dune error ${res.status}: ${await res.text()}`);
  }

  const data = await res.json();
  return data.result?.rows ?? [];
}
