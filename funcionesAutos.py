#funcion agregar auto
def agregarAuto(numeroMotor,marca,modelo,color,cantidadPuertas):
    auto=[numeroMotor,marca,modelo,color,cantidadPuertas]
    return auto

def buscarAuto(matrizAuto,numeroMotor):
    mensaje="No hay registros"
    for i in range(len(matrizAuto)):
        if(numeroMotor==matrizAuto[i][0]):
            mensaje="\nRegistro encontrado."
            mensaje+="\nNumero De Motor: "+str(numeroMotor)
            mensaje+="\nMarca: "+matrizAuto[i][1]
            mensaje+="\nModelo: "+str(matrizAuto[i][2])
            mensaje+="\nColor: "+matrizAuto[i][3]
            mensaje+="\nCantidad de puertas: "+str(matrizAuto[i][4])
        break
    print(mensaje)

def listarAutos(a): 
    if(len(a)>=1):
        mensaje=""
        mensaje+="\n----------ESTA ES LA LISTA DE AUTOS-------: "
        for i in range(len(a)):
            mensaje+="\n---------Registro N "+str(i+1)
            mensaje+="\nNumero Motor: "+str(a[i][0])
            mensaje+="\nMarca: "+a[i][1]
            mensaje+="\nModelo: "+str(a[i][2])
            mensaje+="\nColor: "+a[i][3]
            mensaje+="\nCantidad de puertas: "+str(a[i][4])  
    else:
        mensaje="No hay registros"
    print(mensaje)

def modificarAuto(matriz, numero):
    mensaje="Auto no encontrado"
    for i in range(len(matriz)):
        if (numero==matriz[i][0]):
           nuevocolor= input("ingrese el nuevo color: ")
           matriz[i][3]=nuevocolor
           mensaje="Color modificado"
    print(mensaje)
    
def borrarAuto(matrizAuto, numeroMotor):
    mensaje="no se encontró registro"
    for i in range(len(matrizAuto)):
        if(numeroMotor==matrizAuto[i][0]):
            del matrizAuto[i]
            mensaje="registro eliminado"
            break
    print(mensaje)
        


    