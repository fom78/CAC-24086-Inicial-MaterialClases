# Algunos metodos de los diccionarios
persona = {
  "nombre":"Ingrid",
  "profesion":"estudiante",
  "edad": 15}

# [elem1,elem2,elemn]
"""
{ par1, par2,parn} => { clave1:valor1, clave2:valor2, claven:valorn}
Mas vistoso
{ 
  clave1:valor1, 
  clave2:valor2, 
  claven:valorn
  }

"""


print(persona.keys())
print(persona.values())

print(persona.items()) #[('nombre', 'Yoselin'), ('edad', 18), ('profesion', 'Cocinera'), ('colorFavorito', 'Azul')]

print(persona)

persona.pop("profesion")



print(persona)
# {'nombre': 'Ingrid', 'edad': 15}
# prof = persona["profesion"]

prof = persona.get("profesion", "Sin profesion")

print(f"La profesion es {prof.upper()}")

apellido = persona.get("apellido", None)

print(">>>>>>",persona)
if apellido != None:
    print(apellido)
else:
    print("Falta solicitarle el apellido")

