from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.graph import Graph, LinePlot, PointPlot
import numpy as np


class Plotter(MDBoxLayout):
    def __init__(self, **kwargs):
        super(Plotter, self).__init__(**kwargs)
        self.samples = 19
        self.graph = Graph(
            xmin=0.0, xmax=0.6, ymin=0, ymax=100,
            border_color=[0, 0, 0, 1],
            tick_color=[0, 0, 0, 0.2],
            x_grid_label=True, y_grid_label=True,
            x_grid=True, y_grid=True,
            x_ticks_major=0.1, y_ticks_major=16.6,
            xlabel='Tamaño', ylabel='Retención',
        )
        self.add_widget(self.graph)
        self.plot = LinePlot(color=[0, 0, 1, 1], line_width=2)
        self.ver_line = PointPlot(color=[1, 0, 0, 0.8], point_size=2)
        self.hor_line = PointPlot(color=[1, 0, 0, 0.8], point_size=2)
        self.graph.add_plot(self.plot)
        self.graph.add_plot(self.ver_line)
        self.graph.add_plot(self.hor_line)

    def update(self, plot_x, plot_y, x_80):
        self.plot.points = [(plot_x[x], plot_y[x]*100)
                            for x in range(self.samples)]
        self.ver_line.points = [
            (x_80, x) for x in np.linspace(0, 100, 23)]
        self.hor_line.points = [
            (x, 80) for x in np.linspace(0, 0.9, 23)]
