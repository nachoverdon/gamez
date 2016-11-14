from desordenarLista import desordenarLista


def extrae5():
    lista1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    lista1 = desordenarLista(lista1)
    lista2 = []

    for i in range(5):
        num = lista1.pop()
        lista2.append(num)

    return lista2
