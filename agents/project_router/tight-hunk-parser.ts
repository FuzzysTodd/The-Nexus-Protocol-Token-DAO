export type HunkResolution =
  | { status: "resolved"; content: string }
  | { status: "ambiguous"; reason: string };

/**
 * Resolves only mechanically safe hunks. Non-empty, differing sides require
 * a human because combining arbitrary blocks can invent or duplicate behavior.
 */
export function tightenAndResolve(
  _filePath: string,
  ours: string,
  theirs: string,
): HunkResolution {
  if (ours === theirs) {
    return { status: "resolved", content: ours };
  }
  if (ours.trim() === "") {
    return { status: "resolved", content: theirs };
  }
  if (theirs.trim() === "") {
    return { status: "resolved", content: ours };
  }

  return {
    status: "ambiguous",
    reason: "Both sides contain different non-empty content.",
  };
}
