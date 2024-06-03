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

empleados= [
    ["Enzo",13,"Gamer"],
    ["Ingrid",15,"Estudiante"],
    ["Miriam",39,"Programadora"],
    ["Yoselin",18,"Cocinera"],
]

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
                nombre = input("Nombre(q para salir): ")
                if nombre == "q":
                    break
                edad = int(input("Edad: "))
                profesion = input("Profesion: ")
                
                empleado = [nombre, edad, profesion]
                empleados.append(empleado)

        elif opcionSec == 2:
            print("##### MODIFICACION ####")
        elif opcionSec == 3:
            print("##### BAJA ####")
            empleados.remove("Perro")
        #endif
    elif opcionPrincipal == 2:
        cabecera("Listado Empleados")
        print("Listado de Empleados")
        for empleado in empleados:
            # print(empleado) # ES UNA LISTA !!!
            print(f"{empleado[0]}, {empleado[1]} es: {empleado[2]}")
    elif opcionPrincipal == 3:
        cabecera("GESTION Empleadores")



print("FIN del sistema, volve mañana")



