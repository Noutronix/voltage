import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import sys

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
    title(num)

    plt.ticklabel_format()

    c = coords(num)
    ax.plot_surface(c[0]*10**10, c[1]*10**10, c[2], cmap=plt.cm.gray)
    return ax

def title(num):
    if num == 0:
        plt.title("Deux plaques chargées (rapprochées)")
    if num == 1:
        plt.title("Deux plaques chargées (separées)")
    if num == 2:
        plt.title("Deux protons")
    if num == 3:
        plt.title("Deux électrons")
    if num == 4:
        plt.title("Un électron et un proton")


def plot(num, frame):
    fig = plt.figure(figsize=(4, 4))
    ax = setup_ax(num)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

    
    frame.pack(side=tk.RIGHT)


    

def main():
    clean()
    frame1 = tk.Frame(master=window)
    frame2 = tk.Frame(master=window)

    plot(0, tk.Frame(master=frame1))
    plot(1, tk.Frame(master=frame1))
    plot(2, tk.Frame(master=frame1))
    plot(3, tk.Frame(master=frame2))
    plot(4, tk.Frame(master=frame2))

    ext_btn = tk.Button(width=100, master=window, command=sys.exit, text="Arreter", bg="red", font=('Times', 24))
    

    frame1.pack()
    frame2.pack()
    ext_btn.pack(side=tk.BOTTOM)



def coords(num):
    xline = np.linspace(-16*10**-11, 16*10**-11, 60)
    yline = np.linspace(-16*10**-11, 16*10**-11, 60)
    X, Y = np.meshgrid(xline, yline)
    s = space(num)
    Z = s.zline(X, Y)
    
    return (X, Y, Z)






window = tk.Tk()
window.attributes("-fullscreen", True)

main()

#bibliography_btn = tk.Button(master=window, command=bibliography, text="Voir la bibliographie")
#bibliography_btn.pack()



window.mainloop()
