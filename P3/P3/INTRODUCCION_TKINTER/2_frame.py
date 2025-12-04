from tkinter import *
ventana = Tk()
ventana.geometry("800x500")
ventana.title("Marcos o Frames en Tkinter")
marco1=Frame(ventana,width=400,height=200,bg="red", relief=SOLID).pack()# crear un frame dentro de la ventana
marco1.pack_propagate(False)# evitar que el frame se ajuste al tamaño de sus componentes
marco2=Frame(marco1,width=300,height=150,bg="silver", relief=GROOVE).pack()


ventana=mainloop()