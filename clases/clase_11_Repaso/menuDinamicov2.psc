Algoritmo menuDinamicov2
	
	continuar = Verdadero
	Mientras  continuar Hacer
		Limpiar Pantalla
		Escribir "Mi menu para jugar"
		Escribir "[1] Pipati modo infinito"
		Escribir "[2] Pipati modo campeonato"
		Escribir "[3] Adivina el numero "
		Escribir "[0] Salir"
		
		leer opcionDelMenu
		
		Segun opcionDelMenu Hacer
			1 :
				cVictoriasUsuario = 0
				respuesta = "s"
				cVictoriasCompu = 0
				jugadas = 0
				
				Mientras respuesta == "s" Hacer // "" == "s"
					
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
					Escribir "Desea seguir jugando ? (s/n)"
					leer respuesta
					
				FinMientras
				
				Escribir  "VOS ", cVictoriasUsuario, " PC ", cVictoriasCompu
				Escribir "Sobre ", jugadas, " partidas realizadas"
				
				
			2:
				
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
				
				
	
	
				
			3: 
				Escribir "Adivina el numero "
				numeroDePc = azar(10) // 8
				
				
				vidas = 3
				mientras vidas != 0 Hacer
					Escribir "Que numero es ? " Sin Saltar
					Leer numeroDeUsuario
					
					si numeroDePc == numeroDeUsuario Entonces
						Escribir "GANASTE!! Diste con el numero oculto!!!"
						vidas = 0
					SiNo
						vidas = vidas - 1
						
						si vidas == 0 Entonces
							Escribir "PERDISTE"
						FinSi
					FinSi
				
				FinMientras
				
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

