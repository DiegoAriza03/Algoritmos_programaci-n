frutas = open('frutas.txt', 'r')
numeros= open('numeros.txt','r')
lista_frutas=[]#Llenar las lista con los datos del archivo frutas.txt
lista_numeros=[]#Llenar las lista con los datos del archivo numeros.txt
for i in frutas:
  lista_frutas.append(i)
for i in numeros:
  lista_numeros.append(i)
#Realizar una funcion que elimine un caracter de todos los elementos de la lista
"""
Entradas:
lista-->list-->lista
elemento-->str-->elemento
Salidas
lista-->list-->lista
"""
def eliminar_un_caracter_de_toda_la_lista(lista:list,elemento:str)->list:
 auxiliar=[]
 for i in lista:
   a=i.replace(elemento,"")
   auxiliar.append(a)
 return auxiliar
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  print(lista_fruta_nueva)
"""

#Realizar una funcion que retorne la copia de una funcion que pasa por parametro 
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista
"""
def copia_lista(lista:list)->list:
  return lista.copy() 
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  print(lista_fruta_nueva)
"""

#Realizar una funcion que retorne una lista de numeros enteros   
"""
Entradas:
lista-->list-->lista
Salidas
lista-->lis-->lista
"""  
def numeros_enteros(lista:list):
  auxiliar=[]
  auxiliar_dos=[]
  for i in lista:
    auxiliar.append(float(i))
  for i in auxiliar:
    auxiliar_dos.append(int(i))
  return auxiliar_dos   
"""
if __name__ == "__main__":
  copia=copia_lista(lista_numeros)
  lista_nueva=eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print(numeros_enteros(lista_nueva))
"""

#Realizar una funcion que elimine un elemento de una lista
"""
Entradas:
listas-->list-->lista
elemento-->str-->elemento
Salidas
lista-->list-->lista
"""  
def elimina_elemento_lista(lista:list,elemento:str):
  lista.remove(elemento)
  return lista
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
 print(elimina_elemento_lista(lista_fruta_nueva,"Fresa"))
"""

#Retorna una lista con las palabras iniciales con la letra que pasa por parametro  
"""
Entradas:
lista-->list-->lista
elemento-->str-->lista
Salidas
lista-->list-->lista
"""  
def letra(lista:list,elemento:str)->list:
  auxiliar=[]
  for i in lista:
    if(i[0]=="G"):
      auxiliar.append(i)
  return auxiliar 
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  print(lista_fruta_nueva)
  lista_fruta_dos=letra(lista_fruta_nueva,"")
  print(lista_fruta_dos)
"""

#Realizar una funcion que retorne el tamaño de una lista   
"""
Entradas:
lista-->list-->lista
Salidas
tamaño-->int-->tamaño
"""   
def tamano_lista(lista:list)->list:
  auxiliar=[]
  for i in lista:
    print(len(lista))
  return auxiliar
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  print(lista_fruta_nueva)
  lista_fruta_dos=tamano_lista(lista_fruta_nueva)
  print(lista_fruta_dos)
"""

#Retorna el tamaño de la lista y que tipo de datos estan dentro de la lista
"""
Entradas:
lista-->list-->lista
Salidas
tamaño-->int-->tamaño
tipo de datos-->type-->tipo
"""  
def informacion_lista(lista:list)->list:
  auxiliar=[]
  for i in lista:
    print(len(lista))
  return auxiliar
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  print(lista_fruta_nueva)
  lista_fruta_dos=tamano_lista(lista_fruta_nueva)
  print(lista_fruta_dos)
  lista_fruta_dos=informacion_lista
  print(type(lista_fruta_nueva))
"""

#Retornar una lista con los numero negativos  
"""
Entradas:
lista-->list-->lista
Salidas
lista-->list-->lista
"""  
def numeros_negativos(lista):  
  auxiliar=[]
  for numeros in lista:
    if(float(numeros)<0):
      auxiliar.append(numeros)
  return auxiliar
"""
if __name__ == "__main__":
  copia=copia_lista(lista_numeros)
  lista_nueva=eliminar_un_caracter_de_toda_la_lista(copia,"\n")
  print(numeros_negativos(lista_nueva))
"""

#realizar una funcion que retorne la posicion de un elemento que pasa por parametro
def posicion_elemento(lista:list,elemento:str)->list:
  auxiliar = []
  for i in lista:
    if (str(i)) == str(elemento+("\n")):
      auxiliar.append(lista.index(i))
  return auxiliar
"""
if __name__ == "__main__":
  print(posicion_elemento (lista_frutas, "Mandarina"))
"""

#realizar una funcion que agregue al final de archivo frutas una fruta
def frutas(lista:list,elemento:str)->list:
  for i in lista_frutas:
    frutas.write("\n"+ elemento)
"""
print(frutas,"Aguacate")
"""

#Realizar una funcion que cuente el numero de veces que se repite un elemento 
def repetir(lista:list,elemento:str)->list:
  auxiliar=[]
  for i in lista:
    print(repetir(lista))
  return auxiliar
"""
if __name__ == "__main__":
  lista_fruta_nueva=eliminar_un_caracter_de_toda_la_lista(lista_frutas,"\n")
  lista_fruta_dos=tamano_lista(lista_fruta_nueva)
  print(lista_fruta_dos)
"""
