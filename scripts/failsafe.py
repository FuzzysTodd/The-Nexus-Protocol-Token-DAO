import json
from pathlib import Path

STATE_PATH = Path("failsafe/state.json")

def load_state():
    if not STATE_PATH.exists():
        return {
            "martial_law": False,
            "activated_by": None,
            "activated_at": None,
            "reason": None,
        }
    with STATE_PATH.open() as f:
        return json.load(f)

def failsafe_active():
    state = load_state()
    return bool(state.get("martial_law", False))
