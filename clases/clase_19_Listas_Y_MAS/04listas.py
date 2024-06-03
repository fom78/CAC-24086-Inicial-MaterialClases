
# Las listas son secuencia de elementos
mi_lista = [1, 2, 3, 4, 5, 6 , 65, -9]
frutas = ["pera","manzana","uva"]

fruta1 = "pera"
fruta2 = "manzana"
fruta3 = "uva"


otra= [True, False, True, 5, "Pera", "Pera",45,[2,2,5,"sdjkhsdhj"]]


print(len(otra))


print(frutas)
print(frutas[1])

# Podemos cambiar el valor de un elemento, porque son MUTABLES

frutas[1] = "naranja"

print(frutas[1])
#Agregar elementos

frutas.append("mandarina")
frutas.append(True)
frutas.append(34)

print(len(frutas),frutas)


frutas.pop(2)
frutas.pop(2)

print(len(frutas),frutas)





