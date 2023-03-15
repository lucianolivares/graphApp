from kivymd.uix.screen import MDScreen


class SecondScreenView(MDScreen):
    def back_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'