import os

"""
cabecera imprime de manera bonita el titulo de los menues
param leyenda es el titulo bla bla
"""
def cabecera(leyenda, cantidadCaracter=80):
    os.system("cls")
    cantMedio = cantidadCaracter - 2
    print("#"*cantidadCaracter)
    print(f"#{leyenda.center(cantMedio," ")}#")
    print("#"*cantidadCaracter)

# Esta funcion valid,.....
def validacionInt(leyenda):
    continuar=True
    while continuar:
        numero = input(leyenda)
        if numero.isdigit():
            continuar = False
        else:
            print(f"Che, admito solo números ({numero}) 🏆🏆")
        #endif
    #endwhil
    numero = int(numero)
    return numero
#enddef