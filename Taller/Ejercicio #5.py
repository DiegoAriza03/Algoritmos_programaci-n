salario = float(input("Digite el salario de los vendedores: "))

departamento1 = float(input("Digite la venta del departamento 1: "))
departamento2 = float(input("Digite la venta del departamento 2: "))
departamento3 = float(input("Digite la venta del departamento 3: "))

ventaTotal = float

porcentajeDepartamento1 = float
porcentajeDepartamento2 = float
porcentajeDepartamento3 = float

salarioDepartamento1 = float
salarioDepartamento2 = float
salarioDepartamento3 = float

ventaTotal = departamento1 + departamento2 + departamento3

porcentajeDepartamento1 = departamento1 / ventaTotal * 100
porcentajeDepartamento2 = departamento2 / ventaTotal * 100
porcentajeDepartamento3 = departamento3 / ventaTotal * 100

if (porcentajeDepartamento1 > 33 and porcentajeDepartamento2 > 33):
  salarioDepartamento1 = (salario * 20) / 100
  salarioDepartamento1 = salarioDepartamento1 + salario
  salarioDepartamento2 = (salario * 20) / 100
  salarioDepartamento2 = salarioDepartamento2 + salario
  salarioDepartamento3 = salario

elif (porcentajeDepartamento1 > 33 and porcentajeDepartamento3 > 33):
  salarioDepartamento1 = (salario * 20) / 100
  salarioDepartamento1 = salarioDepartamento1 + salario
  salarioDepartamento3 = (salario * 20) / 100
  salarioDepartamento3 = salarioDepartamento3 + salario
  salarioDepartamento2 = salario

elif (porcentajeDepartamento2 > 33 and porcentajeDepartamento3 > 33):
  salarioDepartamento2 = (salario * 20) / 100
  salarioDepartamento2 = salarioDepartamento2 + salario
  salarioDepartamento3 = (salario * 20) / 100
  salarioDepartamento3 = salarioDepartamento3 + salario
  salarioDepartamento1 = salario

elif (porcentajeDepartamento1 > 33):
  salarioDepartamento1 = (salario * 20) / 100
  salarioDepartamento1 = salarioDepartamento1 + salario
  salarioDepartamento2 = salario
  salarioDepartamento3 = salario

elif (porcentajeDepartamento2 > 33):
  salarioDepartamento2 = (salario * 20) / 100
  salarioDepartamento2 = salarioDepartamento2 + salario
  salarioDepartamento1 = salario
  salarioDepartamento3 = salario

elif (porcentajeDepartamento3 > 33):
  salarioDepartamento3 = (salario * 20) / 100
  salarioDepartamento3 = salarioDepartamento3 + salario
  salarioDepartamento1 = salario
  salarioDepartamento2 = salario

print ("Salario departamento 1: " , salarioDepartamento1)
print ("Salario departamento 2: " , salarioDepartamento2)
print ("Salario departamento 3: " , salarioDepartamento3)