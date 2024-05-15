# Importamos las librerías necesarias
import statistics
from collections import Counter

# Creamos una lista vacía para almacenar los datos
datos = input("Ingrese los datos separados por comas: ")
datos = [float(dato) for dato in datos.split(",")]
n = len(datos)

##frecuencia absoluta: cantidad de c/u de los num. queda que sea entero
#frecuencia relativa: similar al %, solo que entre 0 y 1. poner 4
#moda agregar string que da "la moda es:"
#desvio: formula rara"""

# Calculamos las medidas de posición y dispersión
media = statistics.mean(datos) # o sum(datos) / n
mediana = statistics.median(datos)
datos_inferiores = [n for n in datos if n < mediana]
datos_superiores = [n for n in datos if n > mediana]
cuartil1 = statistics.median(datos_inferiores)
cuartil3 = statistics.median(datos_superiores)
moda = statistics.mode(datos) #siempre da el num menor

"""Calculamos el desvío estándar muestral
desvio_estandar_m = statistics.stdev(datos)
desvio_estandar_p = statistics.pstdev(datos)

print(f"Desvío Estándar Muest: {desvio_estandar_m}")
print(f"Desvío Estándar Pob: {desvio_estandar_p}")

o

varianza_muestral = sum((xi - media) ** 2 for xi in datos) / (n - 1)
varianza_poblacional = sum((xi - media) ** 2 for xi in datos) / n

desvio_muestral = varianza_muestral ** 0.5
desvio_poblacional = varianza_poblacional ** 0.5

print(f"Desvío Estándar Muestral: {desvio_muestral}")
print(f"Desvío Estándar Poblacional: {desvio_poblacional}")
"""

# Imprimimos los resultados
datos.sort()
frec_abs = Counter(datos)
frec_rel = {k: v / n for k, v in frec_abs.items()}
print(f"Datos ordenados: {datos}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Cuartil 1: {cuartil1}")
print(f"Cuartil 3: {cuartil3}")
print(f"Frecuencia Absoluta: {frec_abs}")
print(f"Frecuencia Relativa: {frec_rel}")