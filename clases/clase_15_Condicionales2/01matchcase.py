
opcionUsuario = int(input("Ingresa 1 - Piedra, 2 - Papel, 3 - Tijeras"))

match opcionUsuario: # Segun opcionUsuario Hacer
    case 1:
        print("PIEDRA")
    case 2:
        print("PAPEL")
    case 3:
        print("TIJERAS")
    case _:
        print("Ingresa solo lo que te he pedido!!!!!!")
#endmatch

