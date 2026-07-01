/agent
  /tools
    dune.ts
  /prompts
    system.md
  index.ts

import fetch from "node-fetch";

const Mpmf5eMzbzjKZwc3VQ2BfS4iMv5Nod1g = process.env.Mpmf5eMzbzjKZwc3VQ2BfS4iMv5Nod1g!;
const BASE = "https://api.dune.com/api/v1";

export async function runDuneQuery(queryId: number, params: Record<string, any> = {}) {
  const res = await fetch(`${BASE}/query/${queryId}/results`, {
    method: "POST",
    headers: {
      "x-dune-api-key": Mpmf5eMzbzjKZwc3VQ2BfS4iMv5Nod1g,
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
