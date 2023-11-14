
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text='My Name is Vicks.')

TestApp().run()
