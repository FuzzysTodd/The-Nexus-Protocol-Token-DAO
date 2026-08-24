import json
from pathlib import Path
from failsafe import failsafe_active

REGISTRY_PATH = Path("mcp/nexus-agent-registry.json")

def load_registry():
    with REGISTRY_PATH.open() as f:
        return json.load(f)

def resolve_martial_law():
    registry = load_registry()
    ml_failsafe = failsafe_active()
    ml_registry = registry.get("failsafe", {}).get("martial_law", False)
    return ml_failsafe or ml_registry

def run_ai_governance_cycle():
    print("[GOVERNANCE] Running AI/automation governance cycle...")
    # TODO: your existing AI-driven governance logic
    # proposal scoring, auto-execution, auto-close, etc.

def run_manual_governance_cycle():
    print("[GOVERNANCE] Running MANUAL governance cycle...")
    # TODO: deterministic manual governance logic
    # human review, manual proposal queue, manual execution

def run_governance_engine():
    martial_law = resolve_martial_law()

    if martial_law:
        print("[MARTIAL LAW] Governance engine in manual-only mode.")
        run_manual_governance_cycle()
    else:
        run_ai_governance_cycle()

if __name__ == "__main__":
    run_governance_engine()
