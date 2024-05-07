
def validacionInt(leyenda):
    continuar=True
    while continuar:
        numero = input(leyenda)
        if numero.isdigit():
            continuar = False
        else:
            print(f"Che, admito solo numeros ({numero}) 🏆🏆")
        #endif
    #endwhil
    numero = int(numero)
    return numero
#enddef    

edad = validacionInt("EDAD: ")

nro = validacionInt("NRO: ")

nro2 = validacionInt("otro NRO: ")


nro4 = validacionInt("Otro validado: ")

nro3 = int(input("Otrooo sin validar"))
res = edad + nro
print(f"El resultado da: {res}")


