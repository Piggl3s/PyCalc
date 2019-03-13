import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.config import Config

Config.set('graphics', 'width', '300')
Config.set('graphics', 'height', '300')


class MyGrid(Widget):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

class MyApp (App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()