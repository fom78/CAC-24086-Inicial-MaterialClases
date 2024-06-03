
from primermodulo import validacionInt
def altaEmpleado(listado):
    print("##### ALTA ####")
            
    while True:
        nombre = input("Nombre(q para salir): ")
        if nombre == "q":
            break
        # edad = int(input("Edad: "))
        edad = validacionInt("Edad: ")
        profesion = input("Profesion: ")
        
        empleado = [nombre, edad, profesion]
        listado.append(empleado)
    return listado

def modificacionEmpleado():
    print("##### MODIFICACION ####")
 