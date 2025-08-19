from kivy.uix.screenmanager import Screen
from pathlib import Path

class ExerciseDetailScreen(Screen):
    def set_exercise(self, exercise):
        self.ids.exercise_name.text = exercise["name"]
        self.ids.exercise_desc.text = (
            f"Target: {exercise['primaryMuscles']}\n"
            f"Equipment: {exercise['equipment']}\n"
            f"Instructions: {exercise['instructions']}"
        )

        base_url = "https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/exercises/"
        if exercise.get("images"):
            self.ids.exercise_image.source = base_url + exercise["images"][0]
        else:
            self.ids.exercise_image.source = "assets/placeholder.png"
