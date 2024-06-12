"""
https://docs.python.org/es/3/library/json.html

JSON = JavaScript Object Notation

La mayoría de los lenguajes de programación que usamos hoy en día pueden generar y leer JSON.


Para usar json en python existe un modulo que viene ya instalado cuando se instala python, al igual que random, math, os, etc ...
Este modulo es: json

Lo usamos primero importandolo y luego llamando a sus funciones:

import json


Para cargar el contenido del archivo:
json.load(<archivo>)
- El archivo debe ser una variable que lo contenga en modo lectura.
- La funcion retornara datos (lista) que podremos manipular

Para esribir una lista en el archivo:

json.dump(<datos>,<archivo>)
- <datos> sera normalmente la lista que queremos guardar en el archivo
- <archivo> sera el archivo que vamos a escribir.

"""

print(">>>>>>>>>>",__file__)

