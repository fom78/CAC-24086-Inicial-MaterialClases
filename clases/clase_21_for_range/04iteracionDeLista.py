

frutas = ["Pera", "uva", "naranja","manzana","banana"]


print("-"*30)
print("Listado de frutas".center(30,"-"))
print("-"*30)
for fruta in frutas:
    print(f"{fruta.center(30," ")} {fruta[0]}")
