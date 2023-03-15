from kivymd.uix.screen import MDScreen
from View.MainScreen.components import Formulario, Plotter # NOQA

class MainScreenView(MDScreen):
    def back_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

        
