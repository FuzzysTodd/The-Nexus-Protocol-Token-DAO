import json
import datetime
from pathlib import Path

STATE_PATH = Path("failsafe/state.json")

def main():
    if STATE_PATH.exists():
        with STATE_PATH.open() as f:
            state = json.load(f)
    else:
        state = {
            "martial_law": False,
            "activated_by": None,
            "activated_at": None,
            "reason": None,
        }

    state["martial_law"] = True
    state["activated_by"] = "todd"
    state["activated_at"] = datetime.datetime.utcnow().isoformat()
    state["reason"] = "AI/automation outage / single-point failure risk"

    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with STATE_PATH.open("w") as f:
        json.dump(state, f, indent=4)

    print("✅ Martial law declared. Failsafe mode is now ACTIVE.")

if __name__ == "__main__":
    main()
