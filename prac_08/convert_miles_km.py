from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

# CONSTANT: miles to kilometres factor conversion
MILES_TO_KM_CONVERSION = 1.60934


class ConvertMilesToKmApp(App):
    """
    ConvertMilesToKmApp is a Kivy App for converting a number from miles to kilometres.
    It also decreases or increases the input value by 1 if the up or down button are pressed.
    """

    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        Window.size = (600, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation (miles to kilometres), output result to label widget."""
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_to_km(miles)

    def convert_to_number(self, text):
        """Convert text to float if invalid input given by user."""
        try:
            print("convert to number")
            return float(text)
        except ValueError:
            # Set the output result to 0.0 to prevent an error
            return 0.0

    def update_to_km(self, miles):
        """Update miles input to kilometres as a string."""
        self.output_km = str(miles * MILES_TO_KM_CONVERSION)

    def handle_increment(self, text, change):
        """Handle up or down button press by updating the text float value based on the incremental change. Call calculation function."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)


ConvertMilesToKmApp().run()