import json
from pathlib import Path
from failsafe import failsafe_active

REGISTRY_PATH = Path("mcp/nexus-agent-registry.json")

def load_registry():
    """Load the MCP agent registry JSON."""
    with REGISTRY_PATH.open() as f:
        return json.load(f)

def resolve_martial_law():
    """Determine if martial law is active."""
    registry = load_registry()
    ml_failsafe = failsafe_active()
    ml_registry = registry.get("failsafe", {}).get("martial_law", False)
    return ml_failssafe or ml_registry

def run_ai_treasury_cycle():
    print("[TREASURY] Running AI/automation treasury cycle...")
    # TODO: your existing automated treasury logic:
    # - automated payouts
    # - automated reimbursements
    # - automated validator rewards
    # - automated builder fund disbursements
    # - automated treasury balancing

def run_manual_treasury_cycle():
    print("[TREASURY] Running MANUAL treasury cycle...")
    # TODO: deterministic manual treasury logic:
    # - human approval for payouts
    # - manual validator reward distribution
    # - manual builder fund disbursement
    # - manual treasury balancing
    # - manual reimbursement review

def run_treasury_engine():
    martial_law = resolve_martial_law()

    if martial_law:
        print("[MARTIAL LAW] Treasury engine in manual-only mode.")
        run_manual_treasury_cycle()
    else:
        run_ai_treasury_cycle()

if __name__ == "__main__":
    run_treasury_engine()
