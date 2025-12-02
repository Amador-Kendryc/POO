from tkinter import *
from tkinter import messagebox
from controller import funciones
from model import operaciones

class Vista:
 
    def __init__(self, ventana):
        ventana.title("Calculadora Básica")
        ventana.geometry("800x600")
        ventana.resizable(False, False)
        self.interfaz(ventana)

    def interfaz(self, ventana):
        
        n1 = IntVar()
        n2 = IntVar()
        txt_numero1 = Entry(ventana, textvariable=n1, width=5, justify="right")
        txt_numero1.pack(side="top", anchor="center")

        txt_numero2 = Entry(ventana, textvariable=n2, width=5, justify="right")
        txt_numero2.pack(side="top", anchor="center")

        btn_suma = Button(ventana, text="+",
                        command=lambda: funciones.controladores.operaciones("Suma", n1.get(), n2.get(), "+"))
        btn_suma.pack()

        btn_resta = Button(ventana, text="-", 
                          command=lambda: funciones.controladores.operaciones("Resta", n1.get(), n2.get(), "-"))
        btn_resta.pack()

        btn_multiplicacion = Button(ventana, text="x", 
                                   command=lambda: funciones.controladores.operaciones("Multiplicación", n1.get(), n2.get(), "x"))
        btn_multiplicacion.pack()

        btn_division = Button(ventana, text="/", 
                             command=lambda: funciones.controladores.operaciones("División", n1.get(), n2.get(), "/"))
        btn_division.pack()

        btn_salir = Button(ventana, text="Salir", command=ventana.quit)
        btn_salir.pack()
        
        self.menuPrincipal(ventana)

        ventana.mainloop()

    def menuPrincipal(self, ventana):
        menuBar = Menu(ventana)
        ventana.config(menu=menuBar)

        operacionesMenu = Menu(menuBar, tearoff=0)
        menuBar.add_cascade(label="Operaciones", menu=operacionesMenu)
        operacionesMenu.add_command(label="agregar", command=lambda:"")
       
        operacionesMenu.add_command(label="consultar", command=lambda:"")
        operacionesMenu.add_command(label="cambiar", command=lambda:"")
        operacionesMenu.add_command(label="borrar", command=lambda:"")

        operacionesMenu.add_separator()
        operacionesMenu.add_command(label="salir", command=ventana.quit)
        ventana.mainloop()

    

def eliminarOperacion(self, ventana):
    messagebox.showinfo("Eliminar Operación", "Aquí se eliminará una operación de la base de datos.")
    messagebox.showinfo("ID de la operacion.")
    txt_id = Entry(ventana, width=5, justify="right")
    txt_id.pack(side="top", anchor="center")
    btn_eliminar = Button(ventana, text="Eliminar", command=lambda: "")
    btn_eliminar.pack()
    btn_volver = Button(ventana, text="Volver", command=lambda: self.menuPrincipal(ventana))
    btn_volver.pack()
    ventana.mainloop()


def consultarOperaciones(self, ventana):
    self.borrarVentana(ventana)
    self.menuPrincipal(ventana)
    Label


def cambiarOperacion(self, ventana):
    messagebox.showinfo("Cambiar Operación", "Aquí se cambiará una operación de la base de datos.")
    messagebox.showinfo("ID de la operacion.")
    txt_id = Entry(ventana, width=5, justify="right")
    txt_id.pack(side="top", anchor="center")
    btn_cambiar = Button(ventana, text="Cambiar", command=lambda: "")
    btn_cambiar.pack()
    Label(ventana, text ="Nuevo signo de la operacion:").pack()
    txt_signo = Entry(ventana, width=5, justify="right")
    txt_signo.pack(side="top", anchor="center")
    Label(ventana, text ="Nuevo numero 1:").pack()
    txt_num1 = Entry(ventana, width=5, justify="right")
    txt_num1.pack(side="top", anchor="center")
    Label(ventana, text ="Nuevo numero 2:").pack()
    txt_num2 = Entry(ventana, width=5, justify="right")
    txt_num2.pack(side="top", anchor="center")
    Label(ventana, text ="Nuevo resultado:").pack()
    txt_resultado = Entry(ventana, width=5, justify="right")
    txt_resultado.pack(side="top", anchor="center")
    btn_cambiar = Button(ventana, text="Cambiar", command=lambda: "")
    btn_cambiar.pack()
    btn_volver = Button(ventana, text="Volver", command=lambda: self.menuPrincipal(ventana))
    btn_volver.pack()
    ventana.mainloop()
