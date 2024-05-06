Algoritmo frutaspdf9desafio1
	
	//Escribir un programa que pida al usuario nombre de frutas. Aceptar
	//únicamente los valores "manzana", "pera", "pomelo" o "naranja".
	//Si se ingresa otro valor, indicar el error y solicitar un nuevo valor.
	//Si se ingresa la palabra "fin" terminar el programa.
	
	
	bandera = Verdadero
	mientras bandera Hacer // hacer con el control de fruta distinto a fin
		Escribir "Dame nombres de frutas (fin para terminar la carga) "
		leer fruta
		
		
		si fruta == "pomelo" O  fruta == "pera" O fruta == "manzana" O fruta == "naranja" Entonces
			Escribir "Fruta aceptada"
		sino 
			si fruta == "fin" Entonces
				bandera = Falso
			SiNo
				Escribir "Error"
			FinSi
			
		FinSi
	FinMientras
	
	
	
	
	
	
	
	
FinAlgoritmo
