from tkinter import *

ventanas = Tk()
ventanas.title("listBox")
ventanas.geometry("500x500")

def mostrarEstado():
    seleccion=lista.get(lista.curselection())
    resultado.config(text=f"Seleccionaste: {seleccion}")

lista = Listbox(ventanas, width=10, height=5, selectmode=SINGLE)
lista.pack()

opciones=["Azul", "Rojo", "Verde", "Amarillo"]
for i in opciones:
    lista.insert(END, i)

boton = Button(ventanas, text="Mostrar selección", command=mostrarEstado)
boton.pack()

resultado = Label(ventanas, text="")
resultado.pack()

ventanas.mainloop()