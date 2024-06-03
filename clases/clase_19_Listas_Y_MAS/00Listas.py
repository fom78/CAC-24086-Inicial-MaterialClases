# Definición de una lista
mi_lista = [1, 2, 3, 4, 5]

# Accediendo a elementos de la lista
print("Elemento en la posición 0:", mi_lista[0])  # Imprime: 1
print("Elemento en la posición 2:", mi_lista[2])  # Imprime: 3

# Modificando elementos de la lista
mi_lista[0] = 10
print("Lista después de modificar el primer elemento:", mi_lista)  # Imprime: [10, 2, 3, 4, 5]

# Agregando elementos a la lista
mi_lista.append(6)
print("Lista después de agregar un nuevo elemento:", mi_lista)  # Imprime: [10, 2, 3, 4, 5, 6]

# Removiendo elementos de la lista
elemento_removido = mi_lista.pop(2)
print("Elemento removido:", elemento_removido)  # Imprime: 3
print("Lista después de remover el elemento en la posición 2:", mi_lista)  # Imprime: [10, 2, 4, 5, 6]

# Longitud de la lista
longitud = len(mi_lista)
print("Longitud de la lista:", longitud)  # Imprime: 5

