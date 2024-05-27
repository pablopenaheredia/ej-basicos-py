#Contar letras: Crea una función que tome una cadena como entrada y devuelva un
#diccionario con el recuento de cada letra en la cadena.

def contarLetras(cadena):
    recuento = {}
    for letra in cadena:
        if letra in recuento:
            recuento[letra] += 1
        else:
            recuento[letra] = 1
    return recuento



def main():
    cadena = input("Ingrese una cadena de texto: ")
    print("El recuento es: ", contarLetras(cadena))

if __name__ == "__main__":
    main()