from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        
        
# add widgets to window


# Image Widget
        self.window.add_widget(Image(source="server-room.jpg"))

        # Label Widget
        self.greeting = Label(
                        text="What is your Name?",
                        font_size = 18,
                        color="#77ee88"
                        )
        self.window.add_widget(self.greeting)
        # Text Input Widget
        self.user = TextInput(
                    multiline=False,
                    padding_y = (20, 20),
                    size_hint = (1, 0.5)
                    )
        self.window.add_widget(self.user)
        # Button Widget
        self.button = Button(
                        text="Greetings!",
                        font_size = 18,
                        size_hint = (1, 0.5),
                        bold = True,
                        pos_hint = {"center_x": 0.5, "center_y": 0.5},
                        background_color="#77ee88"
                        )
        
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self, event):
        self.greeting.text = f"Hello {self.user.text} !"



if __name__ == "__main__":
    SayHello().run()
