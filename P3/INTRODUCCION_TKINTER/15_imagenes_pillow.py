import os
from tkinter import *
from PIL import Image, ImageTk


ventana = Tk()
ventana.title("Ejemplo con PIL")
ventana.geometry("700x700")

# Obtener la ruta absoluta del directorio donde está este archivo .py
ruta_base = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta completa al archivo de imagen
ruta_imagen = os.path.join(ruta_base, "logo_utd.png")


# Abrir imagen con PIL
#img = Image.open("/Users/dagfiscal/python/programacion_oo_2025/P2_TKINTER_POO/DFG/INTRODUCCION_TKINTER/logo_utd.png")
img = Image.open(ruta_imagen)
img = img.resize((100, 100))  # Redimensionar (opcional)
imagen_tk = ImageTk.PhotoImage(img)

# Colocar imagen dentro de una etiqueta y boton
etiqueta = Label(ventana, image=imagen_tk).pack()
boton=Button(ventana, image=imagen_tk,).pack()

ventana.mainloop()