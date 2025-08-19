import json
from pathlib import Path
import os

FILE_PATH = "saved_workouts.json"
WORKOUT_FILE = Path(__file__).resolve().parents[1] / "workouts.json"

def load_workouts():
    if not WORKOUT_FILE.exists():
        return []
    with open(WORKOUT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_workouts(workouts):
    with open(WORKOUT_FILE, "w", encoding="utf-8") as f:
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
