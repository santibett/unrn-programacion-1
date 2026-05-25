"""
lineas = [ 
    " AnA ;8;7;9",
    " JuAn ;4;5;3",
    " LucIA ;10;9;10"
]

for i in lineas:
    b = i.strip().split(";")
    nombre = b[0].capitalize()
    b.remove(b[0])
    a = " - ".join(b)

    print(f"Nombre: {nombre}, - Notas: {a}")

usuarios = [
    "ana,progranacion",
    "juan,matematica",
    "lucia,fisica"
]
for i in usuarios:
    a = i.split(",")
    nombre = a[0].capitalize()
    print(f"Hola {nombre}, estas inscripto/a en {a[1].capitalize()}")
def a(t):
    
    
a("pedro MARTINEZ sEgundo")

import random
def aleatorio():
    intentos = 6
    numero = random.randint(1, 100) 
    print (f"tenes {intentos} intentos")
    while intentos > 0:
        num = int(input("escribi un numero: "))
        if num > numero:
            print(f"🔽el numero es menor que {num}")
            intentos -= 1
            print(f"te quedan {intentos} intentos")
        elif num < numero:
            print(f"🔼el numero es mayor que {num}")
            intentos -= 1
            print(f"te quedan {intentos} intentos")
        else:
            print("ganaste")
            break
aleatorio()

numeros = [10,20,30,40,50,60]

print(numeros[:2])
print(numeros[-2:])
print(numeros[::2])
print(numeros[::-1])

p = "programacion"
print(p[:5])
print(p[-4:])
print(p[::-1])


def funcion(palabra):
    o = []
    p = ""
    for i in palabra:
        if i != " ":
            p += i
        else:
            o.append(p.strip(" "))
            p = " "
    o.append(p.strip(" "))
    palabras_invertidas = o[::-1]
    return " ".join(palabras_invertidas)

print(funcion("hola mundo python"))



a = input("nota parcial: ")
if a.isnumeric() and   0<= int(a) <= 10:
    print ("es valida")
else:
    print("no es valida")

lis = input("ingresa productos separados por coma: ")
if lis.count(",") >= 2 :
    a = lis.split(",")
    for i in a:
        if i.strip().isalpha():
            print("bien")
        else:
            print("mal")
else: 
    print("faltan productos o escribir con ,")

def patente():
    patente = input("ingrese su patente nueva (AA000AA): ")
    if len(patente) == 7 and patente[2:5].isnumeric() and patente[:2].isalpha() and patente[5:].isalpha():
        return(f"registrado correcta mente su patente {patente}")
    else: 
        return("ingrese bien su patente, sin espacios, 2 letras, 3 numeros y 2 letras")
    
print(patente())

def validar_float():
    f = input("dame un flotante: ")
    a = f.strip()
    n = False
    for i in range(len(a)):
        c = a[i]
        if c == ".":
            n = True
            return(f"{a}, numero flotante ingresado correctamente")
            
    if n == True:
        return(f"{a}, numero flotante ingresado correctamente")
    else: 
        return("no es flotante/racional")
        
print(validar_float())
"""
