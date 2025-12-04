from tkinter import *

def opcionEstado(tipo):
    resultado.config(text=f"{tipo}")

ventanas = Tk()
ventanas.title("Menu")
ventanas.geometry("500x500")


menubar = Menu(ventanas)
ventanas.config(menu=menubar)
archivoMenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Archivo", command=lambda:opcionEstado("Nuevo Archivo"))
archivoMenu.add_command(label="Guardar Archivo", command=lambda:opcionEstado("Guardar Archivo"))
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=ventanas.quit)

edicionMenu = Menu(menubar, tearoff=False)
menubar.add_cascade(label="Edición", menu=edicionMenu)
edicionMenu.add_command(label="Copiar", command=lambda:opcionEstado("Copiar"))
edicionMenu.add_command(label="Recortar", command=lambda:opcionEstado("Recortar"))
edicionMenu.add_separator()
edicionMenu.add_command(label="Salir", command=ventanas.quit)


resultado = Label(ventanas, text="")
resultado.pack()

ventanas.mainloop()