"Modelar y diagramar en la POO"

import os
os.system("cls")

#clase de coches
class coches:
    #metodo constructor que inicializa los valores cuadno se instancia de la clase
    def __init__(self, color, marca, velocidad): 
        self.color = color  # atributos del objeto
        self.marca = marca
        self.__velocidad = velocidad
    
    #metodos del objeto
    def acelerar(self, incremento):   
        self.__velocidad=self.__velocidad+incremento
        return self.__velocidad
        
    def frenar(self, decremento):
        self.__velocidad=self.__velocidad-decremento
        return self.__velocidad
    

    def tocar_claxon(self):
        return "piiiii"
    
    
#instancair o crear objeto de la clase coches
coche1 = coches("Blanco","Toyota",220)
coche2 = coches("Amarillo","Nissan",180)

print(f"El coche 1 es de marca {coche1.marca}, color {coche1.color} y su velocidad es {coche1.velocidad} km/h")
coche1.acelerar(50)
print(f"El coche 1 acelero de {coche1.velocidad} a {coche1.acelerar(50)}")
print(f"El coche 2 es de marca {coche2.marca}, color {coche2.color} y su velocidad es {coche2.velocidad} km/h")
print(f"El coche 2 freno de {coche2.velocidad} a {coche2.frenar(100)}")