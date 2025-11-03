#Instanciar los objetos para posteriormente implementarlos

from coches import Coche

num_coches=int(input("Cuantos coches quieres crear: "))


for i in range(0,num_coches):
	print(f"Datos del coche {i+1}")
	marca=input("Introduce la marca del coche: ").upper()
	color=input("Introduce el color del coche: ").upper()
	modelo=input("Introduce el modelo del coche: ").upper()
	velocidad=int(input("Introduce la velocidad del coche: "))
	potencia=int(input("Introduce el potencia del coche: "))
	plazas=int(input("Introduce el numero de plazas del coche: "))


	coche1=Coche(marca,color,modelo,velocidad,potencia,plazas)

	print(f"El coche 1 es un {coche1.getMarca()} y el color es {coche1.getColor()} Modelo:{coche1.getModelo()} Velocidad:{coche1.getVelocidad()} Caballaje{coche1.getCaballaje()} Plazas{coche1.getPlazas()}" )
	
	print(coche1.acelerar())
