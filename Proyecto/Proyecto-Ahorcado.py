import random

escenario = \
    '''   
~~~~~~~~~|~
         |
 0123456 J    
~~~~~~~~~~~   
'''

simbolos = '>(º>°)<'


def bienvenida():
    print('*' * 45)
    print('juego del ahorcado cuando se complete la figura >(º>°)< habras perdido, Preparate')
    print('*' * 45)



def inicializar_juego(diccionario):
    palabra = random.choice(diccionario).lower()
    tablero = ['_'] * len(palabra)
    return tablero, palabra, []



def mostrar_escenario(errores):
    escena = escenario
    for i in range(0, len(simbolos)):
        simbolo = simbolos[i] if i < errores else ' '
        escena = escena.replace(str(i), simbolo)
    print(escena)



def mostrar_tablero(tablero, letras_erroneas):
    for casilla in tablero:
        print(casilla, end=' ')
    print()
    print()
    if len(letras_erroneas) > 0:
        print('Letras erróneas:', *letras_erroneas)
        print()



def pedir_letra(tablero, letras_erroneas):
    valida = False
    while not valida:
        letra = input('Introduce una letra (a-z): ').lower()
        valida = 'a' <= letra <= 'z' and len(letra) == 1
        if not valida:
            print('Error, la letra tiene que estar entre a y z.')
        else:
            valida = letra not in tablero + letras_erroneas
            if not valida:
                print('Letra repetida, Ingrese otra.')

    return letra



def procesar_letra(letra, palabra, tablero, letras_erroneas):
    if letra in palabra:
        print('La palabra si tiene esa letra')
        actualizar_tablero(letra, palabra, tablero)
    else:
        print('La Palabra no tiene esa letra')
        letras_erroneas.append(letra)



def actualizar_tablero(letra, palabra, tablero):
    for indice, letra_palabra in enumerate(palabra):
        if letra == letra_palabra:
            tablero[indice] = letra



def comprobar_palabra(tablero):
    return '_' not in tablero



def jugar_al_ahorcado(diccionario):

    tablero, palabra, letras_erroneas = inicializar_juego(diccionario)
    while len(letras_erroneas) < len(simbolos):
        mostrar_escenario(len(letras_erroneas))
        mostrar_tablero(tablero, letras_erroneas)
        letra = pedir_letra(tablero, letras_erroneas)
        procesar_letra(letra, palabra, tablero, letras_erroneas)
        if comprobar_palabra(tablero):
            print('Haz encontrado la palabra')
            break
    else:
        print(f'¡Has perdido! La palabra a adivinar era {palabra}.')
        mostrar_escenario(len(letras_erroneas))

    mostrar_tablero(tablero, letras_erroneas)


def jugar_otra_vez():
    return input('Quieres volver a jugar? introduce s para sí o cualquier otra letra para no')


def despedida():
    print('/' * 35)
    print('Gracias por jugar al ahorcado')
    print('/' * 35)


if __name__ == '__main__':

    diccionario = ['codigo', 'pescado', 'calamar', 'nota', 'facil']

    bienvenida()
    while True:
        jugar_al_ahorcado(diccionario)
        if jugar_otra_vez() != 's': break
    despedida()
