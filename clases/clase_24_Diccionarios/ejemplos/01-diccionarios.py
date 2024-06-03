
# creamos un diccionario vacio

dic1 = {}
dic1 = dict()

# creamos diccionario con los elementos 
dic1 = {
  "cuadrado": 4,
  "triangulo": 3,
  "rectangulo": 4,
  "hexagono": 6,
  "pentagono": 5,
  "rombo": 4,
}


dic1= {
  4: ["Pepe", 10],
  2: (10,2,4),
  5: 42.98,
  7: "Hola!!",
  8: ["Pepe", 10],
  10: ["Pepe", 30],
}

'''creamos un diccionario mediante una coleccion, para esto
necesitamos tener una coleccion que contenga como elementos otra coleccion de pares.
'''
dic2 = dict([("cuadrado", 4),  ("triangulo", 3)])

print(dic1)
print(dir(dic1))