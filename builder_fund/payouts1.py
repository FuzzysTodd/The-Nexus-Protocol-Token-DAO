from pathlib import Path
import json
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

def process_payout(payout):
    """
    Core payout handler.
    `payout` can be a dict with fields like:
    - recipient
    - amount
    - reason
    - stream_id
    """
    martial_law = resolve_martial_law()

    if martial_law:
        print(f"[MARTIAL LAW] Blocking payout to {payout.get('recipient')} amount={payout.get('amount')}.")
        # Optionally log to a manual review queue instead of executing:
        # queue_for_manual_review(payout)
        return

    print(f"[PAYOUT] Executing payout to {payout.get('recipient')} amount={payout.get('amount')}.")
    # TODO: your actual on-chain / off-chain payout logic here
    # e.g. call treasury contract, send transaction, etc.

def process_payouts_batch(payouts):
    """
    Process a list of payouts.
    """
    for payout in payouts:
        process_payout(payout)

if __name__ == "__main__":
    # Example usage: load a batch from JSON
    batch_path = Path("builder_fund/payouts_batch.json")
    if batch_path.exists():
        with batch_path.open() as f:
            payouts = json.load(f)
        process_payouts_batch(payouts)
    else:
        print("[PAYOUT] No batch file found.")
