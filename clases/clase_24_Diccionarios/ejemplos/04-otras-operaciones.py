
dic1 = {
  "cuadrado": 4,
  "triangulo": 3,
  "rectangulo": 4,
  "hexagono": 6,
  "pentagono": 5,
  "rombo": 4,
}


# cantidad de elementos
# len(dic1)

print(len(dic1)) # 6

# Pertenencia
'''
Si queremos saber si una clave o un valor estan en un diccionario

print("rombo" in dic1.keys())

print(3 in dic1.values())


'''

print("rombo" in dic1.keys()) # True
print("circulo" in dic1.keys()) # False


print(3 in dic1.values()) # True
print(9 in dic1.values()) # False

