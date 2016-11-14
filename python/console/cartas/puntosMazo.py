from desglosaCarta import desglosaCarta


def sacarPuntos(carta):
    num, palo = desglosaCarta(carta)

    if num == '1':
        puntos = 11
    elif num == '3':
        puntos = 10
    elif num == '12':
        puntos = 4
    elif num == '11':
        puntos = 3
    elif num == '10':
        puntos = 2
    else:
        puntos = 0

    return puntos
