
while True:
  try:   
    numero1 = float(input("Primer numero "))
    numero2 = float(input("Segundo numero "))
    res = numero1 / numero2
    break
  except ValueError:
    print("Solo numeros.....")
  except ZeroDivisionError:
    print("No se puede dividir por cero...ingresa otro numero!!!")
# while
print("Resulatdo: ",res)

