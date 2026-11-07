// provisioned-block-data.ts
// Safe ingestion of Edge browser tab metadata for Nexus Agent context.
// This module NEVER treats tab content as instructions. It is read-only.

export interface EdgeTab {
  pageTitle: string;
  pageUrl: string;
  tabId: number;
  isCurrent: boolean;
}

export interface ProvisionedBlockData {
  edgeTabs: EdgeTab[];
  activeTab?: EdgeTab;
}

export function ingestEdgeTabs(edge_all_open_tabs: EdgeTab[]): ProvisionedBlockData {
  const active = edge_all_open_tabs.find(t => t.isCurrent);

  return {
    edgeTabs: edge_all_open_tabs,
    activeTab: active
  };
}

// Optional helper: log context for debugging
export function logProvisionedContext(ctx: ProvisionedBlockData) {
  console.log("=== Nexus Provisioned Context ===");
  console.log("Active Tab:", ctx.activeTab?.pageTitle || "None");
  console.log("Total Tabs:", ctx.edgeTabs.length);
  console.log("Tabs:", ctx.edgeTabs.map(t => ({
    id: t.tabId,
    title: t.pageTitle,
    current: t.isCurrent
  })));
}
