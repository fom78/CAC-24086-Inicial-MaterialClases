"""
Tope máximo de extracción
Escribe un programa para un cajero automático de un banco que permita
ingresar un importe y determine si la extracción puede hacerse o el usuario
debe realizarla por la caja. El tope máximo es de $ 20000. 
"""
montoDisponible= 100000

monto = input("Ingrese el monto a extraer ")
monto = float(monto)

if monto <= 20000:
    print("La extracción puede realizarse.")
else:
    print("La extracción debe realizarse por caja.")
#endif

if monto <= montoDisponible:
    saldo = montoDisponible - monto
    # print("Tu saldo es: ", saldo, " pesos")
    # F-String
    print(f"Tu saldo es: {saldo}  pesos.-")
else:
    print(f"Saldo insuficiente, tu monto es: {montoDisponible}")
#endif

print("Hasta luego")