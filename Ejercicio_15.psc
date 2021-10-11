Algoritmo Invertir_num
	Escribir "Por favor, digite el numero que desea invertir aqui"
	Leer Num
	a = ConvertirATexto(Num)
	b = Longitud (a)
	X= ""
	Mientras b > 0 Hacer
		x=x + Subcadena(a,b,b)
		b = b - 1
	FinMientras
    Escribir "El numero" Num "invertido es" ConvertirANumero(x)
	
	
FinAlgoritmo
