Algoritmo clase11_12_desafio1
	
	//Piedra, papel o tijera (versión 2)
	
	//Con lo aprendido hasta ahora podemos implementar una versión mejorada
	//del programa que escribimos para jugar a "piedra, papel o tijera".
	//La nueva versión debe correr hasta que el usuario decida que no quiere
	//continuar jugando (ingresando "s" o "n"). Además, debe contar cuantas
	//partidas gano el usuario y cuantas la computadora
	
	cVictoriasUsuario = 0
	respuesta = "s"
	cVictoriasCompu = 0
	jugadas = 0
	
	Mientras jugadas < 5 Hacer // "" == "s"
		
		// INICIO Logica del juego
		
		Escribir "Ingresa tu opcion (0 piedra - 1 papel - 2 tijeras)"
		leer opcionUsuario // 2
		
		opcionPC = azar(3)
		
		
		si opcionUsuario == opcionPC Entonces
			Escribir "Empataste"
		SiNo
			si opcionUsuario == 0 Entonces // Piedra
				// opcionPC puede ser: 1 o 2
				si opcionPC == 1 Entonces
					Escribir "Perdiste"
					cVictoriasCompu = cVictoriasCompu + 1
				SiNo
					Escribir "Ganaste"
					cVictoriasUsuario = cVictoriasUsuario + 1
				FinSi
			SiNo
				si opcionUsuario == 1 Entonces // Papel
					// pc es 0 o 2
					si opcionPC == 2 Entonces
						Escribir "Perdiste Tijeras mata papel"
						cVictoriasCompu = cVictoriasCompu + 1
					SiNo
						// es cero
						Escribir "Ganaste papel mata a piedra!!!!"
						cVictoriasUsuario = cVictoriasUsuario + 1
					FinSi
				SiNo
					// Si estoy aca el usuario elijio un 2
					si opcionPC == 1 Entonces
						Escribir "Ganaste me cortaste con la tijera"
						cVictoriasUsuario = cVictoriasUsuario + 1
					SiNo
						Escribir "Perdiste, chau!!"
						cVictoriasCompu = cVictoriasCompu + 1
					FinSi
					
				FinSi
			FinSi
		FinSi
		
		
		// FIN Logica del juego
		jugadas = jugadas + 1
		
	FinMientras
	
	Escribir  "VOS ", cVictoriasUsuario, " PC ", cVictoriasCompu
	Escribir "Sobre ", jugadas, " partidas realizadas"
	
	
	
	
	
FinAlgoritmo
