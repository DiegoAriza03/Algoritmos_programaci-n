A = float(input("Digite el valor de A: "))
B = float(input("Digite el valor de B: "))
C = float(input("Digite el valor de C: "))
D = float(input("Digite el valor de D: "))

if(D == 0):
  resultado = (A - C)**2
elif(D > 0):
  resultado = A - B
  resultado = resultado / D
  resultado = resultado ** 3

print (resultado)