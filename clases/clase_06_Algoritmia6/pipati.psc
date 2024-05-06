Algoritmo pipati
	
	
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
			SiNo
				Escribir "Ganaste"
			FinSi
		SiNo
			si opcionUsuario == 1 Entonces // Papel
				// pc es 0 o 2
				si opcionPC == 2 Entonces
					Escribir "Perdiste Tijeras mata papel"
				SiNo
					// es cero
					Escribir "Ganaste papel mata a piedra!!!!"
				FinSi
			SiNo
				// Si estoy aca el usuario elijio un 2
				si opcionPC == 1 Entonces
					Escribir "Ganaste me cortaste con la tijera"
				SiNo
					Escribir "Perdiste, chau!!"
				FinSi
				
			FinSi
		FinSi
	FinSi
	
	
	
	
	
FinAlgoritmo
