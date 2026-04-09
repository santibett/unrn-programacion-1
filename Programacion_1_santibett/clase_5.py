def factorial(num:int) -> int:
    if num < 0:
        return 0
    elif num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)
#print(factorial())
def saludar (nombre):
    return f"hola {nombre}"

print(saludar("juan"))

def sumar(a, b):
    return a + b
resultado = sumar(1, 2)
print (resultado)

def trae_documento():
    return input("trae documento [si/no]: ") == "si"
def ingresar_edad():
    return int(input("ingresar edad: "))
def puede_pasar(documento, edad):
    return documento == True and edad >= 18
if puede_pasar(trae_documento(), ingresar_edad()):
    print ("puede pasar")
else:
    print("no puede pasar")

comida = ""
def pedir_comida():
    while comida == "":
        comida = input("pide una comida: ")
        return comida
#def obtener_precio(comida):