# Importamos libreria
import statistics

# Creamos una lista vacía para almacenar los datos
datos = input("Ingrese los datos separados por comas: ")
#datos = [float(dato) for dato in datos.split(",")]
datos = [float(dato) if "." in dato else int(dato) for dato in datos.split(",")] #para que aparezca sin ,0 los enteros.
n = len(datos)

#media, mediana, primer y tercer cuartil, moda.
media = round(sum(datos) / n, 4) 
media = round(sum(datos) / n, 4) 
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
#Frec Absoluta
frec_abs = {}
for dato in datos:
    if dato in frec_abs:
        frec_abs[dato] += 1
    else:
        frec_abs[dato] = 1

#Frecuencia relativa:
frec_rel = {}
for k in frec_abs:
    frec_rel[k] = round(frec_abs[k] / n, 4)

#frec_rel = {k: round(v / n, 4) for k, v in frec_abs.items()}
#{k: round(v / n, 4) fo r k, v in frec_abs.items()}: Esta expresión es un diccionario por comprensión.
#.items(): Itera sobre los elementos del diccionario frec_abs. Cada elemento consiste en una clave (k) y su valor (v).
#v / n: Calcula la frecuencia relativa dividiendo el valor absoluto (v) por el tamaño total de la muestra (n).
#round(..., 4): Redondea el resultado a 4 decimales.
#{k: ...}: Crea un nuevo diccionario donde las claves son las mismas que en frec_abs, y los valores son las frecuencias relativas calculadas.

#Frecuencia porcentual
frec_porcentual = {k: round(v * 100, 2) for k, v in frec_rel.items()}

#Frecuencia absoluta acumulada
frec_abs_acum = {}
acum = 0
for k in frec_abs:
    acum += frec_abs[k]
    frec_abs_acum[k] = acum

#Frecuencia relativa acumulada
frec_rel_acum = {}
acum = 0
for k in frec_rel:
    acum += frec_rel[k]
    frec_rel_acum[k] = round(acum, 4)

#Frecuencia porcentual acumulada
frec_porcentual_acum = {k: round(v * 100, 2) for k, v in frec_rel_acum.items()}

# Imprimimos los resultados
#print(f"Datos ordenados: {datos}")
#print(f"Media: {media}")
#print(f"Mediana: {mediana}")
#print(f"Cuartil 1: {cuartil1}")
#print(f"Cuartil 3: {cuartil3}")
#print(f"Moda: {moda}")
#print(f"Frecuencia Absoluta: {frec_abs}")
#print(f"Frecuencia Absoluta Acumulada: {frec_abs_acum}")
#print(f"Frecuencia Relativa: {frec_rel}")
#print(f"Frecuencia Relativa Acumulada: {frec_rel_acum}")
#print(f"Frecuencia Porcentual: {frec_porcentual}")
#print(f"Frecuencia Porcentual Acumulada: {frec_porcentual_acum}")
#print(f"Desvío Estándar Muestral: {desvio_muestral}")   
#print(f"Desvío Estándar Poblacional: {desvio_poblacional}")

while True:
    print("Menú de opciones:")
    print("1. Media")
    print("2. Mediana")
    print("3. Cuartil 1")
    print("4. Cuartil 3")
    print("5. Moda")
    print("6. Frecuencia Absoluta")
    print("7. Frecuencia Absoluta Acumulada")
    print("8. Frecuencia Relativa")
    print("9. Frecuencia Relativa Acumulada")
    print("10. Frecuencia Porcentual")
    print("11. Frecuencia Porcentual Acumulada")
    print("12. Desvío Estándar Muestral")
    print("13. Desvío Estándar Poblacional")
    print("14. Salir")
    opciones = input("Ingrese los números de las opciones que desea, separados por comas: ").split(',')

    for opcion in opciones:
        if opcion == "1":
            print(f"Media: {media}")
        elif opcion == "2":
            print(f"Mediana: {mediana}")
        elif opcion == "3":
            print(f"Cuartil 1: {cuartil1}")
        elif opcion == "4":
            print(f"Cuartil 3: {cuartil3}")
        elif opcion == "5":
            print(f"Moda: {moda}")
        elif opcion == "6":
            print(f"Frecuencia Absoluta: {frec_abs}")
        elif opcion == "7":
            print(f"Frecuencia Absoluta Acumulada: {frec_abs_acum}")
        elif opcion == "8":
            print(f"Frecuencia Relativa: {frec_rel}")
        elif opcion == "9":
            print(f"Frecuencia Relativa Acumulada: {frec_rel_acum}")
        elif opcion == "10":
            print(f"Frecuencia Porcentual: ")
            for k, v in frec_porcentual.items():
                print(f"{k}:{v}%")
        elif opcion == "11":
            print(f"Frecuencia Porcentual Acumulada: ")
            for k, v in frec_porcentual_acum.items():
                print(f"{k}:{v}%")
        elif opcion == "12":
            print(f"Desvío Estándar Muestral: {desvio_muestral}")
        elif opcion == "13":
            print(f"Desvío Estándar Poblacional: {desvio_poblacional}")
        elif opcion == "14":
            print("Gracias por usar el programa")
            break
        else:
            print(f"Opción {opcion} no válida. Por favor, intente de nuevo.")

    otra_consulta = input("¿Desea realizar otra consulta? (si/no): ")
    if otra_consulta.lower() != 'si':
        print("Gracias por usar el programa.")
        break
