"""
Practicar la construccion de programas que usen:
Funciones propias
Parametros
return
Separacion del codigo en modulos
Reutilizacion de logica
"""
def saludar(nombre: int):
    return f"Hola {nombre}"
print(saludar("santi"))

def sumar (a, b):
    return a + b
print(sumar(3,5))

def es_par ( num: int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False
print(es_par(0))
print(es_par(13))

def calcular_descuento(precio: int):
    if precio > 10000:
        return precio * 0.90
    else:
        return precio
print (calcular_descuento(5))
print (calcular_descuento(30000))

def obtener_estado (nota: float):
    if nota >= 8.0:
        return "Promociona"
    elif nota < 8.0 and nota >= 6.0:
        return "aprueba"
    else:
        return "no aprueba"
print (obtener_estado (10))
print (obtener_estado (7.50))
print (obtener_estado (4.5))

from mensajes import despedir

despedir(input("a quien despides?  "))

comidas = []
menu = {
    "pizza" : 150,
    "hamburguesa" : 100,
    "milanesa" : 120
    }

total = 0
def precio_total ():
    return f"precio total es {total}"

def pedir():
    global total
    print (f"el menu es el siguiente: {menu}")
    comida = input("que comida quiere? ").lower()
    if comida in menu:
        comidas.append (comida)
        total += menu[comida]
        print(f"genial, se agregó {comida} a su lista")
        print(f"lleva un total de ${total} reales")
        return True
    elif comida == "fin":
        print (precio_total())
        return False 
    else:
        print("esa comida no está en el menu")
        return True

def pedido_de_comidas():
    while True:
        resultado = pedir()
        if resultado == False:
            break
        else:
            print("para salir escriba fin ")
pedido_de_comidas()

        


