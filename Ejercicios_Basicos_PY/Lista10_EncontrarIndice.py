#Encontrar índice: Escribe una función que reciba una lista y un valor, y devuelva el
#índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

def encontrarIndice(lista, valor):
    if valor in lista:
        return lista.index(valor)
    else:
        return -1

numeros = input("Ingrese una lista de numeros separados por comas: ")
lista = list(map(int, numeros.split(",")))
valor = int(input("Ingrese el valor para saber su indice (Debe estar en la lista ingresada previamente): "))
print(f"La lista es: {lista} y el valor es {valor}, El indice del valor agregado es: ", encontrarIndice(lista, valor))
