"""
Tope máximo de extracción
Escribe un programa para un cajero automático de un banco que permita
ingresar un importe y determine si la extracción puede hacerse o el usuario
debe realizarla por la caja. El tope máximo es de $ 20000. 
"""

monto = input("Ingrese el monto a extraer ")
monto = float(monto)

if monto <= 20000:
    print("La extracción puede realizarse.")
else:
    print("La extracción debe realizarse por caja.")
#endif

