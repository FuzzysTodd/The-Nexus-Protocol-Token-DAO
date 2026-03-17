"""Helpers for generating MCP task plans and provenance artifacts."""

from __future__ import annotations

import argparse
import json
import subprocess
import time
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

DEFAULT_CONFIG_PATH = Path("mcp/agents/mig-network-config.json")
DEFAULT_PLAN_DIR = Path(".agent/plans")
DEFAULT_PROVENANCE_DIR = Path(".agent/provenance")


def load_mcp_agents(
    config_path: Path = DEFAULT_CONFIG_PATH,
) -> List[Dict[str, object]]:
    """Load MCP agent definitions from the repository configuration."""

    payload = json.loads(config_path.read_text(encoding="utf-8"))
    return payload["migNetwork"]["mcpAgents"]


def build_mcp_plan(agents: Sequence[Dict[str, object]]) -> str:
    """Render MCP agents into a task-focused markdown plan."""

    lines = ["# Plan"]
    for agent in agents:
        lines.append(f'- [ ] {agent["id"]}: {agent["role"]}')
        for task in agent.get("tasks", []):
            lines.append(f"  - {task}")
    lines.append("")
    return "\n".join(lines)


def collect_repository_files(root: Path = Path(".")) -> List[str]:
    """Return a stable list of repository-tracked files for provenance."""

    try:
        result = subprocess.run(
            ["git", "-C", str(root), "ls-files"],
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return sorted(
            str(path.relative_to(root)).replace("\\", "/")
            for path in root.rglob("*")
            if path.is_file()
        )

    return sorted(line for line in result.stdout.splitlines() if line)


def write_mcp_plan_and_provenance(
    *,
    config_path: Path = DEFAULT_CONFIG_PATH,
    plan_dir: Path = DEFAULT_PLAN_DIR,
    provenance_dir: Path = DEFAULT_PROVENANCE_DIR,
    root: Path = Path("."),
    timestamp: Optional[int] = None,
) -> Tuple[Path, Path]:
    """Write MCP plan and provenance artifacts to disk."""

    ts = int(time.time()) if timestamp is None else timestamp
    agents = load_mcp_agents(config_path)

    plan_dir.mkdir(parents=True, exist_ok=True)
    provenance_dir.mkdir(parents=True, exist_ok=True)

    plan_path = plan_dir / f"plan-{ts}.md"
    plan_path.write_text(build_mcp_plan(agents), encoding="utf-8")

    provenance = {
        "ts": ts,
        "files": collect_repository_files(root),
        "agents": [
            {
                "id": agent["id"],
                "role": agent["role"],
                "tasks": agent.get("tasks", []),
                "priority": agent.get("priority"),
            }
            for agent in agents
        ],
    }
    provenance_path = provenance_dir / f"{ts}.json"
    provenance_path.write_text(
        json.dumps(provenance, indent=2, sort_keys=True),
        encoding="utf-8",
    )

    return plan_path, provenance_path


def main(argv: Optional[Sequence[str]] = None) -> int:
    """CLI entry point for workflow-based MCP plan generation."""

    parser = argparse.ArgumentParser(
        description="Generate MCP task plans and provenance artifacts."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=DEFAULT_CONFIG_PATH,
        help="Path to the MCP configuration JSON file.",
    )
    parser.add_argument(
        "--plan-dir",
        type=Path,
        default=DEFAULT_PLAN_DIR,
        help="Directory where markdown plans should be written.",
    )
    parser.add_argument(
        "--provenance-dir",
        type=Path,
        default=DEFAULT_PROVENANCE_DIR,
        help="Directory where provenance JSON files should be written.",
    )
    args = parser.parse_args(argv)

    plan_path, provenance_path = write_mcp_plan_and_provenance(
        config_path=args.config,
        plan_dir=args.plan_dir,
        provenance_dir=args.provenance_dir,
    )
    print(f"Generated MCP plan: {plan_path}")
    print(f"Generated provenance: {provenance_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
