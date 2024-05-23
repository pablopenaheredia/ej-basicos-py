#Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
#devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
#Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
#hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
#3 oportunidades.

def Login(usuario, contraseña)
    intentos = 0
    if usuario == "usuario1" and contraseña == "asdasd":
        return True
    else:
        intentos += 1
        return False

def validarIntentos(cantidad):
    if cantidad < 3:
        return True
    else:
        return False

def main():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    intentos = 0
    