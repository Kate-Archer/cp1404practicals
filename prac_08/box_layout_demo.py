from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

status_text = StringProperty()


class BoxLayoutDemo(App):
    """Boxlayout class."""
    def build(self):
        """Build the Box Layout GUI."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def press_clear(self):
        """Clear the inputted name."""
        self.root.ids.input_name.text = ""

    def handle_greet(self):
        """Handle the greet button pressed by greeting the user (with the name input)."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()