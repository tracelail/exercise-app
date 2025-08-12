from kivy.uix.screenmanager import Screen
from pathlib import Path

class ExerciseDetailScreen(Screen):
    def set_exercise(self, exercise):
        self.ids.exercise_name.text = exercise["name"]
        self.ids.exercise_desc.text = f"Target: {exercise['primaryMuscles']}\nEquipment: {exercise['equipment']}\nInstructions: {exercise['instructions']}"
        # Use gifUrl if you want
        self.ids.exercise_image.source = exercise.get("gifUrl", "assets/placeholder.png")