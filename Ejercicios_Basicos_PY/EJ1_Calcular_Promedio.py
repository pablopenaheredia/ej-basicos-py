'''Solicitamos al usuario que ingrese los números'''
numeros = input("Ingrese los números separados por espacios: ")

'''Convert cadena de texto a una lista de números'''
lista_numeros = list(map(float, numeros.split()))

'''promedio'''
promedio = sum(lista_numeros) / len(lista_numeros)

'''resultado'''
print("El promedio de los números ingresados es: ", promedio)
