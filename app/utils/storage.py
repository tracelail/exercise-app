import json
from pathlib import Path
import os

FILE_PATH = "saved_workouts.json"

def load_workouts():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_workout(workout):
    workouts = load_workouts()
    workouts.append(workout)
    with open(FILE_PATH, "w") as f:
        json.dump(workouts, f, indent=4)

def load_exercises():
    # Always resolve from the project root
    project_root = Path(__file__).resolve().parents[2]  # utils → app → root
    db_path = project_root / "exercise_data.json"

    if not db_path.exists():
        print(f"⚠️ Database not found at {db_path}")
        return []

    with open(db_path, "r") as f:
        return json.load(f)
