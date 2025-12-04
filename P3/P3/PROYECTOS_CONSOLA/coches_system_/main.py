from tkinter import *
from tkinter import messagebox
from view import vista

class App:
    def __init__(self, ventana):
        view = vista.View(ventana)


if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()
    ventana.title("Sistema de Coches")