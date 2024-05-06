
nombre = input("Dame tu nombre: ") # leer variable
edad = input("Tu edad ? ") # 45 o "45"

# Python es dinamicamente tipado
edad = int(edad)

altura = input("Que altura tenes: ") # 1.77 "1.77"
altura = float(altura)

edadDentroDeDiezAnios = edad + 10


"""
Si expresion entonces

Sino

FinSi

"""

"""
if expresion:

else:

"""



if altura <= 1.65 :
  deporte="Futbol"
  print()
else:
  deporte="Basquet"
#endif




print(f"{nombre.upper()} Tu edad dentro de 10 años sera de {edadDentroDeDiezAnios} años!! y en el club te vamos a probar en {deporte}")
