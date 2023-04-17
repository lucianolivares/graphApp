from kivymd.uix.screen import MDScreen
from kivy.uix.videoplayer import VideoPlayer

class VideoScreenView(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.video = None
        
    def cargar_video(self):
        if self.video: self.ids.grid_layout.remove_widget(self.video) 
        self.video = VideoPlayer(source="assets/test.mpg", size_hint_y=None, height=400)
        self.ids.grid_layout.add_widget(self.video)
        
    def back_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'
        

        
