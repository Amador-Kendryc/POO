from tkinter import *

ventanas = Tk()
ventanas.title("Scale")
ventanas.geometry("500x500")

def mostrarEstado():
    resultado.config(text=f"Valor seleccionado por el usuario: {valor.get()} ")

valor=IntVar()
escala=Scale(ventanas, from_= 0, to = 100, orient=HORIZONTAL, variable=valor)
escala.pack()


boton = Button(ventanas, text="Confirmar", command=mostrarEstado)
boton.pack()

resultado = Label(ventanas, text="")
resultado.pack()

ventanas.mainloop()