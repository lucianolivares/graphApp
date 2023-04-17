from kivymd.uix.screen import MDScreen
from View.MenuScreen.components import MenuCard
import os

class MenuScreenView(MDScreen):
    def on_enter(self, *args) -> None:
        if not self.ids.menu_list.data:
            screens_data = dict(
                main = dict(
                    label = "Predicción de Fragmentación",
                    source = "assets/fragmentación.png"
                ),
                second = dict(
                    label = "Gráfico de Frecuencias",
                    source = "assets/frecuencía.jpg"
                ),
                video = dict(
                    label = "Reproductor de Video",
                    source = "frecuencía.jpg"
                ),
            )
            dict(sorted(screens_data.items()))
            for name, props in screens_data.items():
                self.ids.menu_list.data.append(
                    {
                        "viewclass": "MenuCard",
                        "title": props['label'],
                        "image": props['source'],
                        "elevation": 1,
                        "shadow_softness": 4,
                        "on_release": lambda x=name.lower(): self.switch_screen(
                            x
                        )
                    }
                )

    def switch_screen(self, screen_name):
        self.manager.transition.direction = 'left'
        self.manager.current = screen_name
