from tkinter import *

windows = Tk()
windows.title("Check Button")
windows.geometry("500x500")

def mostrarEstado():
    resultado.config(text="Opción seleccionada: " + opcion.get())

opcion = StringVar()
radioBoton=Radiobutton(windows, text="Opción 1", variable=opcion, value="Opción 1")
radioBoton.pack()

radioBoton2=Radiobutton(windows, text="Opción 2", variable=opcion, value="Opción 2")
radioBoton2.pack()

radioBoton3=Radiobutton(windows, text="Opción 3", variable=opcion, value="Opción 3")
radioBoton3.pack()

boton = Button(windows, text="Mostrar Opcion", command=mostrarEstado)
boton.pack()

resultado = Label(windows, text="")
resultado.pack()

windows.mainloop()