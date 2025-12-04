"tkinter trabaja a traves de interfaces, es una biblioteca de python que permite craear aplicaciones en python para escritorio"

from tkinter import *
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera app con tkinter") #titulo de la ventana
ventana.geometry("800x500") #tamaño de la ventana

ventana.mainloop() #metodo para que la ventana se mantenga abierta todo el tiempo