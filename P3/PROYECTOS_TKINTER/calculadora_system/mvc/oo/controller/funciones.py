from tkinter import messagebox
from model import operaciones



class controladores:
   @staticmethod
   def operaciones(titulo,numero1,numero2,signo):
    if signo=="+":
        resultado=numero1+numero2
    elif signo=="-":
        resultado=numero1-numero2
    elif signo=="x":
        resultado=numero1*numero2
    elif signo=="/":
        resultado=numero1/numero2
    resu=messagebox.askquestion(titulo,f"{numero1}{signo}{numero2}={resultado}\n¿Quieres guardar la operación en la base de datos?",icon="question")
    if resu=="yes":
        respuesta=operaciones.operaciones.insertar(numero1,numero2,signo,resultado)
        controladores.respuesta_sql("agregar registro",respuesta)

    @staticmethod
    def eliminar(id)
        respuesta=operaciones.operaciones.eliminar(id)
        controladores.respuesta_sql("eliminar registro",respuesta)

    @staticmethod
    def cambiar(id,numero1,numero2,signo,resultado):
        respuesta=operaciones.operaciones.cambiar(numero1,numero2,signo,resultado)
        controladores.respuesta_sql("actualizar registro",respuesta)

    @staticmethod
    def consultar(usuario_id):
        registros=operaciones.operaciones.consultar(usuario_id)
        return registros

    @staticmethod
    def respuesta_sql(titulo,respuesta):
     if respuesta:
        messagebox.showinfo(icon="info",title="titulo",message=f"\n\t... ¡ La acción de {titulo} se ha realizado con éxito ! ...")
     else:
        messagebox.showerror(icon="error",title="titulo",message=f"\n\t... ¡ Error en la acción de {titulo} ! ...")




