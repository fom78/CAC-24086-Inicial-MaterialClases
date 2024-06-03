
# creamos diccionario con los elementos 

dic1 = {
  "cuadrado": 4,
  "triangulo": 3,
  "rectangulo": 4,
  "hexagono": 6,
  "pentagono": 5,
  "rombo": 4,
}


dic2= {
  4: ["Pepe", 10],
  2: (10,2,4),
  5: 42.98,
  7: "Hola!!",
  8: ["Pepe", 10],
  10: ["Pepe", 30],
}

# Obtener un valor segun su clave

'''print(dic1["cuadrado"]) # 4

print(dic1.get("hexagono")) # 6'''

# Modificar un valor segun su clave

'''dic1["cuadrado"] = 8
print(dic1["cuadrado"]) # 8

dic2[7] = (23,21)
print(dic2.get(7)) # (23,21)'''

# Agregar un elemento, si existe la clave lo edita, le cambia el valor.
'''
dic1["octagono"] = 8
print(dic1["octagono"]) # 8

dic2.update({4:"hola", "dd":34})
print(dic2)

dic1.update({"cuadrado":5, "octagono":8, "pentagono":7})
'''

# Eliminar un elemento segun su clave

# dic1.clear()
# dic1.pop("cuadrado")


print(dic1)
