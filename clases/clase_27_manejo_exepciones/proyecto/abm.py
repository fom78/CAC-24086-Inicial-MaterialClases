
from primermodulo import validacionInt

""" un empleado
{
    "nombre": "Fernando",
    "edad": 45,
    "profesion": "Docente",
    "trabajando": True
}

"""
def altaEmpleado(listado):
    print("##### ALTA ####")
            
    while True:
        nombre = input("Nombre(q para salir): ")
        if nombre == "q":
            break
        # edad = int(input("Edad: "))
        edad = validacionInt("Edad: ")
        profesion = input("Profesion: ")
        
        empleado = {
            "nombre": nombre,
            "edad": edad,
            "profesion": profesion,
            "trabajando": False
        }
        listado.append(empleado)
    return listado

def modificacionEmpleado():
    print("##### MODIFICACION ####")
 