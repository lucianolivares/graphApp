from kivymd.uix.boxlayout import MDBoxLayout
# from kivy_garden.graph import Graph, LinePlot, PointPlot
import matplotlib.pyplot as plt
import numpy as np
from utils.backend_kivyagg import FigureCanvasKivyAgg


class Plotter(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Plotter, self).__init__(**kwargs)
        self.samples = 19
        self.fig, self.ax = plt.subplots()
        self.draw_plot()


        
    def draw_plot(self):
        self.clear_widgets()
        self.ax.set_title('Predicción Fragmentación', fontsize=15)
        self.ax.set_xlabel('Tamaño frag.(m)', fontsize=10)
        self.ax.set_ylabel('Retención (%)', fontsize=7)
        self.ax.grid(True, color='lightgray')
        self.ax.axhline(y=80, color="r", ls="--")
        canvas = FigureCanvasKivyAgg(figure=self.fig)
        self.add_widget(canvas)
        

    def update(self, plot_x, plot_y, x_80):
        self.ax.cla()
        self.ax.axvline(x=x_80, color="r", ls="--")
        self.ax.plot(plot_x, plot_y*100, label='Valores')
        self.draw_plot()
        # self.clear_widgets()
        # return self.add_widget(FigureCanvasKivyAgg(plt.gcf()))
    #     self.plot.points = [(plot_x[x], plot_y[x]*100)
    #                         for x in range(self.samples)]
    #     self.ver_line.points = [
    #         (x_80, x) for x in np.linspace(0, 100, 23)]
    #     self.hor_line.points = [
    #         (x, 80) for x in np.linspace(0, 0.9, 23)]
