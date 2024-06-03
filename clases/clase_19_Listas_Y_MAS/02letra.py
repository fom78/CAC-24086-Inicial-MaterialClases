



leyenda="Hola ClAse"

caracterActual = 0
resultado=""
while caracterActual < len(leyenda): #10
    if leyenda[caracterActual] == "a" or leyenda[caracterActual] == "e" or leyenda[caracterActual] == "i" or leyenda[caracterActual] == "o" or leyenda[caracterActual] == "u":
        # Es vocal
        resultado = resultado + leyenda[caracterActual].upper()
    else:
        # Es Consonante
        resultado = resultado + leyenda[caracterActual].lower()
    #endif
    caracterActual = caracterActual + 1
#endWhile

print(resultado)

