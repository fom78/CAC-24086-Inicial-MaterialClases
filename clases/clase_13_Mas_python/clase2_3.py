

# NameError: name 'apellido' is not defined
#print("Hola", apellido)

nombre = input("Dame tu nombre: ") # leer variable
edad = input("Tu edad ? ") # 45 o "45"

# Python es dinamicamente tipado
edad = int(edad)


altura = input("Que altura tenes: ") # 1.77 "1.77"
altura = float(altura)

# Opcion en una linea
#altura = float(input("Que altura tenes: ")) # 1.77 "1.77"



edadDentroDeDiezAnios = edad + 10

print(nombre.upper()," Tu edad dentro de 10 años sera de ",edadDentroDeDiezAnios, "años.-" )

# f - strings

print(f"{nombre.upper()} Tu edad dentro de 10 años sera de {edadDentroDeDiezAnios} años!!")
