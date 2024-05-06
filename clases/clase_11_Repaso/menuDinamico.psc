Algoritmo menuDinamico
	
	continuar = Verdadero
	Mientras  continuar Hacer
		Limpiar Pantalla
		Escribir "Mi menu para jugar"
		Escribir "[1] Pipati modo infinito"
		Escribir "[2] Pipati modo campeonato"
		Escribir "[3] Adivina el numero "
		Escribir "[0] Salir"
		
		leer opcionDelMenu
		
		//varia = "z"
		
		//segun varia Hacer
			//"amarillo": Escribir "hola"
			//"b": Escribir "hola!"
			//"z": Escribir "hola!!!!"
		//FinSegun
		
		Segun opcionDelMenu Hacer
			1 :
				Escribir "Pipati modo infinito!!!!"
			2:
				Escribir "pipati"

			3: 
				Escribir "Adivina el numero "
			0:
				Escribir "Hasta luego"
				continuar=Falso
			De Otro Modo:
				Escribir "Che, elegi una de las opciones validas"
		FinSegun
		
		Escribir "Presiona cualquier tecla para continuar ..." 
		Esperar Tecla
		
		
		
	FinMientras
	
	
	
	
	
	
	
	
FinAlgoritmo
