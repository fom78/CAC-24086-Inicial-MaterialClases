Algoritmo clase9_desafio2
	
	// Desaf�o 2: El valor m�s peque�o
	
	
	//Escribir un programa que pida al usuario n�meros positivos hasta que el
	//valor ingresado sea igual a cero.
	//Mostrar en la pantalla el valor m�s peque�o de todos los que se ingresaron
	//(sin considerar el cero que se ingres� para finalizar el bucle).
	
	
	continuar = Verdadero
	numeroMasPeque = 99999
	
	Mientras continuar  Hacer
		//Mientras nroIngresado != 0  Hacer
		Escribir "Dame un nro, positivo (cero para salir): "
		Leer nroIngresado // 5 8 4 9 5 0
		
		si nroIngresado <= 0 Entonces
			continuar = Falso
		SiNo
			// Evaluar el minimo
			si numeroMasPeque > nroIngresado Entonces
				numeroMasPeque = nroIngresado
			FinSi
		FinSi
		
		
	FinMientras
	
	Escribir "Numero menor: ", numeroMasPeque
	escribir "Fin del programa"
	
	
FinAlgoritmo
