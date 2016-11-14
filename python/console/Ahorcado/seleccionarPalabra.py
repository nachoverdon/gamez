from random import randint


def seleccionarPalabra():
    lista = list(open('lista.txt'))
    name = lista[randint(0, len(lista))]
    name = name.replace('\n', '')

    return name
