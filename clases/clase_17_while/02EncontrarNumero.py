

from random import randint

numeroDePc = randint(0,9)

continuar = True
intentos = 0
# while continuar == True:
while continuar:
    numeroUsuario=input("Que nro es (0-9): ")
    numeroUsuario = int(numeroUsuario)
    if numeroDePc == numeroUsuario:
        print("Acertaste!!!!!")
        continuar = False
    else:
        print("volve a intentar")
    # endif
    intentos=intentos+1

print(f"FIN del juego, usaste {intentos} intentos.-")