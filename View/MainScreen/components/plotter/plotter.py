from kivymd.uix.boxlayout import MDBoxLayout
from kivy_garden.graph import Graph, LinePlot, PointPlot
import numpy as np
from kivy.properties import ListProperty

def predecir_frag():
    fr = float(7)
    b = float(4)
    s = float(3)
    h = float(11)
    Desv = float(0.02)
    t = float(2.8)
    d = float(100)
    sp = float(0)
    de = float(0.8)
    rws = float(100)

    lc = h+sp - t
    w = de * lc * 3.1416*d**2/2
    V = b*s*h
    Xprom = fr*((V/w)**0.8)*(w**(1/6))*(115/rws)**(19/30)
    n = 2.2-14*(b/d)*(((1+s/b)/2)**0.5)*(1-Desv/b)*(lc/h)
    paso1 = 5
    Xc = Xprom / (0.693**(1/n))

    y = np.arange(5, 95+paso1, paso1)/100
    x = Xc * ((- (np.log(1-y)))**(1/n))
    X80 = Xc * ((- (np.log(0.2)))**(1/n))
    return x, y, X80


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
            xlabel='Tamaño frag.(m)', ylabel='Retención (%)',
            padding=10
            )
        self.add_widget(self.graph)
        self.plot = LinePlot(color=[0, 0, 1, 1], line_width=2)
        self.ver_line = PointPlot(color=[1, 0, 0, 0.8], point_size=2)
        self.hor_line = PointPlot(color=[1, 0, 0, 0.8], point_size=2)
        self.graph.add_plot(self.plot)
        self.graph.add_plot(self.ver_line)
        self.graph.add_plot(self.hor_line)
        
    def update(self, plot_x, plot_y, x_80):
        # self.plot_x, self.plot_y, self.X80 = predecir_frag()
        self.plot.points = [(plot_x[x], plot_y[x]*100)
                            for x in range(self.samples)]
        
        self.ver_line.points = [
            (x_80, x) for x in np.linspace(0, 100, 23)]
        
        self.hor_line.points = [
            (x, 80) for x in np.linspace(0, 0.9, 23)]


