
"""
Script for managing hot reloading of the project.
For more details see the documentation page -

https://kivymd.readthedocs.io/en/latest/api/kivymd/tools/patterns/create_project/

To run the application in hot boot mode, execute the command in the console:
DEBUG=1 python main.py
"""

# import os

# from kivy import Config
# from kivy.core.text import LabelBase

# from PIL import ImageGrab

# # TODO: You may know an easier way to get the size of a computer display.
# resolution = ImageGrab.grab().size

# # Change the values of the application window size as you need.
# Config.set("graphics", "height", '918')
# Config.set("graphics", "width", "510")

# from kivy.core.window import Window

# # Place the application window on the right side of the computer screen.
# Window.top = 75
# Window.left = resolution[0] - Window.width

# from kivymd.tools.hotreload.app import MDApp
# from kivymd.uix.screenmanager import MDScreenManager

# from View.screens import screens

# class GraphApp(MDApp):
#     KV_DIRS = [os.path.join(os.getcwd(), "View")]

#     def build_app(self) -> MDScreenManager:
#         """
#         In this method, you don't need to change anything other than the
#         application theme.
#         """
#         self.manager_screens = MDScreenManager()
#         Window.bind(on_key_down=self.on_keyboard_down)
#         for name_screen in screens:
#             exec(f"import View.{screens[name_screen]}")
#             view = eval(
#                 f'View.{screens[name_screen]}.{screens[name_screen].split(".")[0]}View()'
#             )
#             view.name = name_screen
#             self.manager_screens.add_widget(view)
            
#         self.manager_screens.current = "main"
        
#         return self.manager_screens

#     def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
#         """
#         The method handles keyboard events.

#         By default, a forced restart of an application is tied to the
#         `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
#         """

#         if "meta" in modifiers or "ctrl" in modifiers and text == "r":
#             self.rebuild()


# LabelBase.register(name='Poppins',
#                    fn_regular='assets/fonts/Poppins-Medium.ttf')

# GraphApp().run()

# After you finish the project, remove the above code and uncomment the below
# code to test the application normally without hot reloading.

"""
The entry point to the application.

The application uses the MVC template. Adhering to the principles of clean
architecture means ensuring that your application is easy to test, maintain,
and modernize.

You can read more about this template at the links below:

https://github.com/HeaTTheatR/LoginAppMVC
https://en.wikipedia.org/wiki/Model–view–controller
"""

from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.core.text import LabelBase

from View.screens import screens


class GraphApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
        # This is the screen manager that will contain all the screens of your
        # application.
        self.manager_screens = MDScreenManager()

    def build(self) -> MDScreenManager:
        self.generate_application_screens()
        return self.manager_screens

    def generate_application_screens(self) -> None:
        """
        Creating and adding screens to the screen manager.
        You should not change this cycle unnecessarily. He is self-sufficient.

        If you need to add any screen, open the `View.screens.py` module and
        see how new screens are added according to the given application
        architecture.
        """
        
        for name_screen in screens:
            exec(f"import View.{screens[name_screen]}")
            view = eval(
                f'View.{screens[name_screen]}.{screens[name_screen].split(".")[0]}View()'
            )
            view.name = name_screen
            self.manager_screens.add_widget(view)
            
        self.manager_screens.current = "main"

LabelBase.register(name='Poppins',
                   fn_regular='assets/fonts/Poppins-Medium.ttf')


GraphApp().run()
