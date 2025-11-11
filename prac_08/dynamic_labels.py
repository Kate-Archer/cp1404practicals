"""
Dynamically create labels based on a list of names
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to create dynamic labels (with a widget) based on a list of names."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app using a list of names."""
        super().__init__(**kwargs)
        self.names = {"John", "Steve", "Mary", "Abi", "Luna", "Tom"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Name Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from the given names and add them to the GUI."""
        print("Labels added")
        for name in self.names:
            # Create a label for each name in the list
            temp_label = Label(text=name)

            # Add the label to the "entries_box" layout widget
            self.root.ids.entries_box.add_widget(temp_label)

    def clear_all(self):
        """Clear all widgets that are children of the "entries_box" layout widget."""
        print("Clear all labels")
        self.root.ids.entries_box.clear_widgets()


DynamicLabelsApp().run()
