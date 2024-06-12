

try:
  numero1 = float(input("Primer numero "))
  numero2 = float(input("Segundo numero "))
  res = numero1 / numero2
  print(res)
except ValueError:
  print("Solo numeros.....")
except ZeroDivisionError:
  print("Imposible dividir por cero")
except:
  print("Algun error raro, llame al admin del sistema")
