#practica 1 implementar paradigma estructurado vs 00
#crear una proframa que obtemga el area de un rectangulo

#2
import os
os.system ("cls")

class AreaRectangulo:
    def areaRectangulo(self,base,altura):
        area=base*altura
        return area
    
rectangulo=AreaRectangulo()

print(f"El area del rectangulo es: {rectangulo.areaRectangulo(5,6)}")



class AreaRectangulo:
    def __init__(self,base,altura):
         self.base=base
         self.altura=altura
    
    def areaRectangulo(self):
        
        area=self.base*self.altura
        return area
    
rectangulo=AreaRectangulo()

print(f"El area del rectangulo es: {rectangulo.areaRectangulo()}")

