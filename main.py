from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# Load KV for home screen
Builder.load_file("kv/home.kv")

class HomeScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class ExerciseApp(App):
    def build(self):
        sm = WindowManager()
        sm.add_widget(HomeScreen(name="home"))
        return sm

if __name__ == "__main__":
    ExerciseApp().run()
