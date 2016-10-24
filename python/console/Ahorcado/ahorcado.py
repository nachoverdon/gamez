import random
from dibujarSoga import dibujarSoga

while True:
    def ahorcado(palabra):
        length = len(palabra)
        oculta = '_' * length
        intento = 0
        acierto = False

        # Muestra en pantalla la cantidad de caracteres que tiene la palabra
        def printOculta(texto):
            temp = ''
            for i in range(length):
                temp += texto[i] + ' '
            print(temp, ' (' + str(length) + ' letras)')

        dibujarSoga(intento)
        printOculta(oculta)

        for i in range(length):
            if palabra[i] == ' ':
                oculta = oculta[0:i] + ' ' + oculta[i + 1:length]

        while oculta != palabra and intento < 6:

            letra = input('Dame una letra: ')

            for i in range(length):
                if palabra[i] == letra:
                    oculta = oculta[0:i] + letra + oculta[i + 1:length]
                    acierto = True

            if letra == palabra:
                oculta = palabra
                acierto = True

            if not acierto:
                intento += 1

            print('Fallos:', intento)
            dibujarSoga(intento)
            if intento < 6:
                printOculta(oculta)
            acierto = False

        if oculta == palabra and intento < 6:
            print('Enhorabuena, has ganado. La palabra secreta era:', palabra)

    palabras = ['cosa', 'teclado', 'perro']
    ahorcado(palabras[random.randint(0, len(palabras) - 1)])

    quit = input('Quit? (y/n)')
    if quit == 'y':
        print('bye.')
        break
