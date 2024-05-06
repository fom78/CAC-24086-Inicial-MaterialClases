"""
Descuentos en tienda de ropa
Escribe un programa en Python que solicite al usuario el monto total de la
compra y la cantidad de artículos que está comprando. El programa debe
determinar el descuento aplicable según las siguientes reglas:
● Si la cantidad de artículos comprados es mayor o igual a 5 y el monto
total es mayor a $10000, aplica un descuento del 15%.
● Si la cantidad de artículos comprados es menor a 5 pero mayor o igual a
3, aplica un descuento del 10%.
● Si la cantidad de artículos comprados es menor a 3, no se aplica
descuento.
Al final, el programa debe imprimir el monto total de la compra después de
aplicar cualquier descuento o simplemente el monto original si no hay
descuento.
"""

montoTotal = input("Monto Total: ")
montoTotal = float(montoTotal)

cantidadArticulos = input("# Articulos: ")
cantidadArticulos = int(cantidadArticulos)

"""
Si la cantidad de artículos comprados es mayor o igual a 5 y el monto
total es mayor a $10000, aplica un descuento del 15%.
"""

totalAPagar=0
if cantidadArticulos >= 5 and montoTotal > 10000:
    #Caso 1
    totalAPagar = montoTotal * 0.85
elif cantidadArticulos < 5 and cantidadArticulos >=3:
    totalAPagar = montoTotal * .9
else:
    totalAPagar = montoTotal

print(f"El total a pagar es de: {totalAPagar}")