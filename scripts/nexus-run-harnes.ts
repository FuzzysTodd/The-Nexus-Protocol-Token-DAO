// scripts/nexus-run-harness.ts
// Nexus Merge + Governance Run Harness (Fly-Skills Edition)

import { protectedMergeRouter } from "../agents/project_router/router.agent";
import { applyGovernanceDecisionWithThreshold } from "../agents/project_router/governance-bridge";
import { shouldAbortMerge } from "../agents/project_router/merge-abort-policy";
import { tightenAndResolve } from "../agents/project_router/tight-hunk-parser";

interface GovernanceDecision {
  proposalId: string;
  action:
    | "ALLOW_PROTECTED"
    | "ALLOW_INVARIANT"
    | "ALLOW_MISSING_TESTS"
    | "ALLOW_INVENTED_BEHAVIOR";
  approved: boolean;
  reason: string;
  signatures: string[]; // Ethereum addresses
}

interface RunOptions {
  file: string;
  ours: string;
  theirs: string;
  governance?: GovernanceDecision;
  dryRun?: boolean;
}

async function runMergeChain(opts: RunOptions) {
  console.log("=== Nexus Merge Chain (Fly-Skills Mode) ===");
  console.log("File:", opts.file);
  console.log("Dry-run:", !!opts.dryRun);

  if (opts.governance) {
    applyGovernanceDecisionWithThreshold(opts.governance, 2);
    console.log("Governance override applied:", opts.governance.reason);
  }

  const abort = shouldAbortMerge(opts.file, opts.ours, opts.theirs);

  if (abort) {
    console.log("Result: ABORTED (fail-closed)");
    return {
      status: "ABORTED",
      file: opts.file,
      committed: false,
      published: false,
      reason: "Abort conditions met"
    };
  }

  const resolved = tightenAndResolve(opts.file, opts.ours, opts.theirs);

  if (opts.dryRun) {
    console.log("Result: RESOLVED_DRY_RUN (no commits, no pushes)");
    return {
      status: "RESOLVED_DRY_RUN",
      file: opts.file,
      resolved,
      committed: false,
      published: false
    };
  }

  console.log("Result: READY_FOR_REVIEW (uncommitted, unpublished)");
  return {
    status: "READY_FOR_REVIEW",
    file: opts.file,
    resolved,
    committed: false,
    published: false
  };
}

// Simple CLI wrapper:
// Example:
//   npx ts-node scripts/nexus-run-harness.ts path/to/file.ts "OURS_BLOCK" "THEIRS_BLOCK" --dry-run
async function main() {
  const args = process.argv.slice(2);

  if (args.length < 3) {
    console.error(
      "Usage: ts-node scripts/nexus-run-harness.ts <file> <ours> <theirs> [--dry-run]"
    );
    process.exit(1);
  }

  const [file, ours, theirs, maybeDry] = args;
  const dryRun = maybeDry === "--dry-run";

  const result = await runMergeChain({
    file,
    ours,
    theirs,
    dryRun
  });

  console.log("Final:", JSON.stringify(result, null, 2));
}

main().catch(err => {
  console.error("Harness error:", err);
  process.exit(1);
});
