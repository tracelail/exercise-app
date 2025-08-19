from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
import json
from pathlib import Path

class ExerciseListScreen(Screen):
    def on_pre_enter(self):
        self.load_exercises()

    def load_exercises(self):
        data_path = Path(__file__).resolve().parents[2] / "exercise_data.json"
        if not data_path.exists():
            print(f"⚠️ Database not found at {data_path}")
            return []
        with open(data_path, "r", encoding="utf-8") as f:
            self.exercises = json.load(f)
        self.display_exercises(self.exercises)

    def display_exercises(self, exercises):
        container = self.ids.exercise_list
        container.clear_widgets()
        for exercise in exercises:
            btn = Button(
                text=exercise["name"],
                size_hint_y=None,
                height=40
            )
            btn.bind(on_release=lambda _, e=exercise: self.show_detail(e))
            container.add_widget(btn)

    def filter_exercises(self, query):
        filtered = [
            e for e in self.exercises if query.lower() in e["name"].lower()
        ]
        self.display_exercises(filtered)

    def show_detail(self, exercise):
        builder_screen = self.manager.get_screen("build_workout")

        if builder_screen.adding_exercise:
            # We're in workout building mode → add exercise
            builder_screen.add_exercise(exercise)
            builder_screen.adding_exercise = False
            self.manager.current = "build_workout"
        else:
            # Normal behavior → show details
            detail_screen = self.manager.get_screen("exercise_detail")
            detail_screen.set_exercise(exercise)
            self.manager.current = "exercise_detail"

