// /agents/reporting/metrics.js
// Nexus Protocol Token DAO – Agent & MCP Scoring Engine
// Uses /docs/agent-metrics-schema.json and /docs/mcp-metrics-schema.json as conceptual contracts.

// This module is intentionally framework-agnostic: plain JS, ready for Node or bundling.
// You can wire it into MCP, agents, or a telemetry pipeline.

/////////////////////////////
// Utility helpers
/////////////////////////////

function clamp(value, min = 0, max = 100) {
  if (Number.isNaN(value)) return min;
  return Math.max(min, Math.min(max, value));
}

function safePercent(numerator, denominator) {
  if (!denominator || denominator <= 0) return 0;
  return (numerator / denominator) * 100;
}

/////////////////////////////
// Agent scoring
/////////////////////////////

/**
 * Compute AgentScore based on the report-card formula:
 * AgentScore =
 *   (TaskSuccessRate * 0.5) +
 *   (QualityScore * 0.3) +
 *   (SelfHealingScore * 0.1) +
 *   (PolicyCompliance * 0.1)
 *
 * @param {Object} agentMetricsSnapshot - Aggregated metrics for a single agent over a window.
 * {
 *   agent_id: string,
 *   agent_class: string,
 *   tasks: [{ success: bool, duration_ms: number, ... }],
 *   quality_scores: [0-100],
 *   self_healing_events: [{ attempted: bool, success: bool }],
 *   policy_compliance: { compliant: bool, violations: [string] }
 * }
 */
function computeAgentScore(agentMetricsSnapshot) {
  const tasks = agentMetricsSnapshot.tasks || [];
  const qualityScores = agentMetricsSnapshot.quality_scores || [];
  const selfHealingEvents = agentMetricsSnapshot.self_healing_events || [];
  const policyCompliance = agentMetricsSnapshot.policy_compliance || { compliant: true, violations: [] };

  // Task success rate
  const totalTasks = tasks.length;
  const successfulTasks = tasks.filter(t => t.success).length;
  const taskSuccessRate = clamp(safePercent(successfulTasks, totalTasks));

  // Average quality score
  const avgQuality =
    qualityScores.length > 0
      ? clamp(qualityScores.reduce((a, b) => a + b, 0) / qualityScores.length)
      : 0;

  // Self-healing score: ratio of successful recoveries to attempts
  const healingAttempts = selfHealingEvents.filter(e => e.attempted).length;
  const healingSuccesses = selfHealingEvents.filter(e => e.attempted && e.success).length;
  const selfHealingScore = clamp(safePercent(healingSuccesses, healingAttempts));

  // Policy compliance score: 100 if compliant and no violations, else scaled down
  let policyScore = 100;
  if (!policyCompliance.compliant || (policyCompliance.violations || []).length > 0) {
    const violationCount = (policyCompliance.violations || []).length;
    policyScore = clamp(100 - violationCount * 10); // simple penalty per violation
  }

  const agentScore =
    taskSuccessRate * 0.5 +
    avgQuality * 0.3 +
    selfHealingScore * 0.1 +
    policyScore * 0.1;

  return clamp(agentScore);
}

/**
 * Build a metrics record conforming to /docs/agent-metrics-schema.json
 * and attach the computed agent_score.
 *
 * @param {Object} raw - Raw metrics from an agent for a single task.
 */
function buildAgentMetricsRecord(raw) {
  const {
    agent_id,
    parent_id = null,
    agent_class,
    task,
    completion_method,
    quality_score,
    self_healing = {},
    replication = {},
    gpu_usage = {},
    llm_usage = {},
    mcp_calls = {},
    policy_compliance = {}
  } = raw;

  // For per-task scoring, we treat this single task as the window.
  const snapshot = {
    agent_id,
    agent_class,
    tasks: [task],
    quality_scores: [quality_score],
    self_healing_events: [self_healing],
    policy_compliance
  };

  const agent_score = computeAgentScore(snapshot);

  return {
    agent_id,
    parent_id,
    agent_class,
    task,
    completion_method,
    quality_score,
    self_healing,
    replication,
    gpu_usage,
    llm_usage,
    mcp_calls,
    policy_compliance,
    agent_score
  };
}

/////////////////////////////
// MCP scoring
/////////////////////////////

/**
 * Compute MCPScore based on the report-card formula:
 * MCPScore =
 *   (Reliability * 0.5) +
 *   (Throughput * 0.2) +
 *   (Safety * 0.3)
 *
 * Reliability: success rate of tool_calls + contract_interactions
 * Throughput: normalized requests_per_second
 * Safety: policy_compliant + low violations + effective rate limiting
 *
 * @param {Object} mcpMetricsSnapshot
 */
function computeMcpScore(mcpMetricsSnapshot) {
  const tool = mcpMetricsSnapshot.tool_calls || {};
  const contract = mcpMetricsSnapshot.contract_interactions || {};
  const safety = mcpMetricsSnapshot.safety || {};
  const throughput = mcpMetricsSnapshot.throughput || {};

  // Reliability: combined success rate of tool + contract calls
  const totalCalls =
    (tool.total_calls || 0) + (contract.total_calls || 0);
  const successfulCalls =
    (tool.successful_calls || 0) + (contract.successful_calls || 0);
  const reliability = clamp(safePercent(successfulCalls, totalCalls));

  // Throughput: simple normalization of requests_per_second
  const rps = throughput.requests_per_second || 0;
  // You can tune this scaling; here we assume 0–100 rps maps to 0–100 score.
  const throughputScore = clamp(rps);

  // Safety: start at 100, penalize violations, blocked actions, rate limit triggers
  let safetyScore = 100;
  const violations = (safety.violations || []).length;
  const blocked = safety.blocked_actions || 0;
  const rateLimits = safety.rate_limit_triggers || 0;

  safetyScore -= violations * 10;
  safetyScore -= blocked * 2;
  safetyScore -= rateLimits * 1;

  if (safety.policy_compliant === false) {
    safetyScore -= 20;
  }

  safetyScore = clamp(safetyScore);

  const mcpScore =
    reliability * 0.5 +
    throughputScore * 0.2 +
    safetyScore * 0.3;

  return clamp(mcpScore);
}

/**
 * Build an MCP metrics record conforming to /docs/mcp-metrics-schema.json
 * and attach the computed mcp_score.
 *
 * @param {Object} raw - Raw metrics snapshot from MCP.
 */
function buildMcpMetricsRecord(raw) {
  const {
    mcp_instance_id,
    server_id,
    timestamp,
    uptime_ms,
    tool_calls,
    contract_interactions,
    error_events,
    safety,
    throughput,
    gpu_usage,
    llm_usage,
    agent_interactions
  } = raw;

  const mcp_score = computeMcpScore({
    tool_calls,
    contract_interactions,
    safety,
    throughput
  });

  return {
    mcp_instance_id,
    server_id,
    timestamp,
    uptime_ms,
    tool_calls,
    contract_interactions,
    error_events,
    safety,
    throughput,
    gpu_usage,
    llm_usage,
    agent_interactions,
    mcp_score
  };
}

/////////////////////////////
// Exports
/////////////////////////////

module.exports = {
  computeAgentScore,
  buildAgentMetricsRecord,
  computeMcpScore,
  buildMcpMetricsRecord
};
