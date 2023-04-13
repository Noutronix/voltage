import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import tkinter as tk
import tkinter.ttk as ttk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import functools as ft

def z_tick_formatter(val, pos=None):
    return "{}V".format(val)

def standardize(item):
    if item > 100:
        return 100
    if item < -100:
        return -100
    return item

k = 8.9875517923*(10**9) #coulomb's constant
Q = 1.60217663*(10**-19) #charge for an electron/proton
e = lambda r:k*Q/r


def clean():
    for widget in window.winfo_children():
        widget.pack_forget()


class space:
    def __init__(self, num):
        np.zeros((50, 50))
        if num == 0:
            self.particles = [particle(-1, (-3, 9)), particle(-1, (-3, 3)), particle(1, (3, 9)), particle(1, (3, 3)), particle(-1, (-3, -3)), particle(1, (3, -3)), particle(1, (3, -9)), particle(-1, (-3, -9))]
        if num == 1:
            self.particles = [particle(-1, (-6, 9)), particle(-1, (-6, 3)), particle(1, (6, 9)), particle(1, (6, 3)), particle(-1, (-6, -3)), particle(1, (6, -3)), particle(1, (6, -9)), particle(-1, (-6, -9))]
        if num == 2:
            self.particles = [particle(1, (0, 3)), particle(1, (0, -3))]
        if num == 3:
            self.particles = [particle(-1, (0, 3)), particle(-1, (-0, -3))]
        if num == 4:
            self.particles = [particle(1, (0, 3)), particle(-1, (-0, -3))]

        for p in self.particles:
            p.x *= 1.5*10**-11
            p.y *= 1.5*10**-11

        


    def zline(self, X, Y):
        values = np.zeros((60, 60))
        for p in self.particles:
            vector = (X-p.x, Y-p.y)
            forces = e((vector[0]**2+vector[1]**2)**0.5)*p.charge
            forces = np.array([[standardize(forces[n1][n2]) for n2 in range(len(forces[n1]))] for n1 in range(len(forces))])
            values = np.add(values, forces)
        return values
         
        

class particle:
    def __init__(self, charge, location):
        self.charge = charge
        self.x = location[0]
        self.y = location[1]

def setup_ax(num):
    ax = plt.axes(projection='3d')
    ax.view_init(elev=25, azim=-137)
    ax.zaxis.set_major_formatter(mticker.FuncFormatter(z_tick_formatter))
    
    plt.xlabel("Axe des X (en 10^-10 m)")
    plt.ylabel("Axe des Y (en 10^-10 m)")

    plt.ticklabel_format()

    c = coords(num)
    ax.plot_surface(c[0]*10**10, c[1]*10**10, c[2], cmap=plt.cm.gray)
    return ax

def plot(num):
    clean()
    fig = plt.figure()
    ax = setup_ax(num)

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()
    

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    canvas.get_tk_widget().pack()

    return_btn = tk.Button(master=window, command=main, text="Retourner")
    return_btn.pack()

def main():
    clean()
    plot1_btn = tk.Button(master=window, command=ft.partial(plot, 0), text="Plusieurs charges rapproches")
    plot1_btn.pack()

    plot2_btn = tk.Button(master=window, command=ft.partial(plot, 1), text="Plusieurs charges eloignes")
    plot2_btn.pack()

    plot3_btn = tk.Button(master=window, command=ft.partial(plot, 2), text="Deux protons")
    plot3_btn.pack()

    plot4_btn = tk.Button(master=window, command=ft.partial(plot, 3), text="Deux electrons")
    plot4_btn.pack()

    plot5_btn = tk.Button(master=window, command=ft.partial(plot, 4), text="Deux charges opposes")
    plot5_btn.pack()



def coords(num):
    xline = np.linspace(-16*10**-11, 16*10**-11, 60)
    yline = np.linspace(-16*10**-11, 16*10**-11, 60)
    X, Y = np.meshgrid(xline, yline)
    s = space(num)
    Z = s.zline(X, Y)
    
    return (X, Y, Z)






window = tk.Tk()

start_btn = tk.Button(master=window, command=main, text="Cliquez ici pour commencer")
start_btn.pack()

#bibliography_btn = tk.Button(master=window, command=bibliography, text="Voir la bibliographie")
#bibliography_btn.pack()



window.mainloop()
