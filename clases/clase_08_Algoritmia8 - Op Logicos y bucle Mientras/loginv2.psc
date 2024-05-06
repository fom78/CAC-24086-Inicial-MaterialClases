Algoritmo loginv2
	
	
	nombreSecreto = "fom"
	claveSecreta = "1234"
	
	
	Escribir "Nombre de usuario: " Sin Saltar
	Leer nombreUsuario
	
	Escribir "Clave: " Sin Saltar
	Leer clave
	
	ingresoOK = Falso // Concepto de variable bandera
	
	Si nombreUsuario == nombreSecreto Y clave == claveSecreta Entonces
		ingresoOK = Verdadero
		Escribir "Tenes acceso al super sistema"
		
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
		
		
				
	FinSi
	
	si NO ingresoOK Entonces
		Escribir "Volve a intentar algo fallo"
	FinSi
	
	
	
	
FinAlgoritmo
