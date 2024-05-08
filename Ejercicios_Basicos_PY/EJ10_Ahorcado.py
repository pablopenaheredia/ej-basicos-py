palabras = ['python', 'ahorcado', 'juego', 'programacion', 'codigo']
palabra = palabras[0]  # Puedes cambiar esto para seleccionar una palabra aleatoria de la lista
adivinada = ['_'] * len(palabra)
intentos = 10

while intentos > 0 and '_' in adivinada:
    print(' '.join(adivinada))
    print('Intentos restantes:', intentos)
    letra = input('Ingresa una letra: ')

    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                adivinada[i] = letra
    else:
        intentos -= 1

if '_' in adivinada:
    print('¡Perdiste! La palabra era:', palabra)
else:
    print('¡Ganaste! La palabra era:', palabra)