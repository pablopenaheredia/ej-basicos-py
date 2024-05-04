# Solicitar conversión
opcion = input("¿Desea convertir de grados Celsius a Fahrenheit (ingrese C) o de Fahrenheit a Celsius (ingrese F)? ")

#.upper se utiliza para convertir todos los caracteres en minúscula de una cadena a caracteres en mayúscula.
#Devuelve una nueva cadena con los caracteres convertidos, dejando la cadena original sin cambios.

if opcion.upper() == 'C': 
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("La temperatura en grados Fahrenheit es: ", fahrenheit)
elif opcion.upper() == 'F':
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("La temperatura en grados Celsius es: ", celsius)
else:
    print("Opción no válida.")

