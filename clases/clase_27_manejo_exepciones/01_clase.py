

while True:
    edad = input("Dame la edad: ") # "5y"

    try:
        edad = int(edad)
        if edad < 0: 
            print("La edad no deberia ser negativa")
        else:
            break
    except:
        print("La edad debe de ser un entero") 


edadEndiezAnios = edad + 10

print(f"Tu edad en 10 años sera de {edadEndiezAnios}.- ")