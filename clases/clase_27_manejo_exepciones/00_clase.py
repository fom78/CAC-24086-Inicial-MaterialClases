

edad = input("Dame la edad: ")


try:
    edad = int(edad)
except:
   print("La edad debe de ser un entero") 
   edad = 0


edadEndiezAnios = edad + 10

print(f"Tu edad en 10 años sera de {edadEndiezAnios}.- ")