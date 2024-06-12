

persona = {
  "nombre":"Yoselin",
  "edad": 17,
  "profesion":"Cocinera"
}


# Iterando por clave
for var in persona.keys(): # persona.keys() >> ['nombre', 'edad', 'profesion']
    if  var == "profesion":
        print(persona[var])

for k,v in persona.items(): # [(key, value), ...  ] [("nombre", "Yoselin"), ("profesion","Cocinera"), ("edad",17)]
    print(f"{k} -- {v}")

for var in persona.keys(): 
    print(f"{var} -- {persona[var]}")