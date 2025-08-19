from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from app.utils import storage

class WorkoutListScreen(Screen):
    def on_pre_enter(self):
        self.refresh_workouts()

    def refresh_workouts(self):
        container = self.ids.workout_list
        container.clear_widgets()
        workouts = storage.load_workouts()

        for workout in workouts:
            btn = Button(
                text=workout["name"],
                size_hint_y=None,
                height=50
            )
            btn.bind(on_release=lambda _, w=workout: self.view_workout(w))
            container.add_widget(btn)

    def view_workout(self, workout):
        # Navigate to detail screen or workout builder
        detail_screen = self.manager.get_screen("build_workout")
        detail_screen.workout_name = workout["name"]
        detail_screen.workout = workout["exercises"]
        detail_screen.refresh_workout_list()
        self.manager.current = "build_workout"

    def delete_workout(self, workout_name):
        workouts = storage.load_workouts()
        workouts = [w for w in workouts if w["name"] != workout_name]
        storage.save_workouts(workouts)
        self.refresh_workouts()
