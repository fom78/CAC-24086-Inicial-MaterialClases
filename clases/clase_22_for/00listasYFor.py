

# empleados = [
#     "Enzo",
#     "Ingrid",
#     "Miriam",
#     "Yoselin",
#     "Perro",
#     "Pepe",
#     5,
#     5.69,
#     True,
#     [],
#     [2,3,"Miriam"]
#     ]


# un empleado tiene nombre, edad, profesion 
# un empleado: [nombre,edad,profesion]
empleados = [
    "Enzo",
    "Ingrid",
    "Miriam",
    "Yoselin",
    ]

empleados= [
    ["Enzo",13,"Gamer"],
    ["Ingrid",15,"Estudiante"],
    ["Miriam",39,"Programadora"],
    ["Yoselin",18,"Cocinera"],
]

# print(empleados[2])

# Ingrid, 15 es: Estudiante
print("Listado de Empleados")
for empleado in empleados:
    # print(empleado) # ES UNA LISTA !!!
    print(f"{empleado[0]}, {empleado[1]} es: {empleado[2]}")



while True:
    nombre = input("Nombre(q para salir): ")
    if nombre == "q":
        break
    edad = int(input("Edad: "))
    # edad = int(edad)
    profesion = input("Profesion: ")
    
    # empleado = []
    # empleado.append(nombre)
    # empleado.append(edad)
    # empleado.append(profesion)
    empleado = [nombre, edad, profesion]

    # Que hago con empleado ===)))??? Agreagr el empleado a la lista empleadoS
    empleados.append(empleado)
    # continuar = input("Desea continuar ? (s/n)")
    # if continuar == "n":
    #     break
    

print("Listado de Empleados")
for empleado in empleados: # "Fer"
    # print(empleado) # ES UNA LISTA !!!
    print(f"{empleado[0]}, {empleado[1] + 10} es: {empleado[2]}")