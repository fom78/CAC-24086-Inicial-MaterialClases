Algoritmo cajero
	
	Definir monto, montoARetirar, saldoAhora Como Real
	
	
	monto = 4000
	
	Escribir "Che tu monto actual es de: ",  monto , " pesos.-"
	
	Escribir "Cuanto deseas retirar ?"
	leer montoARetirar
	
	saldoAhora = monto - montoARetirar
	
	// Evaluar si el saldoAhora no es menor que cero
	si saldoAhora < 0 Entonces
		Escribir "Saldo insuficiente"
	SiNo
		Escribir "Che tu monto actual ahora es de: ", saldoAhora  , " pesos.-"
	FinSi
	
	
	
	
FinAlgoritmo
