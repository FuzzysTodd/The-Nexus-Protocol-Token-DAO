import { execFileSync } from "node:child_process";
import {
  evaluateMergeAbort,
  type MergeAbortInput,
} from "./merge-abort-policy";
import { tightenAndResolve, type HunkResolution } from "./tight-hunk-parser";

export type RouteCommit = (commitHash: string) => Promise<unknown>;
export type BranchViolation = {
  code: string;
  branch: string;
  commitHash: string;
};

export interface ProtectedMergeInput extends MergeAbortInput {}

export interface ProtectedMergeResult {
  status: "ABORTED" | "RESOLVED";
  file: string;
  resolved?: HunkResolution;
  reasons?: string[];
  committed: false;
  published: false;
  governanceOverride: boolean;
}

export interface RouteOptions {
  /**
   * The oldest commit to exclude from the route. A range is mandatory so that
   * branch history cannot be swept accidentally.
   */
  since: string;
  /** Preview commits without invoking the routing handler. */
  dryRun?: boolean;
  /** Prevent an unexpectedly large route from consuming unbounded resources. */
  maxCommits?: number;
  /**
   * Explicitly authorize routing from a protected branch in write mode.
   * Protected branches remain dry-run only unless this is true.
   */
  allowProtectedBranchWrites?: boolean;
}

/**
 * Prepares a protected-branch conflict resolution without changing Git state.
 * Ambiguous hunks fail closed and must be resolved by a human.
 */
export function protectedMergeRouter(
  input: ProtectedMergeInput,
): ProtectedMergeResult {
  const decision = evaluateMergeAbort(input);
  const governanceOverride = Boolean(
    input.governanceOverride?.reason.trim()
      && input.governanceOverride?.approvalReference.trim(),
  );
  if (decision.abort) {
    return {
      status: "ABORTED",
      file: input.filePath,
      reasons: decision.reasons,
      committed: false,
      published: false,
      governanceOverride,
    };
  }

  const resolved = tightenAndResolve(
    input.filePath,
    input.ours,
    input.theirs,
  );
  if (resolved.status === "ambiguous") {
    return {
      status: "ABORTED",
      file: input.filePath,
      reasons: ["invented-behavior"],
      committed: false,
      published: false,
      governanceOverride,
    };
  }

  return {
    status: "RESOLVED",
    file: input.filePath,
    resolved,
    committed: false,
    published: false,
    governanceOverride,
  };
}

const DEFAULT_MAX_COMMITS = 100;
const PROTECTED_BRANCHES = new Set(["MASTER", "main"]);
const BRANCHES = {
  master: "MASTER",
  main: "main",
} as const;

const ALLOWED_MERGE_SOURCES = ["develop", "staging"];

function emitViolation(code: string, branch: string, commitHash: string): void {
  const violation: BranchViolation = { code, branch, commitHash };
  console.warn(JSON.stringify({ agent: "nexus-project-router", violation }));
}

function extractMergeSource(message: string): string {
  const branchMerge = message.match(/^Merge branch ['"]([^'"]+)['"]/m);
  if (branchMerge?.[1]) {
    return branchMerge[1];
  }

  const pullRequestMerge = message.match(/^Merge pull request \S+ from [^/]+\/([^\s]+)/m);
  return pullRequestMerge?.[1] ?? "";
}

function agentHasAuthority(required: string[]): boolean {
  const configured = new Set(
    (process.env.NEXUS_AGENT_AUTHORITIES ?? "")
      .split(",")
      .map((permission) => permission.trim())
      .filter(Boolean),
  );
  return required.every((permission) => configured.has(permission));
}

/**
 * Enforces commit policy before any protected-branch routing action.
 *
 * Protected branches accept only approved merge commits from develop/staging,
 * tagged with [NEXUS], signed by NexusAgent, and authorized by the runtime.
 */
export function enforceBranchProtection(
  branch: string,
  commitHash: string,
  message: string,
): void {
  assertCommitSha(commitHash, "commitHash");
  if (!PROTECTED_BRANCHES.has(branch)) {
    return;
  }

  const isMerge = message.includes("Merge");
  if (!isMerge) {
    emitViolation("DIRECT_COMMIT_BLOCKED", branch, commitHash);
    throw new Error(`Direct commits to ${branch} are prohibited.`);
  }

  const mergeSource = extractMergeSource(message);
  if (!ALLOWED_MERGE_SOURCES.some((source) => mergeSource.startsWith(source))) {
    emitViolation("UNAUTHORIZED_MERGE_ATTEMPT", branch, commitHash);
    throw new Error(`Merge from ${mergeSource || "unknown"} into ${branch} is not allowed.`);
  }

  if (!message.includes("[NEXUS]")) {
    emitViolation("BAD_COMMIT_MESSAGE", branch, commitHash);
    console.warn(`Commit ${commitHash} is missing required tag [NEXUS].`);
  }

  if (!agentHasAuthority(["nexus.project.write", "nexus.status.write"])) {
    emitViolation("MISSING_AUTHORITY", branch, commitHash);
    throw new Error("Agent lacks required authority for protected branch operations.");
  }

  if (!message.includes("Signed-off-by: NexusAgent")) {
    emitViolation("SIGNATURE_REQUIRED", branch, commitHash);
    throw new Error("Commit requires NexusAgent signature.");
  }
}

function assertCommitSha(value: string, label: string): void {
  if (!/^[0-9a-f]{7,40}$/i.test(value)) {
    throw new Error(`${label} must be a hexadecimal commit SHA`);
  }
}

function assertOptions(options: RouteOptions): Required<RouteOptions> {
  assertCommitSha(options.since, "since");

  const maxCommits = options.maxCommits ?? DEFAULT_MAX_COMMITS;
  if (!Number.isInteger(maxCommits) || maxCommits < 1 || maxCommits > 1000) {
    throw new Error("maxCommits must be an integer between 1 and 1000");
  }

  return {
    since: options.since,
    dryRun: options.dryRun ?? true,
    maxCommits,
    allowProtectedBranchWrites: options.allowProtectedBranchWrites ?? false,
  };
}

function assertProtectedBranchPolicy(
  branch: string,
  options: Required<RouteOptions>,
): void {
  if (!PROTECTED_BRANCHES.has(branch)) {
    throw new Error(`Branch '${branch}' is not an approved routing target`);
  }
  if (!options.dryRun && !options.allowProtectedBranchWrites) {
    throw new Error(
      `Write routing for protected branch '${branch}' requires allowProtectedBranchWrites: true`,
    );
  }
}

function assertBranchExists(branch: string): void {
  try {
    execFileSync("git", ["rev-parse", "--verify", "--quiet", `refs/heads/${branch}`], {
      stdio: ["ignore", "ignore", "pipe"],
    });
  } catch {
    throw new Error(`Required local branch '${branch}' was not found`);
  }
}

function commitsForBranch(branch: string, options: Required<RouteOptions>): string[] {
  assertProtectedBranchPolicy(branch, options);
  assertBranchExists(branch);
  assertCommitSha(options.since, "since");

  const output = execFileSync(
    "git",
    [
      "rev-list",
      `--max-count=${options.maxCommits + 1}`,
      `${options.since}..refs/heads/${branch}`,
    ],
    { encoding: "utf8" },
  ).trim();

  const commits = output === "" ? [] : output.split(/\r?\n/);
  if (commits.length > options.maxCommits) {
    throw new Error(
      `Route for '${branch}' exceeds maxCommits (${options.maxCommits}); narrow the range`,
    );
  }
  return commits;
}

function commitMessage(commitHash: string): string {
  return execFileSync("git", ["show", "-s", "--format=%B", commitHash], {
    encoding: "utf8",
  });
}

async function routeBranches(
  branches: readonly string[],
  options: RouteOptions,
  routeCommit: RouteCommit,
): Promise<string[]> {
  const validated = assertOptions(options);
  const commits = [
    ...new Set(branches.flatMap((branch) => commitsForBranch(branch, validated))),
  ];

  for (const branch of branches) {
    for (const commit of commitsForBranch(branch, validated)) {
      enforceBranchProtection(branch, commit, commitMessage(commit));
    }
  }

  if (validated.dryRun) {
    return commits;
  }

  for (const commit of commits) {
    await routeCommit(commit);
  }
  return commits;
}

/**
 * Routes bounded commits from MASTER. Dry-run mode is the default.
 *
 * @param options Explicit commit boundary and optional dry-run settings.
 * @param routeCommitHandler Approved handler for a single commit.
 */
export async function routeMaster(
  options: RouteOptions,
  routeCommitHandler: RouteCommit,
): Promise<string[]> {
  return routeBranches([BRANCHES.master], options, routeCommitHandler);
}

/**
 * Routes bounded commits from main. Dry-run mode is the default.
 *
 * @param options Explicit commit boundary and optional dry-run settings.
 * @param routeCommitHandler Approved handler for a single commit.
 */
export async function routeMain(
  options: RouteOptions,
  routeCommitHandler: RouteCommit,
): Promise<string[]> {
  return routeBranches([BRANCHES.main], options, routeCommitHandler);
}

/**
 * Routes the deduplicated union of bounded commits from MASTER and main.
 *
 * @param options Explicit commit boundary and optional dry-run settings.
 * @param routeCommitHandler Approved handler for a single commit.
 */
export async function routeBoth(
  options: RouteOptions,
  routeCommitHandler: RouteCommit,
): Promise<string[]> {
  return routeBranches(
    [BRANCHES.master, BRANCHES.main],
    options,
    routeCommitHandler,
  );
}
