#Ejercicio 8: Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario. 
#La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de:
#letras (mayúsculas y minúsculas), números y caracteres especiales. El programa debe mostrar la contraseña generada al usuario.

import string
import random

caracteres_random = string.ascii_letters + string.digits + string.punctuation
contraseña_random = ""
longitud = 12
for i in range(longitud):
    contraseña_random += ''.join(random.choice(caracteres_random))
print(f"Su contraseña aleatoria es: {contraseña_random}")
