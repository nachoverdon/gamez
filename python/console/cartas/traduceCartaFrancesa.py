from desglosaCarta import desglosaCarta
from traduceCarta import traduceCarta


def traduceCartaFrancesa(carta):
    palos = ['P', 'C', 'D', 'T']
    nombrePalos = ['Picas', 'Corazones', 'Diamantes', 'Tréboles']
    nombreNumeros = ['As', 'Jota', 'Reina', 'Rey']

    return traduceCarta(carta, palos, nombrePalos, nombreNumeros)


# def traduceCartaFrancesa(carta):
#     num, palo = desglosaCarta(carta)

#     if palo == 'P':
#         paloNombre = 'Picas'
#     elif palo == 'C':
#         paloNombre = 'Corazones'
#     elif palo == 'D':
#         paloNombre = 'Diamantes'
#     elif palo == 'T':
#         paloNombre = 'Tréboles'

#     if num == '1':
#         cartaNombre = 'As'
#     elif num == '10':
#         cartaNombre = 'Jota'
#     elif num == '11':
#         cartaNombre = 'Reina'
#     elif num == '12':
#         cartaNombre = 'Rey'
#     else:
#         cartaNombre = num

#     return cartaNombre + ' de ' + paloNombre
