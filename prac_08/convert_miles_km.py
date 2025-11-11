from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

class ConvertMilesToKmApp(App):
    """ SquareNumberApp is a Kivy App for squaring a number """
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root



ConvertMilesToKmApp().run()