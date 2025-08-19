from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty

class WorkoutBuilderScreen(Screen):
    workout = ListProperty([])  # Stores exercises with sets/reps
    workout_name = ""  # User-defined name
    adding_exercise = False  # Flag to track if we're adding

    def add_exercise(self, exercise):
        # Add exercise with default sets/reps
        self.workout.append({
            "name": exercise["name"],
            "sets": 3,
            "reps": 10
        })
        self.refresh_workout_list()

    def refresh_workout_list(self):
        container = self.ids.workout_list
        container.clear_widgets()
        for ex in self.workout:
            container.add_widget(
                self.create_exercise_item(ex)
            )

    def create_exercise_item(self, ex):
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.label import Label
        from kivy.uix.button import Button

        layout = BoxLayout(orientation="horizontal", size_hint_y=None, height=40)
        layout.add_widget(Label(text=f"{ex['name']} - {ex['sets']}x{ex['reps']}"))
        # Buttons for adjusting sets/reps
        inc_sets = Button(text="+Set", size_hint_x=None, width=70)
        dec_sets = Button(text="-Set", size_hint_x=None, width=70)
        inc_reps = Button(text="+Rep", size_hint_x=None, width=70)
        dec_reps = Button(text="-Rep", size_hint_x=None, width=70)

        inc_sets.bind(on_release=lambda _: self.change_sets(ex, 1))
        dec_sets.bind(on_release=lambda _: self.change_sets(ex, -1))
        inc_reps.bind(on_release=lambda _: self.change_reps(ex, 1))
        dec_reps.bind(on_release=lambda _: self.change_reps(ex, -1))

        layout.add_widget(inc_sets)
        layout.add_widget(dec_sets)
        layout.add_widget(inc_reps)
        layout.add_widget(dec_reps)
        return layout

    def change_sets(self, ex, delta):
        ex["sets"] = max(1, ex["sets"] + delta)
        self.refresh_workout_list()

    def change_reps(self, ex, delta):
        ex["reps"] = max(1, ex["reps"] + delta)
        self.refresh_workout_list()

    def save_workout(self):
        if not self.workout_name.strip():
            print("Please enter a workout name!")
            return

        workout_data = {
            "name": self.workout_name,
            "exercises": self.workout
        }

        # Persist to storage (we can use JSON file)
        from app.utils import storage
        storage.save_workout(workout_data)

        print(f"Workout '{self.workout_name}' saved with {len(self.workout)} exercises.")
        self.workout.clear()
        self.workout_name = ""
        self.refresh_workout_list()
        self.manager.current = "home"

