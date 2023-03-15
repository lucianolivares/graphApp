from kivymd.uix.screen import MDScreen
from View.MenuScreen.components import MenuCard


class MenuScreenView(MDScreen):
    def on_enter(self, *args) -> None:
        if not self.ids.menu_list.data:
            menu_list = [
                "Main",
                "Second",
            ]
            menu_list.sort()
            for name_card in menu_list:
                self.ids.menu_list.data.append(
                    {
                        "viewclass": "MenuCard",
                        "title": name_card,
                        "elevation": 1,
                        "shadow_softness": 4,
                        "on_release": lambda x=name_card.lower(): self.switch_screen(
                            x
                        )
                    }
                )

    def switch_screen(self, screen_name):
        self.manager.transition.direction = 'left'
        self.manager.current = screen_name
