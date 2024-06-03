
# notas = [7,8,9,2,2,6]
notas=[]
while True:
    nro = input("Dame la nota: (0 para salir) ")
    if nro == "0":
        break
    #endif
    nro = float(nro)
    notas.append(nro)

# Colocar una nota en el 3er lugar (posicion o indice 2 de la lista)

notas.insert(2,10)




print(notas)
# Eliminar la posicion 2
notas = [7,8,2,9,2,3,2,6]

notas.remove(2)

notas.remove(2)

print(notas)



promedio = sum(notas) / len(notas)

print(f"El promedio para este alumno/a es {promedio}")