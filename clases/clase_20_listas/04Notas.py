
notas=[]
while True:
    nro = input("Dame la nota: (0 para salir) ")
    if nro == "0":
        break
    #endif
    nro = float(nro)
    notas.append(nro)


promedio = sum(notas) / len(notas)

menor = min(notas)
mayor = max(notas)

print(f"El promedio para este alumno/a es {promedio}, la menor nota: {menor} y su mayor desempeño fue un: {mayor}")