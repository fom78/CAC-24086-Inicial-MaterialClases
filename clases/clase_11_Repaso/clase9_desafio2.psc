Algoritmo clase9_desafio2
	
    // Desafío 2: El valor más pequeño
	
	
    //Escribir un programa que pida al usuario números positivos hasta que el
    //valor ingresado sea igual a cero.
    //Mostrar en la pantalla el valor más pequeño de todos los que se ingresaron
    //(sin considerar el cero que se ingresó para finalizar el bucle).
	
	
    continuar = Verdadero
    numeroMasPeque = 99999
    numeroMaximo = 0
    Mientras continuar  Hacer
        //Mientras nroIngresado != 0  Hacer
        Escribir "Dame un nro, positivo (cero para salir): "
        Leer nroIngresado // 5 8 4 9 5 0
		
        si nroIngresado == 0 Entonces
            continuar = Falso
        SiNo
            // Evaluar el minimo
            si numeroMasPeque > nroIngresado Entonces
                numeroMasPeque = nroIngresado
            FinSi
			
            si numeroMaximo < nroIngresado Entonces
                numeroMaximo = nroIngresado
            FinSi
        FinSi
		
		
    FinMientras
	
    Escribir "Numero menor: ", numeroMasPeque
    Escribir "El mayor: ", numeroMaximo
    escribir "Fin del programa"
	
	
FinAlgoritmo