from kivymd.uix.screen import MDScreen
import numpy as np
import matplotlib.pyplot as plt
from kivymd.uix.slider import MDSlider
from utils.backend_kivyagg import FigureCanvasKivyAgg


class SecondScreenView(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fig, self.ax = plt.subplots()
        self.fig.subplots_adjust(left=0.2, bottom=0.2)
        self.draw()
        
        self.nivel = MDSlider(min=0, max = 7, orientation= 'horizontal', size_hint= [1, 0.1], value=3)
        self.ids.box.add_widget(self.nivel)
        self.nivel.bind(value = self.valor_slider)
        
    def draw(self):
        plt.xlim(-11, 11)
        plt.ylim(-8, 8)
        plt.grid (alpha=0.2)

        self.ax.set_xlabel("Eje  Horizontal", size=15)
        self.ax.set_ylabel("Eje  Vertical", size = 15)

        canvas = FigureCanvasKivyAgg(self.fig)
        self.ids.plotter.add_widget(canvas)

    def update_plot(self):
        self.ids.plotter.clear_widgets()
        self.draw()
        
    def valor_slider(self, instance, value):
        self.ax.cla()
        x = np.arange(-4*np.pi, value*np.pi, 0.01)
        self.ax.plot(x, value*np.sin(x), color ='lime', marker='o', linestyle='dotted', 
          markersize=1,linewidth=8)
        self.update_plot()
        
    def back_to_menu(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'