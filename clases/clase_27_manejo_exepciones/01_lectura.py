import json  # Importa el módulo json, que permite trabajar con datos en formato JSON.
import os    # Importa el módulo os, que proporciona funciones para interactuar con el sistema operativo.

# Obtiene el directorio donde se encuentra el script actual.
d = os.path.dirname(__file__)

# Cambia el directorio de trabajo actual al directorio del script.
os.chdir(d)

# Abre el archivo "datos.json" en modo lectura.

try:
    archivo = open("datosHola.json", "r")
except:
    archivo = open("datosHola.json", "w")
    json.dump([],archivo)
    archivo.close()
    archivo = open("datosHola.json", "r")



# Carga el contenido del archivo JSON en una variable llamada 'colores'.
# json.load(archivo) convierte el contenido JSON en un objeto de Python (en este caso, una lista de diccionarios).
colores = json.load(archivo)
# print(colores)
# Cierra el archivo después de haber leído su contenido.
archivo.close()

# Itera sobre cada elemento en la lista 'personas'.
# Se asume que cada elemento en 'personas' es un diccionario que representa una persona.
for color in colores:
    # Imprime el diccionario de cada persona.
    print(color)
