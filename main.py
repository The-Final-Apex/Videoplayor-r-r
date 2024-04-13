from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivy.uix.button import Button
from plyer import filechooser

class MainApp(MDApp):
    title = "Video playor-r-r"
    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = "BlueGray"
        
        self.player = VideoPlayer(source="Loading Screen Effect.mp4")
        self.player.state = "play"
        self.player.options = {'eos': 'loop'}
        self.player.allow_stretch = True

        button = MDFloatingActionButton(icon="file", pos_hint={"center_x": 0.5, "center_y": 0.1})
        button.bind(on_release=self.show_file_chooser)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.player)
        layout.add_widget(button)
        
        return layout

    def show_file_chooser(self, instance):
        filechooser.open_file(on_selection=self.select_file)

    def select_file(self, selection):
        if selection:
            selected_file = selection[0]
            self.player.source = selected_file
            self.player.state = "play"

MainApp().run()