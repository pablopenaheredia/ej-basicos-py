#Ejercicio 2: Conversor de Moneda
#Desarrolla un programa en Python que convierta una cantidad de dinero de dólares estadounidenses a euros.
#El programa debe solicitar al usuario que ingrese la cantidad en dólares 
#y luego mostrar la cantidad equivalente en euros, utilizando un tipo de cambio fijo.

dolares = float(input("Ingrese el monto a convertir, debe ser en dolares: "))

cambio = 0.92

euros = dolares * cambio

print(f"Sus dolares son: {dolares}. El cambio actual es de {cambio}. El equivalente en euros es de {euros}")
