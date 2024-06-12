while True:
    
    try:
        nro1 = input("Numero 1: ")
        nro1 = int(nro1)

        nro2 = input("Numero 2: ")
        nro2 = int(nro2)

        resultado = nro1 / nro2
        break
    except ValueError:
        print("Hubo un error, ingresa solo enteros")

    except ZeroDivisionError:
        print("No se puede dividir por cero")



print(resultado)