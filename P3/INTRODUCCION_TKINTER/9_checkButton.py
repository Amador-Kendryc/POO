from tkinter import *

windows = Tk()
windows.title("Check Button")
windows.geometry("500x500")

def mostrarEstado():
    if opcion.get() == 1:
        resultado.config(text=f"Notificaciones Activadas")
    else:
        resultado.config(text=f"Notificaciones Desactivadas")

opcion = IntVar()
checkBoton = Checkbutton(windows, text="Desea Recibir Notificaciones",
variable=opcion, onvalue=1, offvalue=0)
checkBoton.pack()

boton = Button(windows, text="Confirmar", command=mostrarEstado)
boton.pack()

resultado = Label(windows, text="")
resultado.pack()

windows.mainloop()