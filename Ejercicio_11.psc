Algoritmo Nota_final
	Escribir "Señor estudiante, por favor ingrese el valor del parcial 1"
	Leer parcial1
	Escribir "Señor estudiante, por favor ingrese el valor del parcial 2"
	Leer parcial2
	Escribir "Señor estudiante, por favor ingrese el valor del parcial 3"
	Leer parcial3
	Promedioparciales <- (parcial1+parcial2+parcial3)/3;
	Escribir "Señor estudiante, este es el valor promedio de sus parciales es de" Promedioparciales
	Escribir "Ahora, por favor ingrese el valor de su examen final"
	Leer Examenfinal
	Escribir "Por ultimo, ingrese el valor de su examen final"
	Leer Trabajofinal
	Calificacionfinal <- Promedioparciales*0.55+Examenfinal*0.30+Trabajofinal*0.15
	Escribir "Señor estudiante, su calificacion final es" Calificacionfinal
FinAlgoritmo
