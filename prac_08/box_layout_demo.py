from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

status_text = StringProperty()


class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def press_clear(self):
        self.root.ids.input_name.text = ""

    def handle_greet(self):
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()
