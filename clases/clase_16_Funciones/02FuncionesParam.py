
# Parametros y argumentos !!!
def saludar(nombre, edad):
    nombre = nombre.upper()
    if edad >= 30:
        edad = edad - 5
    print("###############❤️")
    print(f"Hola {nombre}, Tu edad es: {edad}")
    print("###############❤️")

def otra():
    print("eeeee")

saludar("Fer".upper(),45) # Invocacion de la funcion o llamada
saludar("Enzo", 13)
saludar("Yose", 18)
saludar("Juli", 15)
saludar("Pepe",33)

# nombre = input("Dame tu nombre: ")
# edad = input("Dame tu edad: ")
# edad = int(edad)

# saludar(nombre,edad)

# saludar()
