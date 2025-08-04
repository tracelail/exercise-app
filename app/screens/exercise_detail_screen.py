from kivy.uix.screenmanager import Screen
from pathlib import Path

class ExerciseDetailScreen(Screen):
    def set_exercise(self, exercise):
        self.ids.exercise_name.text = exercise["name"]
        self.ids.exercise_desc.text = exercise["description"]

        assets_dir = Path("assets")
        image_file = exercise.get("image")
        image_path = assets_dir / image_file if image_file else None

        if image_file and image_path.exists():
            self.ids.exercise_image.source = str(image_path)
        else:
            self.ids.exercise_image.source = str(assets_dir / "placeholder.png")
