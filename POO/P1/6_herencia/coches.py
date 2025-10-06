import os
os.system("cls")






class Coche:
    def __init__(self):
        self._marca=""
        self._color=""
        self._modelo=""
        self._velocidad=0
        self._caballaje=0
        self._plazas=0

    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,marca):
        self._marca=marca

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,color):
        self._color=color

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo

    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad

    @property
    def caballaje(self):
        return self._caballaje
    
    @caballaje.setter
    def caballaje(self,caballaje):
        self._caballaje=caballaje

    @property
    def plazas(self):
        return self._plazas
    
    @plazas.setter
    def plazas(self,plazas):   
        self._plazas=plazas

    







#Metodos-o•acciones•o-funciones•que-hace-el-objeto•




   
    def acelerar(self):   
     return"El coche esta acelerando"

    def frenar(self):
     return"El coche esta frenando"
    

    
class Camiones(Coche):
    def __init__(self,marca,modelo,color,velocidad,caballaje,plazas,carga,eje,capacidadCarga):
        super().__init__(marca,modelo,color,velocidad,caballaje,plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    @property
    def eje(self):
        return self.__eje
    
    @eje.setter
    def eje(self,eje):
        self.__eje=eje

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    
    @capacidadCarga.setter
    def capacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.__tipo_carga
    
    
class Camionetas(Coche):
    def __init__(self,marca,modelo,color,velocidad,caballaje,plazas,traccion,capacidadCarga):
        super().__init__(marca,modelo,color,velocidad,caballaje,plazas)
        self.__traccion=traccion
        self.__capacidadCarga=capacidadCarga

    @property
    def traccion(self):
        return self.__traccion
    
    @traccion.setter
    def traccion(self,traccion):
        self.__traccion=traccion

    @property
    def cerrada(self):
        return self.__cerrada
    
    @cerrada.setter
    def cerrada(self,cerrada):
        self.__cerrada=cerrada

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    
    @capacidadCarga.setter
    def capacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

    def transportar(self,num_pasajeros):
        self.num_pasajeros=num_pasajeros
        return self.__num_pasajeros
        