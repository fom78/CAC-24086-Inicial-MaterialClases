
from primermodulo import cabecera, validacionInt
from abm import altaEmpleado, modificacionEmpleado
from datos_prueba import empleados

print(empleados)
   
TOPE = 3
accesoPermitido = False
intentos = 1


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
    cabecera("MENU Principal",55)

    print("1 Gestion de Empleados")
    print("2 Listado empleado")
    print("3 Gestion de Empleadores")

    print("0 Salir")

    opcionPrincipal = validacionInt("Opcion: ")

    if opcionPrincipal == 0:
        print("Saliendo del sistema ....")
        break
    elif opcionPrincipal == 1:
        cabecera("SUBMENU Empleados",40)
        print("1 Alta empleado")
        print("2 Modificacion empleado")
        print("3 Baja empleado")
        opcionSec = validacionInt("Opcion: ")
        if opcionSec == 1: # alta
            empleados = altaEmpleado(empleados)
        elif opcionSec == 2:
            modificacionEmpleado()
        elif opcionSec == 3:
            print("##### BAJA ####")
            empleados.remove("Perro")
        #endif
    elif opcionPrincipal == 2:
        cabecera("Listado Empleados")
        print("Listado de Empleados")
        for empleado in empleados: # [{},{},{}, []]
            # print(empleado) # ES UNA LISTA !!!
            print(f"{empleado["nombre"]}({empleado["edad"]}) es: {empleado["profesion"]}")
        input("Presiona enter para continuar ...")
        # os.system("pause")
    elif opcionPrincipal == 3:
        cabecera("GESTION Empleadores")



print("FIN del sistema, volve mañana")



