export const PROTECTED_PATHS = [
  ".env",
  ".github/agents/",
  ".github/workflows/",
  "contracts/",
  "config/credentials",
  "governance/",
  "mcp/",
  "secrets/",
  "treasury/",
] as const;

export const SECURITY_INVARIANTS = [
  "requireOwner",
  "onlyDAO",
  "onlyTreasury",
  "onlyGovernance",
  "nonReentrant",
  "invariant(",
] as const;

export type MergeAbortReason =
  | "protected-path"
  | "incompatible-security-invariant"
  | "checks-unavailable"
  | "invented-behavior";

export interface MergeAbortDecision {
  abort: boolean;
  reasons: MergeAbortReason[];
}

export interface GovernanceOverride {
  allowProtectedPathMerge?: boolean;
  allowInvariantConflictMerge?: boolean;
  allowMissingChecksMerge?: boolean;
  allowInventedBehaviorMerge?: boolean;
  reason: string;
  approvalReference: string;
}

function normalizePath(filePath: string): string {
  return filePath.replaceAll("\\", "/").toLowerCase();
}

export function fileTouchesProtectedArea(filePath: string): boolean {
  const normalizedPath = normalizePath(filePath);
  return PROTECTED_PATHS.some((protectedPath) => {
    const normalizedProtectedPath = protectedPath.toLowerCase();
    return normalizedPath === normalizedProtectedPath
      || normalizedPath.startsWith(normalizedProtectedPath)
      || normalizedPath.includes(`/${normalizedProtectedPath}`);
  });
}

function securityInvariantSet(text: string): Set<string> {
  return new Set(
    SECURITY_INVARIANTS.filter((invariant) => text.includes(invariant)),
  );
}

export function hunkTouchesSecurityInvariant(hunk: string): boolean {
  return securityInvariantSet(hunk).size > 0;
}

export function resolutionWouldInventBehavior(
  ours: string,
  theirs: string,
): boolean {
  const oursInvariants = securityInvariantSet(ours);
  const theirsInvariants = securityInvariantSet(theirs);
  const sharedInvariants = [...oursInvariants].filter((invariant) =>
    theirsInvariants.has(invariant),
  );

  return sharedInvariants.length > 0 && ours.trim() !== theirs.trim();
}

export interface MergeAbortInput {
  filePath: string;
  ours: string;
  theirs: string;
  /** True only when the required project checks can actually run. */
  checksAvailable: boolean;
  /** True when the proposed resolution adds behavior absent from both sides. */
  inventsBehavior?: boolean;
  /** Optional explicit governance authorization; omitted means fail-closed. */
  governanceOverride?: GovernanceOverride;
}

function hasValidOverride(
  override: GovernanceOverride | undefined,
): override is GovernanceOverride {
  return Boolean(
    override
      && override.reason.trim()
      && override.approvalReference.trim(),
  );
}

export function evaluateMergeAbort(input: MergeAbortInput): MergeAbortDecision {
  const reasons: MergeAbortReason[] = [];
  const override = hasValidOverride(input.governanceOverride)
    ? input.governanceOverride
    : undefined;

  if (
    fileTouchesProtectedArea(input.filePath)
    && !override?.allowProtectedPathMerge
  ) {
    reasons.push("protected-path");
  }
  if (
    resolutionWouldInventBehavior(input.ours, input.theirs)
    && !override?.allowInvariantConflictMerge
  ) {
    reasons.push("incompatible-security-invariant");
  }
  if (!input.checksAvailable && !override?.allowMissingChecksMerge) {
    reasons.push("checks-unavailable");
  }
  if (input.inventsBehavior === true && !override?.allowInventedBehaviorMerge) {
    reasons.push("invented-behavior");
  }

  return {
    abort: reasons.length > 0,
    reasons,
  };
}

/**
 * Convenience wrapper for callers that only need the policy result.
 *
 * This function deliberately does not execute package managers, Git commands,
 * merge operations, or abort operations.
 */
export function shouldAbortMerge(input: MergeAbortInput): boolean {
  return evaluateMergeAbort(input).abort;
}
