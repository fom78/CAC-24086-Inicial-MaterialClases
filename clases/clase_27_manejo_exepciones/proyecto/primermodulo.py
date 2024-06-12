import os


def cabecera(leyenda, cantidadCaracter=80):
    """
cabecera imprime de manera bonita el titulo de los menues
param leyenda es el titulo bla bla
"""
    os.system("cls")
    cantMedio = cantidadCaracter - 2
    print("#"*cantidadCaracter)
    print(f"#{leyenda.center(cantMedio," ")}#")
    print("#"*cantidadCaracter)

# Esta funcion valid,.....
def validacionInt(leyenda):
    """
    Esta funcion retorna un enttero.
    Pasa como argumento la leyenda que queres ver en el input
    """
    while True:
        numero = input(leyenda)
        try:
            numero = int(numero)
            return numero
        except:
            print(f"Che, admito solo números ({numero}) 🏆🏆")