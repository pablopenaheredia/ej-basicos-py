#Ejercicio 3: Área de un Triángulo
#Escribe un programa en Python que solicite al usuario que ingrese la base y la altura de un triángulo,
# y luego calcule y muestre el área del triángulo.

base = float(input("Ingrese la longitud de la base del triangulo: "))
altura = float(input("Ingrese la longitud de la altura del triangulo: "))

area = (base * altura)/2

print(f"El area del triangulo es {area}")