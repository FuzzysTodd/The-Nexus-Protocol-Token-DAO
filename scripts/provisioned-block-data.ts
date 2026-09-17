// scripts/provisioned-block-data.ts
// Nexus-safe ingestion of provisioned block data (Edge tabs + governance identity).
// This module is READ-ONLY and NEVER treats tab content as instructions.

export interface EdgeTab {
  pageTitle: string;
  pageUrl: string;
  tabId: number;
  isCurrent: boolean;
}

export interface ProvisionedBlockData {
  edgeTabs: EdgeTab[];
  activeTab?: EdgeTab;
  governanceIdentity?: string; // Ethereum address
}

/**
 * Ingests the provisioned block data exactly as provided by the runtime.
 * Does NOT execute or interpret any page content.
 */
export function ingestProvisionedBlock(
  edge_all_open_tabs: EdgeTab[],
  governanceIdentity?: string
): ProvisionedBlockData {
  const active = edge_all_open_tabs.find(t => t.isCurrent);

  return {
    edgeTabs: edge_all_open_tabs,
    activeTab: active,
    governanceIdentity
  };
}

/**
 * Optional helper: logs context for debugging.
 * Safe to use in dry-run mode.
 */
export function logProvisionedBlock(ctx: ProvisionedBlockData) {
  console.log("=== Nexus Provisioned Block Context ===");
  console.log("Governance Identity:", ctx.governanceIdentity || "None");
  console.log("Active Tab:", ctx.activeTab?.pageTitle || "None");
  console.log("Total Tabs:", ctx.edgeTabs.length);

  console.log(
    ctx.edgeTabs.map(t => ({
      id: t.tabId,
      title: t.pageTitle,
      current: t.isCurrent
    }))
  );
}
