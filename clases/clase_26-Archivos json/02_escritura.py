import json  # Importa el módulo json, que permite trabajar con datos en formato JSON.
import os    # Importa el módulo os, que proporciona funciones para interactuar con el sistema operativo.

d = os.path.dirname(__file__)
os.chdir(d)

# Define una lista de diccionarios, cada uno representando un conjunto de datos.
misdatos = [
    {
        "codigo": 23222222,  
        "color": "rojo",  
        "presente": True  
    },
    {
        "codigo": 2222,  
        "color": "rojo",  
        "presente": False  
    },
    {
        "codigo": 888888,  
        "color": "azul", 
        "presente": True  
    }
]

# Abre el archivo "datos.json" en modo escritura.
# Si el archivo no existe, se crea. Si existe, se sobreescribe.
archivito = open("datos.json", "w")

# Convierte la lista de diccionarios (misdatos) a formato JSON
# y escribe el resultado en el archivo "datos.json".
json.dump(misdatos, archivito, indent=4)

# Cierra el archivo después de haber escrito en él.
archivito.close()
