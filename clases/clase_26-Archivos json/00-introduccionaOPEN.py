'''
Con Python podemos de manera muy simple manejar archivos.
Vamos a ver las instrucciones basicas, como abrir un archivo, leerlo o escribirle informacion.

Abrir un archivo

open(archivo,modo)

archivo --> Es el nombre del archivo, si no va acompañado de una ruta, se tomara la ruta actual.
modo --> uno de los distintos modos para abrir un archivo.

Modos disponibles:
Read ("r") (Leer)
Append ("a") (Agregar)
Write ("w") (Escribir)
Create ("x") (Crear)
'''

# Maneras de crear un archivo

'''
Para crear un archivo
archivo = open("archivo_nuevo.txt", "x")
>>> Modo write
Si queremos abrir el archivo y escribir un nuevo contenido, eliminado el anterior lo abrimos con el modo "w·
y luego ejecutando el metodo write() escribira el nuevo contenido
archivo = open("colores.txt","w")
archivo.write("Nuevo contenido etc")

>>> Modo append
Con append agregamos algo al final del archivo, asi que abrimos en ese modo el archivo

archivo = open("colores.txt","a")

Y luego agregamos texto con el metodo write()

archivo.write("\nNegro")

'''

# Cerrar el archivo
'''
Luego de usar un archivo es muy importante cerrarlo, para ello esta el metodo close()

archivo.close()
'''


# Lecturas de archivos

'''
Como leer el archivo y trabajarlo

Para leer una linea usamos el metodo readline()

archivo.readline(<tamaño_opcional>)
El tamaño es en bytes y es opcional, no lo usaremos nosotros.

Ejemplo

archivo = open("colores.txt","r")
print(archivo.readline())
archivo.close()


Para recorrer o iterar un archivo lo podemos hacer linea por linea de la siguiente manera directamente sobre el objeto de archivo:

archivo = open("colores.txt","r")
for linea in archivo:
  # Realizamos las tareas necesaria con cada linea, ejemplo la imprimimos decorada
  print("···",linea)
archivo.close()

Tambien podemos iterar sobre el resultado del metodo readlines(), el cual devuelve una lista

archivo = open("colores.txt","r")
for linea in archivo.readlines():
  # Realizamos las tareas necesaria con cada linea, ejemplo la imprimimos decorada
  print("···",linea)
archivo.close()


Para trabajar en el directorio donde se encuentra el archivo se puede con estas lineas solucionar rapidamente:

import os
dirDeTrabajo = os.path.dirname(__file__)
os.chdir(dirDeTrabajo)
'''
