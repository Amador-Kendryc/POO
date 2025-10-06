class calculadora:
    def __init__(self):
        self.numero1 = int(input("Ingrese el primer numero: "))
        self.numero2 = int(input("Ingrese el segundo numero: "))

    @property
    def numero1(self):
        return self._numero1
    @numero1.setter
    
    @property
    def numero2(self):
        return self._numero2
    @numero2.setter

    def suma(self):
        R_suma = self.numero1 + self.numero2
        return R_suma

    def resta(self):
        R_resta = self.numero1 - self.numero2
        return R_resta

    def multiplicacion(self):
        R_multiplicacion = self.numero1 * self.numero2
        return R_multiplicacion

    def division(self):
        R_division = self.numero1 / self.numero2
        return R_division

calc = calculadora()
print(f"la suma es: {calc.suma()} \n la resta es: {calc.resta()} \n la multiplicacion es: {calc.multiplicacion()} \n la division es: {calc.division()}")