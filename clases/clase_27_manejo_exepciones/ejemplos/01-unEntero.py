

edad=0
try:
  edad = int(input("Ingrese edad: "))
except ValueError:
  print("Hola")
except:
  print("Ingresa un numero entero si y solo si!!")

if edad >= 18:
  print("Sos mayor de edad")
else:
  print("Sos menor!")

'''
  Primera correccion
try:
  edad = int(input("Ingrese edad: "))
except:
  print("Ingresa un numero entero si y solo si!!")


Una mejor correccion es colocarlo en un while True para asegurar salir con un valor entero en edad
  '''

