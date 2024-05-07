

"""
Mientras condicion hacer
    sentencia1
    sentencia2
    sentencian
Fin Mientras
"""

# El while se ejecuta un nro indeterminado de veces
# En el caso siguiente podemos a priori saber cuantas veces se va a ejecutar.
nro=0
while nro<5:
    print(f"Hola {nro}")
    nro = nro + 1
#Fin while

if nro == 9:
    print("Chau")

# En este caso no podemos saber la cantidad de veces que se ejecutara

continuar = True

while continuar == True:
    nroUsuario = input("Dame un numero positivo(0 para terminar): ")
    nroUsuario = int(nroUsuario)
    if nroUsuario == 0:
        continuar = False

