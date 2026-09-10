import json
from pathlib import Path

STATE_PATH = Path("failsafe/state.json")

def main():
    if not STATE_PATH.exists():
        print("No failsafe state file found.")
        return

    with STATE_PATH.open() as f:
        state = json.load(f)

    state["martial_law"] = False

    with STATE_PATH.open("w") as f:
        json.dump(state, f, indent=4)

    print("✅ Martial law revoked. Normal operations restored.")

if __name__ == "__main__":
    main()
