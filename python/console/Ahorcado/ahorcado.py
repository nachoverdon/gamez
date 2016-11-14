from dibujarSoga import dibujarSoga
from seleccionarPalabra import seleccionarPalabra
from quitarTildes import quitarTildes
from printOculta import printOculta
from devuelvePosiciones import devuelvePosiciones

while True:
    def ahorcado(palabra):
        length = len(palabra)
        oculta = '_' * length
        intento = 0
        acierto = False

        dibujarSoga(intento)
        printOculta(oculta)

        for i in range(length):
            if palabra[i] == ' ':
                oculta = oculta[0:i] + ' ' + oculta[i + 1:length]

        while oculta != palabra and intento < 6:

            letra = input('Dame una letra: ')

            pos = devuelvePosiciones(palabra, letra)
            for i in pos:
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
            dibujarSoga(-1)
            print('Enhorabuena, has ganado. La palabra secreta era:', palabra)

    palabra = seleccionarPalabra()
    ahorcado(quitarTildes(palabra))

    quit = input('Quit? (y/n)')
    if quit == 'y':
        print('bye.')
        break
