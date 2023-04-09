import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)

k = 8.9875517923*(10**9) #coulomb's constant
Q = 1.60217663*(10**-19) #charge for an electron/proton
e = lambda r:k*Q/r

def manual_log(num):
    new_num = np.log10(abs(num*(10**14)))
    new_num = (new_num if new_num > 0 else 0) # if the exponent is still negative after multiplying by 10^14, its 0 now
    new_num = new_num*num/abs(num)
    return new_num

def clean():
    for widget in window.winfo_children():
        widget.pack_forget()


def log_tick_formatter(val, pos=None):
    if val == 0:
        return "0"
    
    return "{}10^{}V".format(("" if val > 0 else "-"), 
                            int(abs(val)-14))





class space:
    def __init__(self):
        np.zeros((50, 50))
        self.particles = [particle(-1, (-3, 3)), particle(1, (3, 3)), particle(-1, (-3, -3)), particle(1, (3, -3))]

    
    def zline(self, X, Y):
        values = np.zeros((60, 60))
        for p in self.particles:
            vector = (X-p.x, Y-p.y)
            forces = e((vector[0]**2+vector[1]**2)**0.5)*p.charge
            values = np.add(values, forces)
        return values
         
        

class particle:
    def __init__(self, charge, location):
        self.charge = charge
        self.x = location[0]
        self.y = location[1]

def plot():
    clean()
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.zaxis.set_major_formatter(mticker.FuncFormatter(log_tick_formatter))
    ax.zaxis.set_major_locator(mticker.MaxNLocator(integer=True))


    xline = np.linspace(-16, 16, 60)
    yline = np.linspace(-16, 16, 60)
    X, Y = np.meshgrid(xline, yline)

    s = space()
    z = s.zline(X, Y)
    Z = np.array([[manual_log(z[n1][n2]) for n2 in range(len(z[n1]))] for n1 in range(len(z))])

    ax.plot_surface(X, Y, Z, cmap=plt.cm.gray)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()


def main():
    clean()
    plot_btn = tk.Button(master=window, command=plot, text="plot")
    plot_btn.pack()



window = tk.Tk()

start_btn = tk.Button(master=window, command=main, text="Cliquez ici pour commencer")
start_btn.pack()

bibliography_btn = tk.Button(master=window, command=bibliography, text="Voir la bibliographie")
bibliography_btn.pack()



window.mainloop()
