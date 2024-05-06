Algoritmo ej_acumulador
	
	
	nota= -1
	acumulador=0
	cantidadDeNotas=0
	Mientras  nota != 0 Hacer
		Escribir "Nota de estudiante (0 para salir): "
		Leer nota
		
		acumulador = acumulador + nota
		si nota != 0 Entonces
			cantidadDeNotas = cantidadDeNotas + 1
		FinSi
		
		
	FinMientras
	
	
	promedio = acumulador / cantidadDeNotas
	Escribir promedio
	
FinAlgoritmo
