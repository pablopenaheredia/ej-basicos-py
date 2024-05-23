#Ejercicio 6: Validación de Contraseña 
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. 
#La contraseña debe cumplir con los siguientes requisitos:
#Debe tener al menos 8 caracteres de longitud.
#Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
#El programa debe informar al usuario si la contraseña es válida o no.

import re

contraseña = input("Ingrese la contraseña a validar: ")

if len(contraseña) >= 8:
    mayusculas = re.search('[A-Z]', contraseña)
    minuscula = re.search('[a-z]', contraseña)
    numeros = re.search('[0-9]', contraseña)
    especiales = re.search('[!"·$%&/()=?¿|@#~€¬_,;:.]', contraseña)

    if mayusculas and minuscula and numeros and especiales:
        print("La contraseña es válida")

    else:
        print("La contraseña es invalida.")