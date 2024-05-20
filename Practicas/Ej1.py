#Ejercicio 1: Calculadora de Promedio
#scribe un programa en Python que solicite al usuario que ingrese tres números y luego calcule y muestre el promedio de esos números.


numeros = input("Ingrese los numeros separados por espacios:")

#usamos list, para luego conseguir el len
#map para convertir numeros en int, primer parametro es a lo que convertimos, y el segundo es lo ingresado
#.split Divide la cadena de texto en una lista de subcadenas
lista_numeros = list(map(float, numeros.split()))

prom = sum(lista_numeros) / len(lista_numeros)

print(f"El total de la suma es {sum(lista_numeros)} y su promedio es {prom}")
