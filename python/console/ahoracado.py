import random

while True:
    def ahorcado(palabra):
        length = len(palabra)
        oculta = '_' * length

        # Muestra en pantalla la cantidad de caracteres que tiene la palabra
        def printOculta(texto):
            temp = ''
            for i in range(length):
                temp += texto[i] + ' '
            print(temp, ' (' + str(length) + ' letras)')

        printOculta(oculta)

        for i in range(length):
            if palabra[i] == ' ':
                oculta = oculta[0:i] + ' ' + oculta[i + 1:length]

        while oculta != palabra:
            letra = input('Dame una letra: ')

            for i in range(length):
                if palabra[i] == letra:
                    oculta = oculta[0:i] + letra + oculta[i + 1:length]

            printOculta(oculta)
        if oculta == palabra:
            print('Enhorabuena')

    palabras = ['cosa', 'teclado', 'perro']
    ahorcado(palabras[random.randint(0, len(palabras) - 1)])

    quit = input('Quit? (y/n)')
    if quit == 'y':
        print('bye.')
        break
