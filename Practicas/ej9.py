#Ejercicio 9: Calculadora de Factorial 
#Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario.
#El factorial de un número entero positivo n se define como el producto
#de todos los enteros positivos menores o iguales a n. 
#El programa debe manejar números enteros grandes y mostrar el resultado.

factorial = int(input("Ingrese el numero que desee sacar el factorial: "))
resultado = 1

if factorial > 1 :
    for i in range(1, factorial+1):
        resultado *= i
    if factorial < 0:
        print("El factorial no se puede calcular para números negativos")
    elif factorial == 0: print("El factorial de 0 es 1.")

print(f"El factorial de {factorial}, es {resultado}")