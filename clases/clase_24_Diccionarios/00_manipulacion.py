
"""
Un diccionario o dict es mutable, se define usando llaves {}, 
los elementos son pares clave:valor
"""
# un diccionario que representa los datos de una persona
persona = {
  "nombre":"Yoselin",
  "edad": 17,
  "profesion":"Cocinera"
}

len(persona) # 3

persona2 = {
  "nombre":"Ingrid",
  "profesion":"estudiante",
  "edad": 15
}
# Acceder a un elemento y mostrarlo por pantalla 
# o realizar alguna operacion

variable = persona["edad"] 
print(variable)

# Modificar un elemento

persona["edad"] = persona["edad"] + 1 

if persona["edad"] >= 18:
    print("Sos mayor")
else:
    print("Sos menor", persona["edad"])

# Agregar un elemento

persona["colorFavorito"] = "Azul"
persona2["altura"] = 1.75

# Eliminar un elemento

persona2.pop("edad")

# Algunos metodos de los diccionarios

print(persona.keys())
print(persona.values())
print(persona.items()) #[('nombre', 'Yoselin'), ('edad', 18), ('profesion', 'Cocinera'), ('colorFavorito', 'Azul')]


print(":"*100)
print(persona)
print(":"*100)

print(persona2)

