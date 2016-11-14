def quitarTildes(palabra):
    sinTilde = []
    palabra = palabra.lower()
    for i in palabra:
        if i in ['á', 'à', 'â', 'ä']:
            sinTilde.append('a')
        elif i in ['é', 'è', 'ê', 'ë']:
            sinTilde.append('e')
        elif i in ['í', 'ì', 'î', 'ï']:
            sinTilde.append('i')
        elif i in ['ó', 'ò', 'ô', 'ö']:
            sinTilde.append('o')
        elif i in ['ú', 'ù', 'û', 'ü']:
            sinTilde.append('u')
        else:
            sinTilde.append(i)

    return ''.join(sinTilde)
