import json
import os

d = os.path.dirname(__file__)
os.chdir(d)


archivo = open("personas.json","r")

personas = json.load(archivo) # [{},{}]

archivo.close()


for p in personas:
    if p["edad"] <= 18:
        print(p)

personas.append({'nombre': 'Ingrid', 'edad': 15, 'profesion': 'Gamer', 'estaTrabajando': False})

archivo = open("personas.json","w")

json.dump(personas,archivo, indent=1) 

archivo.close()