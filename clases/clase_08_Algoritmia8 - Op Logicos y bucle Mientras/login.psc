Algoritmo login
	
	
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
				
	FinSi
	
	si NO ingresoOK Entonces
		Escribir "Volve a intentar algo fallo"
	FinSi
	
	
	
	
FinAlgoritmo
