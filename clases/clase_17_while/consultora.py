import os

def cabecera(leyenda):
    os.system("cls")
    print("*###########*")
    print(f"{leyenda}")
    print("*###########*")
continuar= not False
while continuar:
    cabecera("MENU Principal")

    print("1 Gestion de Empleados")
    print("2 Listado empleado")
    print("3 Gestion de Empleadores")

    print("0 Salir")

    opcionPrincipal = input("Opcion: ")
    opcionPrincipal = int(opcionPrincipal)

    if opcionPrincipal == 0:
        print("Saliendo del sistema ....")
        continuar= not continuar
    elif opcionPrincipal == 1:
        cabecera("MENU Empleados")
        print("1 Alta empleado")
        print("2 Modificacion empleado")
        print("3 Baja empleado")
        opcionSec = int(input("Opcion: "))
        if opcionSec == 1:
            print("##### ALTA ####")
        elif opcionSec == 2:
            print("##### MODIFICACION ####")
        elif opcionSec == 3:
            print("##### BAJA ####")
        #endif
    elif opcionPrincipal == 2:
        cabecera("Listado Empleados")
    elif opcionPrincipal == 3:
        cabecera("GESTION Empleadores")



print("FIN del sistema, volve mañana")

