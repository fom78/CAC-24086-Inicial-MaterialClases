Algoritmo horasExtras
	
	
	Escribir "Ctas horas trabajaste"
	Leer horasTrabajadas
	
	Escribir "Cto ganas por hora"
	Leer valorPorHora
	
	si horasTrabajadas <= 40 Entonces
		salario = valorPorHora * horasTrabajadas 
	SiNo
		horas_extras=horasTrabajadas-40
		valorEnExtras = horas_extras*valorPorHora*1.5
		salario = valorPorHora * 40 + valorEnExtras
	FinSi
	
	Escribir "Tu salario sera  de: ", salario
	
FinAlgoritmo
