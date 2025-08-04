import json
from pathlib import Path

def load_exercises():
    # Always resolve from the project root
    project_root = Path(__file__).resolve().parents[2]  # utils → app → root
    db_path = project_root / "exercise_data.json"

    if not db_path.exists():
        print(f"⚠️ Database not found at {db_path}")
        return []

    with open(db_path, "r") as f:
        return json.load(f)
