#Sumar valores: Escribe una función que reciba un diccionario con valores numéricos y
#devuelva la suma de todos los valores.

def sumarValores(diccionario):
    suma = 0    
    for k, v in diccionario.items():
        for v in value:
            suma += v
        diccionariosumado[k] = suma

numeros = input("Ingrese una lista de numeros separados por comas: ")
lista = list(map(int, numeros.split(",")))
print(f"La suma de los valores de la lista es: ", sumarValores(lista))


#le falta