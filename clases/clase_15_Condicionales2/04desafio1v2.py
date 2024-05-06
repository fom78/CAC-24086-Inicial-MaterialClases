
continuar = Verdadero
productos=0
Mientras continuar Hacer
    leer montoProducto
    montoTotal = montoTotal + montoProducto
    productos=productos+1
    leer "desea continibuar" continuar
Fin Mientras

# montoTotal = input("Monto Total: ")
# montoTotal = float(montoTotal)



# cantidadArticulos = input("# Articulos: ")
# cantidadArticulos = int(cantidadArticulos)


totalAPagar=0
if cantidadArticulos >= 5 and montoTotal > 10000:
    #Caso 1
    totalAPagar = montoTotal * 0.85
elif cantidadArticulos < 5 and cantidadArticulos >=3:
    totalAPagar = montoTotal * .9
else:
    totalAPagar = montoTotal

print(f"El total a pagar es de: {totalAPagar}")