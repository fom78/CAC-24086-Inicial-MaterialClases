

frutas = [["Pera",5], ["uva",8], ["naranja",4],["manzana",56],["banana",5]]


print("-"*30)
print("Listado de frutas".center(30,"-"))
print("-"*30)
for fruta in frutas: # ["Pera",5]
    print(f"{fruta[0]} - {fruta[1]}")
