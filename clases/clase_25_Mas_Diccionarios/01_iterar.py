

persona = {
  "nombre":"Yoselin",
  "edad": 17,
  "profesion":"Cocinera"
}


# Iterando por clave
for var in persona.keys(): # persona.keys() >> ['nombre', 'edad', 'profesion']
    if  var == "profesion":
        print(persona[var])

