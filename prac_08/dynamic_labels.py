"""
Dynamically create labels based on a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty

from prac_05.kivy_layout import Label

NEW_COLOUR = (1, 0, 0, 1)  # RGBA for red
ALTERNATIVE_COLOUR = (1, 0, 1, 1)  # RGBA for magenta


class DynamicLabelsApp(App):
    """Main program - Kivy app to create dynamic labels based on a list of names."""
    status_text = StringProperty()

    def __init__(self, name):
        """Construct main app using name."""
        self.name = name

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Name Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the given names and add them to the GUI."""
        for name in self.name:
            # create a name for each name entry, specifying the text
            temp_label = Label(text=name)
            temp_label.bind(on_press=self.press_entry)
            # set the button's background colour
            temp_label.background_color = NEW_COLOUR
            # add the button to the "entries_box" layout widget
            self.root.ids.entries_box.add_label(temp_label)

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        self.root.ids.entries_box.clear_labels()


DynamicLabelsApp().run()
