#Instanciar los objetos para posterior implementarlos 
from model import coches,cochesBD
import os

def borrarPantalla():
   os.system("cls") 

def esperaTecla():
    input("\n\t... Oprima una tecla para continuar ...")   

def datos_autos(tipo):
    borrarPantalla()
    print(f"\n\t ...Ingresar los datos del Vehiculo de tipo: {tipo}")
    marca=input("Marca: ").upper()
    color=input("Color: ").upper()
    modelo=input("Modelo: ").upper()
    velocidad=int(input("Velocidad: "))
    potencia=int(input("Potencia: "))
    plazas=int(input("No. de plazas: "))
    return marca,color,modelo,velocidad,potencia,plazas

def imprimir_datos_vehiculo(marca,color,modelo,velocidad,potencia,plazas):
    borrarPantalla()
    print(f"\n\tDatos del Vehiculo: \n Marca:{marca} \n color: {color} \n Modelo: {modelo} \n velocidad: {velocidad} \n caballaje: {potencia} \n plazas: {plazas}")

def resultados_inserar(respuesta):
    if respuesta:
        print("/n/tRegistro insertado correctamente")
    else:
        print("/n/tNo fue posible insertar el registro, intenta lo nuevamente ...")

def autos():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Auto")
    coche=coches.Coches(marca,color,modelo,velocidad,potencia,plazas)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    return(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)

            
def camionetas():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camioneta")
    traccion=input("Traccion: ").upper()
    cerrada=input("¿Cerrada (Si/No)?: ").upper().strip()
    if cerrada=="SI":
        cerrada=True
    else:
        cerrada=False    
    coche=coches.Camionetas(marca,color,modelo,velocidad,potencia,plazas,traccion,cerrada)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"traccion: {coche.traccion}\n cerrada: {coche.cerrada}")
    #Agregar en la BD
    respuesta=cochesBD.Camionetas.insertar(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas,coche.traccion,coche.cerrada)
    resultados_inserar(respuesta)


def camiones():
    marca,color,modelo,velocidad,potencia,plazas=datos_autos("Camiones")
    eje=int(input("No. de ejes: "))
    capacidadCarga=int(input("Capacidad de carga: "))
    coche=coches.Camiones(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    imprimir_datos_vehiculo(coche.marca,coche.color,coche.modelo,coche.velocidad,coche.caballaje,coche.plazas)
    print(f"#Ejes: {coche.eje}\n Capacidad de carga: {coche.capacidadCarga}")
    #Agregar en la BD
    respuesta=cochesBD.Camiones.insertar(marca,color,modelo,velocidad,potencia,plazas,eje,capacidadCarga)
    resultados_inserar(respuesta)

def main():
   opcion=True
   while opcion:
    os.system("clear")
    opcion=input("\n\t\t ::: Menu Principal ::.\n\t1.- Autos\n\t2.-Camionetas\n\t3.-Camiones\n\t4.-Salir\n\tElige un opción: ").lower().strip()
    match opcion:
        case "1":
            autos()
            
        case "2":
            camionetas()
            
        case "3":
            camiones()
            
        case "4":
            borrarPantalla()
            input("\n\t\tSalir del Sistema")
            opcion=False   
        case _:
            input("\n\tOpcion invalidad ... vuelva a intertarlo ... ")      

if __name__=="__main__":
    main()

def menu_acciones(tipo):
    borrarPantalla()
    print(f"\n\t ...Menu de Acciones del Vehiculo de tipo: {tipo}")
    opcion=input("\n\t1.- Insertar\n\t2.-Actualizar\n\t3.-Eliminar\n\t4.-Consultar todos\n\t5.-Salir\n\tElige una opción: ").lower().strip()
    return opcion

def menu_autos():
    while True:
     borrarPantalla()
     opcion=menu_acciones("Auto")
     if opcion=="1" or opcion=="insertar":
        marca,color,modelo,velocidad,caballaje,plazas=autos()
        #Agregar en la BD
        auto=cochesBD.Autos(marca,color,modelo,velocidad,caballaje,plazas)
        respuesta=auto.insertar()
        resultados_inserar(respuesta)
        esperaTecla()
     elif opcion=="2" or opcion=="consultar":
        print("\n\tConsultar todos los autos")
        borrarPantalla()
        resultados=cochesBD.Autos.consltar_todos()
        if len(resultados)>0:
            num_autos=1
            for fila in resultados:
                print(f"\n\tAuto No. {num_autos} compuesto por: \n ID: {fila[0]} \n Marca: {fila[1]} \n Color: {fila[2]} \n Modelo: {fila[3]} \n Velocidad: {fila[4]} \n Caballaje: {fila[5]} \n Plazas: {fila[6]}")
                num_autos+=1
                esperaTecla()
        else:
            print("\n\tNo hay autos registrados en la BD")
            esperaTecla()
     elif opcion=="3" or opcion=="actualizar":
        borrarPantalla()
        id_=input("Ingrese el ID del auto a actualizar: ")
        respuesta=cochesBD.Autos.actualizar(marca,color,modelo,velocidad,caballaje,plazas,id_)
        esperaTecla()
     elif opcion=="4" or opcion=="Eliminiar":
        print("\n\tEliminar un auto")
        id_=input("Ingrese el ID del auto a eliminar: ")
        respuesta=cochesBD.Autos.eliminar(marca,color,modelo,velocidad,caballaje,plazas,id_)
        resultados_inserar(respuesta)
        esperaTecla()
     elif opcion=="5" or opcion=="salir":
        borrarPantalla()
        break
     else:
        input("\n\tOpcion invalidad ... vuelva a intertarlo ... ")
        esperaTecla()