#Encapsular es un pilar de la POO que permite indicar cual es la manera de como utilizar los metodos y atributos y
#una clase a la hora de usar objetos o en herencia

import os
os.system("cls")

class Clase:
    atributo_publico = "Soy un atributo publico"
    _atributo_protegido = "Soy un atributo protegido"
    __atributo_privado = "Soy un atributo privado"

    def __init__(self,color,tamanio):
        self.__color=color
        self.__tamanio=tamanio


    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    @property
    def atributopublico(self):
        return self.atributo_publico
    
    def atributopublico(self, atributo_publico):
        self.atributopublico = atributo_publico

    @property
    def atributo_protegido(self):
        return self._atributo_protegido
    
    def atributo_protegido(self, atributo_protegido):
        self._atributo_protegido = atributo_protegido

    def getAtributoPrivado(self):
        return self.__atributo_privado
    
    def setAtributoPrivado(self, atributo_privado):
        self.__atributo_privado = atributo_privado




    #utilizar la clase

objeto = Clase("Rojo", "Grande")
print(objeto.tamanio)
print(objeto.atributo_publico)
print(objeto._atributo_protegido)
print(objeto.getAtributoPrivado())
objeto.color = "Azul"
print(objeto.color)