/src/config/nexusApiSchema.ts
// ------------------------------------------------------------
// NEXUS + ALSN AUTOMATION REQUEST SCHEMA
// This file defines the canonical API input format for ALL:
// - Azure Functions
// - Bots
// - Workflows (Logic Apps)
// - Telemetry producers
// - AI agents
// ------------------------------------------------------------

export enum NexusServiceType {
  AUTOMATION = "automation",
  AI_AGENT = "ai-agent",
  TELEMETRY = "telemetry",
  DASHBOARD = "dashboard",
  GOVERNANCE = "governance",
  WORKFLOW = "workflow",
}

export enum NexusUsageType {
  AI_CALL = "ai-call",
  WORKFLOW_RUN = "workflow-run",
  TELEMETRY_INGEST = "telemetry-ingest",
  DASHBOARD_READ = "dashboard-read",
  BOT_TRIGGER = "bot-trigger",
  SYSTEM_EVENT = "system-event",
}

export interface NexusAutomationRequest {
  // Required core Nexus fields
  nexusChainId: string;            // e.g. "nexus-main", "nexus-dev"
  nexusWorkflowId: string;         // unique ID for bot/workflow
  nexusServiceType: NexusServiceType;
  nexusCaller: string;             // "steward", "tokenholder", "system", "bot"

  // Required metadata
  timestamp: string;               // ISO timestamp
  usageEventId: string;            // unique event ID
  usageType: NexusUsageType;       // type of billable event
  usageUnits: number;              // normalized compute units

  // Optional ALSN fields
  alsnRegionId?: string;           // e.g. "atlanta-metro", "pilot-01"
  stewardId?: string;              // unique Steward ID
  stewardshipTitleId?: string;     // unique Title ID

  // Optional payload for bots/AI/workflows
  payload?: any;
}

// ------------------------------------------------------------
// VALIDATION FUNCTION
// Ensures every Function/bot/workflow receives proper inputs
// ------------------------------------------------------------

export function validateNexusRequest(req: any): { valid: boolean; errors: string[] } {
  const errors: string[] = [];

  if (!req.nexusChainId) errors.push("Missing: nexusChainId");
  if (!req.nexusWorkflowId) errors.push("Missing: nexusWorkflowId");
  if (!req.nexusServiceType) errors.push("Missing: nexusServiceType");
  if (!req.nexusCaller) errors.push("Missing: nexusCaller");
  if (!req.timestamp) errors.push("Missing: timestamp");
  if (!req.usageEventId) errors.push("Missing: usageEventId");
  if (!req.usageType) errors.push("Missing: usageType");
  if (typeof req.usageUnits !== "number") errors.push("Missing or invalid: usageUnits");

  return {
    valid: errors.length === 0,
    errors,
  };
}

// ------------------------------------------------------------
// NORMALIZED RESPONSE FORMAT
// Every Function/bot/workflow should return this structure
// ------------------------------------------------------------

export interface NexusAutomationResponse {
  success: boolean;
  usageEventId: string;
  nexusWorkflowId: string;
  nexusServiceType: NexusServiceType;
  timestamp: string;
  result?: any;
  errors?: string[];
}
