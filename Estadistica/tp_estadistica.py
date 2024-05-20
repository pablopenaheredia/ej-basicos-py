# Importamos libreria
import statistics

# Creamos una lista vacía para almacenar los datos
datos = input("Ingrese los datos separados por comas: ")
#datos = [float(dato) for dato in datos.split(",")]
datos = [float(dato) if "." in dato else int(dato) for dato in datos.split(",")] #para que aparezca sin ,0 los enteros.
n = len(datos)

#media, mediana, primer y tercer cuartil, moda.
media = round(sum(datos) / n, 4) # o 
mediana = round(statistics.median(datos), 4)
datos_inferiores = [n for n in datos if n < mediana]
datos_superiores = [n for n in datos if n > mediana]
cuartil1 = round(statistics.median(datos_inferiores), 4)
cuartil3 = round(statistics.median(datos_superiores), 4)
moda = statistics.multimode(datos)

#desvío estándar muestral y poblacional
varianza_muestral = sum((xi - media) ** 2 for xi in datos) / (n - 1)
varianza_poblacional = sum((xi - media) ** 2 for xi in datos) / n
desvio_muestral = round(varianza_muestral ** 0.5, 4)
desvio_poblacional = round(varianza_poblacional ** 0.5, 4)

#Frecuencias:
datos.sort()
frec_abs = {}
for dato in datos:
    if dato in frec_abs:
        frec_abs[dato] += 1
    else:
        frec_abs[dato] = 1

frec_rel = {}
for k in frec_abs:
    frec_rel[k] = round(frec_abs[k] / n, 4)
#frec_rel = {k: round(v / n, 4) for k, v in frec_abs.items()}
#{k: round(v / n, 4) fo r k, v in frec_abs.items()}: Esta expresión es un diccionario por comprensión. Veamos qué hace cada parte:
#.items(): Itera sobre los elementos del diccionario frec_abs. Cada elemento consiste en una clave (k) y su valor (v).
#v / n: Calcula la frecuencia relativa dividiendo el valor absoluto (v) por el tamaño total de la muestra (n).
#round(..., 4): Redondea el resultado a 4 decimales.
#{k: ...}: Crea un nuevo diccionario donde las claves son las mismas que en frec_abs, y los valores son las frecuencias relativas calculadas.

frec_porcentual = {k: round(v * 100, 2) for k, v in frec_rel.items()}

#Falta:
#Frecuencia absoluta acumulada: Se obtiene sumando todas las frecuencias absolutas de las variables que le anteceden más la frecuencia absoluta de dicha variable.
#Frecuencia relativa acumulada: Se obtiene sumando todas las frecuencias relativas que la anteceden más la frecuencia relativa de dicha variable.
#Frecuencia porcentual acumulada: Se obtiene sumando todas las frecuencias porcentuales de las variables que la anteceden más la frecuencia porcentual de dicha variable.

frec_abs_acum = {}
acum = 0
for k in frec_abs:
    acum += frec_abs[k]
    frec_abs_acum[k] = acum


frec_rel_acum = {}
acum = 0
for k in frec_rel:
    acum += frec_rel[k]
    frec_rel_acum[k] = round(acum, 4)


frec_porcentual_acum = {k: round(v * 100, 2) for k, v in frec_rel_acum.items()}

# Imprimimos los resultados
print(f"Datos ordenados: {datos}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Cuartil 1: {cuartil1}")
print(f"Cuartil 3: {cuartil3}")
print(f"Moda: {moda}")
print(f"Frecuencia Absoluta: {frec_abs}")
print(f"Frecuencia Absoluta Acumulada: {frec_abs_acum}")
print(f"Frecuencia Relativa: {frec_rel}")
print(f"Frecuencia Relativa Acumulada: {frec_rel_acum}")
print(f"Frecuencia Porcentual: {frec_porcentual}")
print(f"Frecuencia Porcentual Acumulada: {frec_porcentual_acum}")
print(f"Desvío Estándar Muestral: {desvio_muestral}")   
print(f"Desvío Estándar Poblacional: {desvio_poblacional}")