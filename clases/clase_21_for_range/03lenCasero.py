
def lenCaserito(secuencia):
    contador = 0

    for iterable in secuencia:
        contador = contador + 1
    #end for
    return contador
    




leyenda = input("Dame un texto ")

# cantidad = len(leyenda)
cantidad = lenCaserito(leyenda)

print(f"Tu texto ingresado tiene {cantidad} caracteres !!!")