from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle


class ConverterApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.1, 0.1, 1)  # dark background
        self.title = "Number Converter"

        root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # 1. Title (Blue background)
        title_layout = BoxLayout(size_hint=(1, None), height=50)
        with title_layout.canvas.before:
            Color(0, 0, 1, 1)  # Blue
            self.bg1 = Rectangle(size=title_layout.size, pos=title_layout.pos)
        title_layout.bind(size=self._update_bg1, pos=self._update_bg1)

        title_label = Label(text="Number Converter", font_size=24, color=(1, 1, 1, 1))
        title_layout.add_widget(title_label)
        root.add_widget(title_layout)

        # 2. Input field (White background)
        input_layout = BoxLayout(size_hint=(1, None), height=50)
        with input_layout.canvas.before:
            Color(1, 1, 1, 1)  # White
            self.bg2 = Rectangle(size=input_layout.size, pos=input_layout.pos)
        input_layout.bind(size=self._update_bg2, pos=self._update_bg2)

        self.number_input = TextInput(
            hint_text="Enter number",
            multiline=False,
            background_color=(1, 1, 1, 0),  # transparent (use layout bg)
            foreground_color=(0, 0, 0, 1),
            cursor_color=(0, 0, 0, 1),
            hint_text_color=(0.4, 0.4, 0.4, 1),
        )
        input_layout.add_widget(self.number_input)
        root.add_widget(input_layout)

        # 3. Dropdown row (Green background)
        dropdown_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, None), height=50)
        with dropdown_layout.canvas.before:
            Color(0, 1, 0, 1)  # Green
            self.bg3 = Rectangle(size=dropdown_layout.size, pos=dropdown_layout.pos)
        dropdown_layout.bind(size=self._update_bg3, pos=self._update_bg3)

        self.from_system = Spinner(text="Decimal", values=("Binary", "Octal", "Decimal", "Hexadecimal"))
        self.to_system = Spinner(text="Binary", values=("Binary", "Octal", "Decimal", "Hexadecimal"))
        dropdown_layout.add_widget(self.from_system)
        dropdown_layout.add_widget(self.to_system)
        root.add_widget(dropdown_layout)

        # 4. Buttons row (Purple background)
        btn_layout = BoxLayout(orientation="horizontal", spacing=10, size_hint=(1, None), height=50)
        with btn_layout.canvas.before:
            Color(0.5, 0, 0.5, 1)  # Purple
            self.bg4 = Rectangle(size=btn_layout.size, pos=btn_layout.pos)
        btn_layout.bind(size=self._update_bg4, pos=self._update_bg4)

        convert_btn = Button(text="Convert", background_color=(0.7, 1, 0.7, 1), color=(0, 0, 0, 1))
        convert_btn.bind(on_press=self.convert)
        clear_btn = Button(text="Clear", background_color=(1, 0.6, 0.6, 1), color=(0, 0, 0, 1))
        clear_btn.bind(on_press=self.clear_input)

        btn_layout.add_widget(convert_btn)
        btn_layout.add_widget(clear_btn)
        root.add_widget(btn_layout)

        # 5. Output box (Faded black, full size again)
        output_layout = BoxLayout(size_hint=(1, 1))  # fills remaining space
        with output_layout.canvas.before:
            Color(0.15, 0.15, 0.15, 1)  # Faded black
            self.bg5 = Rectangle(size=output_layout.size, pos=output_layout.pos)
        output_layout.bind(size=self._update_bg5, pos=self._update_bg5)

        self.output_box = TextInput(
            text="Result will appear here.",
            readonly=True,
            background_color=(0.15, 0.15, 0.15, 1),  # faded black
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0, 0, 0, 0),  # hide cursor
            font_size=16,
        )
        output_layout.add_widget(self.output_box)
        root.add_widget(output_layout)

        return root

    # Update background rectangles
    def _update_bg1(self, instance, value): self.bg1.size, self.bg1.pos = instance.size, instance.pos
    def _update_bg2(self, instance, value): self.bg2.size, self.bg2.pos = instance.size, instance.pos
    def _update_bg3(self, instance, value): self.bg3.size, self.bg3.pos = instance.size, instance.pos
    def _update_bg4(self, instance, value): self.bg4.size, self.bg4.pos = instance.size, instance.pos
    def _update_bg5(self, instance, value): self.bg5.size, self.bg5.pos = instance.size, instance.pos

    def convert(self, instance):
        try:
            value = self.number_input.text.strip()
            from_sys, to_sys = self.from_system.text, self.to_system.text

            if not value:
                self.output_box.text = "Please enter a number."
                return

            base_map = {"Decimal": 10, "Binary": 2, "Octal": 8, "Hexadecimal": 16}
            decimal_val = int(value, base_map[from_sys])

            if to_sys == "Decimal": converted = str(decimal_val)
            elif to_sys == "Binary": converted = bin(decimal_val)[2:]
            elif to_sys == "Hexadecimal": converted = hex(decimal_val)[2:].upper()
            elif to_sys == "Octal": converted = oct(decimal_val)[2:]
            else:
                self.output_box.text = "Invalid target system"
                return

            self.output_box.text = f"{value} ({from_sys}) = {converted} ({to_sys})"

        except Exception as ex:
            self.output_box.text = f"Error: {str(ex)}"

    def clear_input(self, instance):
        self.number_input.text = ""
        self.output_box.text = "Result will appear here."


if __name__ == "__main__":
    ConverterApp().run()
