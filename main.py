from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# from app.screens.home_screen import HomeScreen
from app.screens.exercise_list_screen import ExerciseListScreen
from app.screens.exercise_detail_screen import ExerciseDetailScreen
from app.screens.build_workout_screen import WorkoutBuilderScreen

class HomeScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ExerciseApp(App):
    def build(self):
        # Load KV files
        Builder.load_file("kv/home.kv")
        Builder.load_file("kv/exercise_list.kv")
        Builder.load_file("kv/exercise_detail.kv")
        Builder.load_file("kv/build_workout.kv")

        sm = WindowManager()
        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(ExerciseListScreen(name="exercise_list"))
        sm.add_widget(ExerciseDetailScreen(name="exercise_detail"))
        sm.add_widget(WorkoutBuilderScreen(name="build_workout"))

        return sm

if __name__ == "__main__":
    ExerciseApp().run()



