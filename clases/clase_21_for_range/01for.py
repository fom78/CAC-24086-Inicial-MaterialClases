

# dato iterable
"""
Para que sea iterable debe ser una coleccion de elementos
dato[indice]
Datos iterables conocidos !!
- lista
- tuplas tuplita = (1,5,"t",True) tuplita[2]
- str "Hola Clase"[3]
- range
"""

# El for nos va a permitir iterar sobre colecciones de datos

""" Sintaxis
for iterable in secuencia:
    instruccion 1 
    instruccion 2 
    instruccion n
# endfor 
"""
for iterable in range(5): # 0 1 2 3 4
    print(f"Hola {iterable + 6}")
    print("Chau")


