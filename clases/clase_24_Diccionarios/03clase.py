



nombre = input("Nombre ")
edad = input("Edad ")
edad = int(edad)
profesion = input("Profesion ")


empleado = {
    "nombre": nombre,
    "edad": edad,
    "profesion": profesion 
}

if empleado == {}:
    print("El dic esta vacio")
else:
    print(empleado)