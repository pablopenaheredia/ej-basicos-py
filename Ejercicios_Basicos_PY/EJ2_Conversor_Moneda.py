#Ingresar cantidad en dolares
dolares = float(input("Ingrese la cantidad en dólares: "))

#Cambio
tipo_de_cambio = 0.85  # 1 dólar = 0.85 euros

#Convertimos la cantidad a euros
euros = dolares * tipo_de_cambio

#resultado
print(dolares, "dólares son equivalentes a", euros, "euros.")
