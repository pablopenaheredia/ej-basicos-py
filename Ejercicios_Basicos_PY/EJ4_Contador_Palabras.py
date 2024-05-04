#ingrese una frase
frase = input("Ingrese una frase: ")

#número de palabras en la frase, el metodo .split separa una cadena de texto por partes
num_palabras = len(frase.split())

#resultado
print("El número de palabras en la frase es: ", num_palabras)