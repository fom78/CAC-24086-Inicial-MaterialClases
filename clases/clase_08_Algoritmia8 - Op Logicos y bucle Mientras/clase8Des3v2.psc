Algoritmo clase8Des3v2
	
	
	Escribir "Dame un nro: " Sin Saltar
	Leer nro1
	
	Escribir "Dame otro nro: " 
	Leer nro2
	// 6 -9
	nro1EsPositivo = nro1 >= 0
	nro2EsPositivo = nro2 >= 0
	
	//resultado = nro1EsPositivo Y nro2EsPositivo
	
	si (nro1EsPositivo Y nro2EsPositivo) == Verdadero Entonces
		Escribir "Ambos nros ingresados son positivos"
	SiNo
		Escribir "Al menos uno o ambos es negativo"
	FinSi
	//res = 2+9 < 3*9 // 11 < 27 
	
FinAlgoritmo
