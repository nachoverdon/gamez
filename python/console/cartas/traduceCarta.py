from desglosaCarta import desglosaCarta


def traduceCarta(carta, palos, nombresPalos, nombreNumeros):
    num, palo = desglosaCarta(carta)

    if palo == palos[0]:
        paloNombre = nombresPalos[0]
    elif palo == palos[1]:
        paloNombre = nombresPalos[1]
    elif palo == palos[2]:
        paloNombre = nombresPalos[2]
    elif palo == palos[3]:
        paloNombre = nombresPalos[3]

    if num == '1':
        cartaNombre = nombreNumeros[0]
    elif num == '10':
        cartaNombre = nombreNumeros[1]
    elif num == '11':
        cartaNombre = nombreNumeros[2]
    elif num == '12':
        cartaNombre = nombreNumeros[3]
    else:
        cartaNombre = num

    return cartaNombre + ' de ' + paloNombre
