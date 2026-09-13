import type { GovernanceOverride } from "./merge-abort-policy";

export type GovernanceAction =
  | "ALLOW_PROTECTED"
  | "ALLOW_INVARIANT"
  | "ALLOW_MISSING_TESTS"
  | "ALLOW_INVENTED_BEHAVIOR";

export interface GovernanceDecision {
  proposalId: string;
  action: GovernanceAction;
  approved: boolean;
  reason: string;
  signatures: string[];
}

export interface GovernanceOverrideResult {
  approved: boolean;
  proposalId: string;
  override?: GovernanceOverride;
  reason?: string;
}

const ACTION_TO_OVERRIDE: Record<
  GovernanceAction,
  keyof Omit<GovernanceOverride, "reason" | "approvalReference">
> = {
  ALLOW_PROTECTED: "allowProtectedPathMerge",
  ALLOW_INVARIANT: "allowInvariantConflictMerge",
  ALLOW_MISSING_TESTS: "allowMissingChecksMerge",
  ALLOW_INVENTED_BEHAVIOR: "allowInventedBehaviorMerge",
};

function isValidSignature(signature: string): boolean {
  return /^0x[0-9a-f]{40}$/i.test(signature);
}

function hasEnoughSignatures(signatures: string[], required: number): boolean {
  const validSignatures = new Set(signatures.filter(isValidSignature));
  return validSignatures.size >= required;
}

/**
 * Converts an approved, multisigned governance decision into a scoped router
 * override. The caller must pass the returned override to one merge request.
 */
export function applyGovernanceDecision(
  decision: GovernanceDecision,
): GovernanceOverrideResult {
  const proposalId = decision.proposalId.trim();
  const reason = decision.reason.trim();
  const signatures = [
    ...new Set(decision.signatures.filter(isValidSignature)),
  ];

  if (!decision.approved) {
    return {
      approved: false,
      proposalId,
      reason: "Governance decision was not approved.",
    };
  }
  if (!proposalId) {
    throw new Error("Governance decision requires a proposalId.");
  }
  if (!reason) {
    throw new Error("Approved governance decision requires a reason.");
  }
  if (signatures.length < 2) {
    throw new Error("Approved governance decision requires at least two valid signatures.");
  }

  const overrideKey = ACTION_TO_OVERRIDE[decision.action];
  return {
    approved: true,
    proposalId,
    override: {
      [overrideKey]: true,
      reason,
      approvalReference: proposalId,
    } as GovernanceOverride,
  };
}

/**
 * Applies a decision only when its approved, unique signer set meets the
 * requested threshold. Invalid or insufficient decisions are rejected without
 * creating an override.
 */
export function applyGovernanceDecisionWithThreshold(
  decision: GovernanceDecision,
  requiredSignatures = 2,
): GovernanceOverrideResult | undefined {
  if (
    !Number.isInteger(requiredSignatures)
    || requiredSignatures < 2
    || !hasEnoughSignatures(decision.signatures, requiredSignatures)
  ) {
    return undefined;
  }

  return applyGovernanceDecision(decision);
}
