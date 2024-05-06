Algoritmo primer_lectura
	
	Definir miNombre, miApellido, nombreCompleto Como Caracter
	Definir miEdad Como Entero
	
	// Instruccion para ingresar datos es Leer 
	Escribir "#################################"
	Escribir "Ingresa tu nombre"
	Leer miNombre
	
	
	Escribir "#################################"
	Escribir "Apellido?"
	Leer miApellido
	
	
	Escribir "#################################"
	Escribir "Edad?"
	Leer miEdad
	
	
	
	nombreCompleto = "Bienvenido/a " + miNombre + ", " + miApellido // Concatenacion
	Escribir "#################################"
	Escribir nombreCompleto
	
	
	edadALargoPlazo = miEdad + 32
	
	
	Escribir "Che, Tu edad en 32 años sera de: " , edadALargoPlazo
	
	
	
	
FinAlgoritmo
