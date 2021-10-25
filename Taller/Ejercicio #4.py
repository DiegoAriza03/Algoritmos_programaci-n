totalCompra = float(input("Digite el monto total de la compra: "))
inversionEmpresa = float
cantidadPrestadaBanco = float
cantidadPagadaFabricante = float
montoPagarIntereses = float(20)


if (totalCompra > 5000000):
  inversionEmpresa = (totalCompra * 55)/100
  cantidadPrestadaBanco = (totalCompra * 30)/100
  cantidadPagadaFabricante = (totalCompra * 15)/100
  print ("Cantidad prestada al banco : " , cantidadPrestadaBanco)
  
elif (totalCompra <= 5000000):
  inversionEmpresa = (totalCompra * 70)/100
  cantidadPagadaFabricante = (totalCompra * 30)/100
  montoPagarIntereses = (cantidadPagadaFabricante * 20)/100
  print ("Monto a pagar por intereses : " , montoPagarIntereses)
  


print ("Cantidad a invertir de los fondos de la empresa: " , inversionEmpresa)
print ("Cantidad pagada por el fabricante: " , cantidadPagadaFabricante)