class figuras:
    def __init__(self, x, y, visible, estaVisible, mostrar, ocultar, mover, calcularArea):
        self.x = x
        self.y = y
        self.visible = visible
        self.estaVisible = estaVisible
        self.mostrar = mostrar
        self.ocultar = ocultar
        self.mover = mover
        self.calcularArea = calcularArea

class Rectangulos(figuras):
    def __init__(self, x, y, ancho, alto):
        super().__init__(x, y, True, self.estaVisible, self.mostrar, self.ocultar, self.mover, self.calcularArea)
        self.ancho = ancho
        self.alto = alto

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcularArea(self):
        return self.ancho * self.alto
    
class Circulos(figuras):
    def __init__(self, x, y, radio):
        super().__init__(x, y, True, self.estaVisible, self.mostrar, self.ocultar, self.mover, self.calcularArea)
        self.radio = radio

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcularArea(self):
        import math
        return math.pi * (self.radio ** 2)
    
circulo1=Circulos(0, 0, 5)
rectangulo1=Rectangulos(10, 10, 4, 6)
        
print("Área del círculo:", circulo1.calcularArea())
print("Área del rectángulo:", rectangulo1.calcularArea())