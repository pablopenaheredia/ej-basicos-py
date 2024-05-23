#Ejercicio 7: Juego de Adivinar el Número 
#Desarrolla un juego en el que el programa selecciona aleatoriamente un número
#entre 1 y 100 y el jugador debe adivinarlo.
#El programa debe proporcionar pistas al jugador si el 
#número ingresado es demasiado alto o demasiado bajo.
#El juego debe continuar hasta que el jugador adivine correctamente el número.

import random

numero_aleatorio = random.randint(1,100)

print("¡Bienvenido al juego de adivinar el número!")
print("Estoy pensando en un número entre 1 y 100...")

print("Ingrese el numero a adivinar debajo:")

while True:
    numero_usuario = int(input("Ingrese el numero a adivinar: "))

    if numero_aleatorio > numero_usuario:
        print("El numero que ingresaste es mayor. Intenta de nuevo")
    elif numero_aleatorio < numero_usuario:
        print("El numero que ingresaste es menor. Intenta de nuevo")
    if numero_usuario == numero_aleatorio:
        print("Felicidades, adivinaste el numero!")
        break