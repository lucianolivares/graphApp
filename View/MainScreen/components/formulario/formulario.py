from kivymd.uix.boxlayout import MDBoxLayout
import numpy as np
from kivymd.app import MDApp


class Formulario(MDBoxLayout):
    def gnrt_graph(self):
        fr = float(self.ids.fr.text)
        b = float(self.ids.b.text)
        s = float(self.ids.s.text)
        h = float(self.ids.h.text)
        Desv = float(self.ids.Desv.text)
        t = float(self.ids.t.text)
        d = float(self.ids.d.text)
        sp = float(self.ids.sp.text)
        de = float(self.ids.de.text)
        rws = float(self.ids.rws.text)

        lc = h+sp - t
        w = de * lc * 3.1416*d**2/2
        V = b*s*h
        Xprom = fr*((V/w)**0.8)*(w**(1/6))*(115/rws)**(19/30)
        n = 2.2-14*(b/d)*(((1+s/b)/2)**0.5)*(1-Desv/b)*(lc/h)
        paso1 = 5
        p = np.arange(5, 95+paso1, paso1)/100

        Xc = Xprom / (0.693**(1/n))

        X = Xc * ((- (np.log(1-p)))**(1/n))
        X80 = Xc * ((- (np.log(0.2)))**(1/n))

        main_screen = MDApp.get_running_app().manager_screens.get_screen('main')
        plotter = main_screen.ids.plotter

        plotter.update(X, p, X80)
