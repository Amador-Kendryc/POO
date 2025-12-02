#Crear una calculadora: 1. Dos campos de texto 2. 4 botones para la operaciones 3. Mostrar el resultado en una alerta 
# 4. programacion estrucuturada 5. importar el MVC

from view import interfaz
from tkinter import *
from conexionBD import *

class App:
    def __init__(self, ventana):
        view = interfaz.Vista(ventana)



if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()