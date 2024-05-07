

continuar=True
while continuar:
    edad = input("EDAD: ")
    if edad.isdigit():
        continuar = False
    #endif
#endwhile

edad = int(edad)

continuar=True
while continuar:
    nro = input("NRO: ")
    if nro.isdigit():
        continuar = False
    #endif
#endwhile
nro = int(nro)

res = edad + nro
print(f"El resultado da: {res}")


# print("Hola".isdigit())
# print("1234".isdigit())

