
def validacionInt(leyenda):
    continuar=True
    while continuar:
        numero = input(leyenda)
        if numero.isdigit():
            continuar = False
        #endif
    #endwhile
    return numero
#enddef    

edad = validacionInt("EDAD: ")
edad = int(edad)

nro = validacionInt("NRO: ")
nro = int(nro)


nro2 = validacionInt("otro NRO: ")
nro2 = int(nro2)

res = edad + nro
print(f"El resultado da: {res}")


