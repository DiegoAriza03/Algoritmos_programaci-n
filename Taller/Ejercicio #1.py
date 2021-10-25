depositoInicial = float(input("Digite su depósito inicial: "))
APY = float(input("Digite su tasa de interés anual: "))
interesObtenido = float
añosInvertir = float(input("digite sus años a invertir: "))

APY = APY/100

interesObtenido = depositoInicial * (1 + APY) ** añosInvertir

interesObtenido =  round(interesObtenido, 2)

print (interesObtenido)