import os
os.system("cls")

coche1=Coches()
coche2=Coches()
coche3=Coches()

coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
coche1.num_serie="123ABC"

coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

coche3.setMarca("Toyota")

print(f"El coche 1 es un {coche1.getMarca()} y el color es {coche1.getColor()} Modelo:{coche1.getModelo()} Velocidad:{coche1.getVelocidad()} Caballaje{coche1.getCaballaje()} Plazas{coche1.getPlazas()}" )


class Coche:
    __marca=""
    __color=""
    __modelo=""
    __velocidad=0
    __caballaje=0
    __plazas=0


   
    def acelerar(self):   
        pass

    def frenar(self):
        pass





coche1=Coche()
coche1.marca="vw"
coche1.color="blanco"
coche1.modelo="2022"
coche1.velocidad=180
coche1.__caballaje=150
coche1.plazas=6

#•#Crear»Los-netodos-setters-y-getters•,-estos-netodos-son• Importantes y necesarios-en-todas •las. clases • para-que-el-programador-interactue-con• los-valores-de•los-atributos•a-traves-de-estos• metodos• ...•digamos •que-es - la-manera-mas-adecuada-y• recomendada•para•solicitar•un-valor•(get) •y/ o-para-ingresar•o-cambiar-un-valor+(set)-a•un• atributo-en-particular-de•la-clase•a-traves-devun-
#objeto.*
#•En•teoria• se-deberia•de-crear-un-metodo•Getters-y• Setters• por-cada-atributo-que- contenga•la-clase
#.••Los-metodos •get-siempre-regresan-valor-es-decir-el valor-de •la•propledad:a-traves-del-retum
#Por-otro-Lado-el-setodo•set-siempre•recibe-paranetros•para-canblar-o-modificar-el-valor-del-
#atributo-o-propiedad• en •cuestion

def getMarca(self):
    return self.marca

def setMarca(self,marca):
    self.marca=marca

def getColor(self):
    return self.color

def setColor(self,color):
    self.color=color

def getModelo(self):
    return self.modelo

def setModelo(self,modelo):
    self.modelo=modelo

def getVelocidad(self):
    return self.velocidad

def setVelocidad(self,velocidad):
    self.velocidad=velocidad

def getCaballaje(self):
    return self.caballaje

def setCaballaje(self,caballaje):
    self.caballaje=caballaje

def getPlazas(self):
    return self.plazas

def setPlazas(self,plazas):
    self.plazas=plazas




#Metodos-o•acciones•o-funciones•que-hace-el-objeto•

