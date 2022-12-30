from funcionesAutos import*
from os import system

matrizAuto=[]
openclosse=True
while(openclosse):
    print("por favor seleccione una opcion")
    print("1.Agregar")
    print("2.Buscar")
    print("3.Listar")
    print("4.Modificar")
    print("5.Eliminar")
    print("6.Salir")
    opcion=int(input("\nOpcion: "))
    
    #numeroMotor,marca,modelo,color,cantidadPuertas
    if(opcion==1):
        numeroMotor=(int(input("Ingrese Numero De Motor: ")))
        marca=input("ingrese la marca: ")
        modelo=int(input("ingrese el modelo: "))
        color=input("ingrese color del auto: ")
        cantidadPuertas=int (input("ingrese cantidad de puertas: "))
        
        matrizAuto.append(agregarAuto(numeroMotor,marca,modelo,color,cantidadPuertas))
        print("Auto Agregado Con Exito...")
    elif(opcion==2):
       numeroMotor=(int(input("Ingrese Numero De Motor: "))) 
       buscarAuto(matrizAuto,numeroMotor)
    elif(opcion==3):
       listarAutos(matrizAuto)
    elif(opcion==4):
        numeroMotor=int(input("ingrese el numero de motor: "))
        modificarAuto(matrizAuto, numeroMotor)        
    elif(opcion==5):
        numeroMotor=int(input("ingrese numero de motor:  "))
        borrarAuto(matrizAuto, numeroMotor)
    else:
        openclosse=False        
        print("Gracias por usar nuestro programa")
    
    
    
    
    
    
