from kivymd.uix.screen import MDScreen
import numpy as np

class MainScreenView(MDScreen):
    def gnrt_graph(self):
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
        
        # fr = float (self.ids.fr.text) 
        # b = float (self.ids.b.text)
        # s = float (self.ids.s.text)
        # h = float (self.ids.h.text)
        # Desv = float (self.ids.Desv.text)
        # t = float (self.ids.t.text)
        # d = float (self.ids.d.text)
        # sp = float (self.ids.sp.text)
        # de = float (self.ids.de.text)
        # rws = float (self.ids.rws.text)

        lc = h+sp- t
        w = de * lc *3.1416*d**2/2
        V= b*s*h
            
        Xprom = fr*((V/w)**0.8)*(w**(1/6))*(115/rws)**(19/30)
        
        n = 2.2-14*(b/d)*(((1+s/b)/2)**0.5)*(1-Desv/b)*(lc/h)
        
        paso1 =5
        p=np.arange(5,95+paso1,paso1)/100 
        
        Xc = Xprom / (0.693**(1/n))
        
        X = Xc * ((- (np.log(1-p)))**(1/n))
                    
        X80 = Xc * ((- (np.log(0.2)))**(1/n))      
        
        # plt.close()
        # plt.xlabel('Tamaño frag.(m)', fontsize=10)
        # plt.ylabel('Retención (%)', fontsize = 7)
        # plt.grid(True, color='lightgray')

        # #plt.subplot(2,2,3)
        # plt.axhline(y=80, color="r", ls ="--") 
        # plt.axvline(x=X80, color = "r", ls="--")
        # plt.text (0.10,50,'Gráfica', color="r", fontsize=10)
        # plt.title ('Predicción Fragmentación', fontsize=15,color='blue')
        # plt.plot(X,p*100, label = 'Valores')
        # plt.savefig('plot.png')

        self.bx = self.ids.bx
        # self.bx.clear_widgets()
        # return self.bx.add_widget(FigureCanvasKivyAgg(plt.gcf()))
