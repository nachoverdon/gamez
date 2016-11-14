from random import randint


def desordenarLista(lista):
    lista2 = []

    for i in range(len(lista)):
        pos = randint(0, len(lista) - 1)
        num = lista.pop(pos)
        lista2.append(num)

    return lista2
