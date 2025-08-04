from kivy.uix.screenmanager import Screen
from app.utils.storage import load_exercises
from kivy.uix.button import Button

class ExerciseListScreen(Screen):
    def on_pre_enter(self):
        self.exercises = load_exercises()
        self.display_exercises(self.exercises)

    def filter_exercises(self, query):
        filtered = [
            ex for ex in self.exercises 
            if query.lower() in ex["name"].lower()
        ]
        self.display_exercises(filtered)

    def display_exercises(self, exercises):
        container = self.ids.exercise_list
        container.clear_widgets()
        for ex in exercises:
            btn = Button(
                text=ex["name"], 
                size_hint_y=None, 
                height=40
            )
            btn.bind(on_press=lambda btn, ex=ex: self.show_detail(ex))
            container.add_widget(btn)

    def show_detail(self, exercise):
        detail_screen = self.manager.get_screen("exercise_detail")
        detail_screen.set_exercise(exercise)
        self.manager.current = "exercise_detail"
