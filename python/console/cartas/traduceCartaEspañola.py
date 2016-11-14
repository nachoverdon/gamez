from desglosaCarta import desglosaCarta
from traduceCarta import traduceCarta


def traduceCartaEspalola(carta):
    palos = ['O', 'B', 'E', 'C']
    nombrePalos = ['Oros', 'Bastos', 'Espadas', 'Copas']
    nombreNumeros = ['As', 'Sota', 'Caballo', 'Rey']

    return traduceCarta(carta, palos, nombrePalos, nombreNumeros)


# def traduceCarta(carta):
#     num, palo = desglosaCarta(carta)

#     if palo == 'O':
#         paloNombre = 'Oros'
#     elif palo == 'B':
#         paloNombre = 'Bastos'
#     elif palo == 'E':
#         paloNombre = 'Espadas'
#     elif palo == 'C':
#         paloNombre = 'Copas'

#     if num == '1':
#         cartaNombre = 'As'
#     elif num == '10':
#         cartaNombre = 'Sota'
#     elif num == '11':
#         cartaNombre = 'Caballo'
#     elif num == '12':
#         cartaNombre = 'Rey'
#     else:
#         cartaNombre = num

#     return cartaNombre + ' de ' + paloNombre
