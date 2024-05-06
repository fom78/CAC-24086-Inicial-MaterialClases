
# from math import sqrt
import math
from random import randint


# randint(valorinicial,valorfinal) da un entero entre vi y vf [7,99]
# azar(100)

opcionUsuario = int(input("Ingresa 1 - Piedra, 2 - Papel, 3 - Tijeras: "))
opcionCompu = randint(1,3) 

# nro = abs(-9)
# nro = math.sqrt(9)
# print(nro)
if opcionUsuario == opcionCompu:
    print("EMPATE!!!!!!")
else:

    if opcionUsuario == 1:
        if opcionCompu == 2:
            print("Perdiste!!!, la pc saco papel")
        else:
            print("Ganaste!!!, Piedra mata tijeras!")
        #endif
    #endif
    elif opcionUsuario == 2: #Papel
        if opcionCompu == 3:
            print("Perdiste!!!, la pc saco ✂️")
        else:
            print("Ganaste!!!, Papel mata Piedra!")
        #endif
    #endelif linea 19
    elif opcionUsuario == 3:
        if opcionCompu == 1:
            print("Perdiste!!!, la pc saco piedra")
        else:
            print("Ganaste!!!, Tijeras mata papel!")
        #endelif
#endif
print()

