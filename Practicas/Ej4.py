#Ejercicio 4: Contador de Palabras
#Desarrolla un programa en Python que solicite al usuario que
#ingrese una frase y luego cuente y muestre el número de palabras en esa frase.

palabras = input("Ingrese una frase: ")
#split hace que separa una cadena en cadenas. (una frase en palabras)
frase = len(palabras.split())

print(f"El numero de palabras de la frase es de {frase}")