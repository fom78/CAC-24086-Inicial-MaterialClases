import os

def cabecera(leyenda):
    # os.system("cls")
    print("*###########*")
    print(f"{leyenda}")
    print("*###########*")

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

TOPE = 3
accesoPermitido = False
intentos = 1

empleados = []

while intentos <= TOPE:
    intentos= intentos + 1
    print("Accediendo al sistema")
    # usuario = input("Usuario: ")
    # clave = input("Clave: ")
    usuario = "admin"
    clave = "1234"
    if usuario == "admin" and clave == "1234":
        print("Acceso Correcto 🏆")
        # intentos = TOPE + 1 
        accesoPermitido = True
        break
    else:
        print("Credenciales incorrectas")


while accesoPermitido:
    cabecera("MENU Principal")

    print("1 Gestion de Empleados")
    print("2 Listado empleado")
    print("3 Gestion de Empleadores")

    print("0 Salir")

    # opcionPrincipal = input("Opcion: ")
    # opcionPrincipal = int(opcionPrincipal)

    opcionPrincipal = validacionInt("Opcion: ")

    if opcionPrincipal == 0:
        print("Saliendo del sistema ....")
        accesoPermitido= not accesoPermitido
    elif opcionPrincipal == 1:
        cabecera("SUBMENU Empleados")
        print("1 Alta empleado")
        print("2 Modificacion empleado")
        print("3 Baja empleado")
        opcionSec = validacionInt("Opcion: ")
        if opcionSec == 1:
            print("##### ALTA ####")
            while True:
                nombre = input("Nombre: (0 para salir) ")
                if nombre == "0":
                    break
                #endif
                empleados.append(nombre)
            #enwhile
            print("No se ingresan mas nombres ....")

        elif opcionSec == 2:
            print("##### MODIFICACION ####")
        elif opcionSec == 3:
            print("##### BAJA ####")
        #endif
    elif opcionPrincipal == 2:
        cabecera("Listado Empleados")
        print(empleados)
    elif opcionPrincipal == 3:
        cabecera("GESTION Empleadores")



print("FIN del sistema, volve mañana")

