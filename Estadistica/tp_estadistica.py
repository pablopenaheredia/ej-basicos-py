import statistics  # Importa el módulo statistics para realizar cálculos estadísticos.

def convertir_datos(datos):
    datos_lista = datos.split(",")  # Divide la cadena en una lista donde cada elemento es se separa por una coma.
    datos_convertidos = []  #Definimos una lista vacia donde se van a guardar los datos.
    for dato in datos_lista: #Ciclo for para que itere sobre cada dato en la lista de datos ingresados en linea 1.
        if "." in dato:  # Si el dato contiene un punto, es se considera decimal.
            datos_convertidos.append(float(dato))  # Convierte a float y lo agrega a la lista.
        else:
            datos_convertidos.append(int(dato))  # Si no, convierte a entero y lo agrega a la lista.
    return datos_convertidos  # Retorna la lista de datos ya convertidos como una lista nueva.

def calcular_estadisticas(datos):
    n = len(datos)  # Calcula cantidad de datos.
    media = round(sum(datos) / n, 4)  # Calcula la media con 4 decimales.
    mediana = round(statistics.median(datos), 4)  # Calcula la mediana con 4 decimales.
    '''if n % 2 == 0: 
        indice_1 = n // 2  #Redondea hacia arriba   
        indice_2 = indice_1 - 1
        mediana = (datos_ordenados[indice_1] + datos_ordenados[indice_2]) / 2
    else: 
        indice = n // 2
        mediana = datos_ordenados[indice]'''
    
    datos_inferiores = [n for n in datos if n < mediana]  # Filtra los datos inferiores a la mediana. donde la primera n significa que es lo que se va a agregar (append).
    '''for n in datos: 
        if n < mediana: 
        datos_inferiores.append(n)'''
    datos_superiores = [n for n in datos if n > mediana]  # Filtra los datos superiores a la mediana. igual a inferior.
    cuartil1 = round(statistics.median(datos_inferiores), 4)  # Calcula el primer cuartil con 4 decimales.
    cuartil3 = round(statistics.median(datos_superiores), 4)  # Calcula el tercer cuartil con 4 decimales.
    moda = statistics.multimode(datos)  # Calcula la moda.
    '''def calcular_moda(datos):
    frecuencia = {} 
    for dato in datos:
        if dato in frecuencia:
            frecuencia[dato] += 1
        else:
            frecuencia[dato] = 1

    #frecuencia más alta
    moda_frecuencia = max(frecuencia.values())

modas = []  Lista para almacenar las modas
for dato, freq in frecuencia.items():  # Recorremos el diccionario de frecuencias
    if freq == moda_frecuencia:  
        modas.append(dato)   Añadimos el elemento a la lista de modas

    return modas'''
    varianza_muestral = sum((xi - media) ** 2 for xi in datos) / (n - 1)  # Calcula la varianza muestral.
    varianza_poblacional = sum((xi - media) ** 2 for xi in datos) / n  # Calcula la varianza poblacional.
    desvio_muestral = round(varianza_muestral ** 0.5, 4)  # Calcula el desvío estándar muestral con 4 decimales.
    desvio_poblacional = round(varianza_poblacional ** 0.5, 4)  # Calcula el desvío estándar poblacional con 4 decimales.
    return media, mediana, cuartil1, cuartil3, moda, desvio_muestral, desvio_poblacional  # Retorna cada calculo previo.

def calcular_frecuencias(datos):
    n = len(datos) 
    datos.sort()  #Ordena los datos.

#Frecuencia Absoluta:
#Número de veces en que aparece repetido un mismo valor de la variable
    frec_abs = {}  #Definimos un diccionario vacio para la frecuencia absoluta.
    for dato in datos:
        if dato in frec_abs:
            frec_abs[dato] += 1  # Incrementa el contador si el dato esta en el diccionario.
        else:
            frec_abs[dato] = 1  # Inicializa el contador si el dato no está en el diccionario.

#Frecuencia Relativa:
#Es el cociente entre su frecuencia absoluta y la suma de todas las frecuencias absolutas.
    frec_rel = {}
    for k, v in frec_abs.items():
        frec_rel[k] = round(v / n, 4)  # Calcula la frecuencia relativa.

#Frecuencia porcentual
#Es igual a la frecuencia relativa multiplicada por 100. 
#Expresa el porcentaje que el valor de una variable tiene en el total de observaciones.
    frec_porcentual = {}
    for k, v in frec_rel.items():
        frec_porcentual[k] = round(v * 100, 2) # Calcula la frecuencia porcentual.

#Frecuencia absoluta acumulada
#Se obtiene sumando todas las frecuencias absolutas de las variables que le anteceden más la frecuencia absoluta de dicha variable.
    frec_abs_acum = {}  #Definimos un diccionario vacio para la frecuencia absoluta acumulada.
    contador = 0
    for k in frec_abs:
        contador += frec_abs[k]  # Acumula las frecuencias absolutas.
        frec_abs_acum[k] = contador  # Asigna la frecuencia acumulada al dato.

#Frecuencia relativa acumulada
#Se obtiene sumando todas las frecuencias relativas que la anteceden más la frecuencia relativa de dicha variable.
    frec_rel_acum = {}  #Definimos un diccionario vacio para la frecuencia relativa acumulada.
    contador = 0
    for k in frec_rel:
        contador += frec_rel[k]  # Acumula las frecuencias relativas.
        frec_rel_acum[k] = round(contador, 4)  # Asigna la frecuencia relativa acumulada al dato.

#Frecuencia porcentual acumulada
#Se obtiene sumando todas las frecuencias porcentuales de las variables que la anteceden
#más la frecuencia porcentual de dicha variable.

    frec_porcentual_acum = {}
    for k, v in frec_rel_acum.items():
        frec_porcentual_acum[k] = round(v * 100, 2) # Calcula la frecuencia porcentual acumulada.
    
    return frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum  # Retorna todas las frecuencias calculadas.

def mostrar_menu():
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
    print("0. Salir")


def obtener_datos():
    datos_entrada = input("Ingrese los datos separados por comas: ")
    return convertir_datos(datos_entrada)


def main():
    datos_entrada = input("Ingrese los datos separados por comas: ")  # Pide al usuario que ingrese los datos.
    datos = convertir_datos(datos_entrada)  # Convierte los datos ingresados a una lista de numeros enteros y/o floats.
    media, mediana, cuartil1, cuartil3, moda, desvio_muestral, desvio_poblacional = calcular_estadisticas(datos)  # Calcula las estadísticas.
    frec_abs, frec_rel, frec_porcentual, frec_abs_acum, frec_rel_acum, frec_porcentual_acum = calcular_frecuencias(datos)  # Calcula las frecuencias.
    
    while True:
        mostrar_menu()  # Muestra el menú de opciones.
        opciones = input("Ingrese los números de las opciones que desea, separados por comas: ").split(',')  # Pide al usuario que ingrese las opciones deseadas.
        for opcion in opciones:
            if opcion == "1":
                print(f"Media: {media}")  # Muestra la media.
            elif opcion == "2":
                print(f"Mediana: {mediana}")  # Muestra la mediana.
            elif opcion == "3":
                print(f"Cuartil 1: {cuartil1}")  # Muestra el primer cuartil.
            elif opcion == "4":
                print(f"Cuartil 3: {cuartil3}")  # Muestra el tercer cuartil.
            elif opcion == "5":
                print(f"Moda: {moda}")  # Muestra la moda.
            elif opcion == "6":
                print(f"Frecuencia Absoluta: {frec_abs}")  # Muestra la frecuencia absoluta.
            elif opcion == "7":
                print(f"Frecuencia Absoluta Acumulada: {frec_abs_acum}")  # Muestra la frecuencia absoluta acumulada.
            elif opcion == "8":
                print(f"Frecuencia Relativa: {frec_rel}")  # Muestra la frecuencia relativa.
            elif opcion == "9":
                print(f"Frecuencia Relativa Acumulada: {frec_rel_acum}")  # Muestra la frecuencia relativa acumulada.
            elif opcion == "10":
                print("Frecuencia Porcentual: ")
                for k, v in frec_porcentual.items():
                    print(f"{k}: {v}%")  # Muestra la frecuencia porcentual.
            elif opcion == "11":
                print("Frecuencia Porcentual Acumulada: ")
                for k, v in frec_porcentual_acum.items():
                    print(f"{k}: {v}%")  # Muestra la frecuencia porcentual acumulada.
            elif opcion == "12":
                print(f"Desvío Estándar Muestral: {desvio_muestral}")  # Muestra el desvío estándar muestral.
            elif opcion == "13":
                print(f"Desvío Estándar Poblacional: {desvio_poblacional}")  # Muestra el desvío estándar poblacional.
            elif opcion == "0":
                print("Gracias por usar el programa")  # Mensaje de despedida.
                return  # Termina la ejecución del programa.
            else:
                print(f"Opción {opcion} no válida. Por favor, intente de nuevo.")  # Mensaje de error si la opción no es válida.

        otra_consulta = input("¿Desea realizar otra consulta? (si/no): ")  # Pregunta al usuario si desea realizar otra consulta.
        if otra_consulta.lower() != 'si':
            print("Gracias por usar el programa.")
            break

if __name__ == "__main__":
    main()