# Muestra en pantalla la cantidad de caracteres que tiene la palabra
def printOculta(texto):
    temp = ''
    for i in range(len(texto)):
        temp += texto[i] + ' '
    print(temp, ' (' + str(len(texto)) + ' letras)')
