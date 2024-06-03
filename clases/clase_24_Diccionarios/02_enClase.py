

# str secuencia de elementos (caracteres)
cadena= "2d,fKg,/&/(/) sdjsdfj"

# list secuencia de elementos (tipo dato)
varLista = [2,"sddfk",4,4.2,True]

# tuple secuencia de elementos (tipo dato)
(2,"sddfk",4,4.2,True)

print("ANTES",varLista)


varLista[4] = 8  # Modificando un valor // MUTANDO LA LISTA 
print("Despues",varLista)

varLista.pop()
varTupla =(2,"sddfk",4,4.2,True)

# var = list(varTupla)

print("TUPLA********")

# varTupla

# varTupla[4] = 8
print(varTupla)

cadena = "Hola"
cadena = cadena + " Clase!"

print(cadena)

# diccionario

# Son mutables y son desordenados

lista1 = [23]
empleado1 = {
    "nombre":"Fernado", 
    "edad":45,
    "profesion":"Docente"
    }

empleado2 = {
    "edad":18,
    "nombre":"Yoselin", 
    "profesion":"Cocinera",
    }

producto = {
    1: "Martillo",
    2: 3.45,
    3: 467
}

name = "Martillo"
producto = {
    "nombre": name,
    "precio": 3.45,
    "cantidad": 467
}

# producto = {
#     (34,"ffffff"): "Martillo",
#     True: 3.45,
#     3: 467
# }


empleado2["profesion"] = "Cheff"
print(empleado2["profesion"])

print("ANTES",empleado2)

empleado2["colorFavorito"] = "Rojo"
print("DESPUES",empleado2)

# emp2 = ["Yoselin",18,"Cocinera"]
# print(emp2[2])

