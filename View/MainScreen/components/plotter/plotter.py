from kivymd.uix.boxlayout import MDBoxLayout
import matplotlib.pyplot as plt
from utils.backend_kivyagg import FigureCanvasKivyAgg


class Plotter(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Plotter, self).__init__(**kwargs)
        self.samples = 19
        self.fig, self.ax = plt.subplots()
        self.draw_plot()

    def draw_plot(self):
        self.clear_widgets()
        self.ax.set_title('Predicción Fragmentación')
        self.ax.set_xlabel('Tamaño frag.(m)')
        self.ax.set_ylabel('Retención (%)')
        self.ax.grid(True, color='lightgray')
        self.ax.axhline(y=80, color="r", ls="--")
        canvas = FigureCanvasKivyAgg(figure=self.fig)
        self.add_widget(canvas)
        
    def update(self, plot_x, plot_y, x_80):
        self.ax.cla()
        self.ax.axvline(x=x_80, color="r", ls="--")
        self.ax.plot(plot_x, plot_y*100, label='Valores')
        self.draw_plot()

