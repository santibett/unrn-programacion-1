contraseña = "1245"
intentos = 3
contraseña_ingresada= input("contraseña : ")

if contraseña_ingresada == contraseña:
    print ("acceso permitido")
else:
    while intentos > 0 and contraseña_ingresada != contraseña:
        print (f"contraseña incorrecta, te quedan {intentos} intentos")
        intentos -= 1 
        contraseña_ingresada = input("vuelve a intenar la contraseña: ")
        if contraseña_ingresada == contraseña:
               print("acceso permitido")
        break
    
    else:
        print("te quedaste sin intentos")


def entrada (documento, edad, genero):
    if documento == True and edad >= 18 or genero == ("mujer"):
        print ("pasa gratis")
    elif genero != "mujer":
        print ("pasa")
    else:
        print ("no pasa")

entrada(True, 17, "hombre")
entrada(False, 23, "mujer")
entrada(True, 19, "mujer")

personas= ("pedro", "mateo", "juan")
for plato in range (1,7):
    if plato % 3 == 0:
        print(f"pedro lavo el plato numero {plato} ")
    elif plato == 1 or plato == 2:
            print(f"juan lavo el plato numero {plato}")
    else:
        print (f"mateo lavo el plato numero {plato}")
        

#ejericio 2

def dato (temperatura):
    if temperatura < 10:
        print("abrigate")
    elif temperatura >= 10 and temperatura <= 20:
        print("ropa media")
    else:
        print("ropa ligera")
dato(10)


numero = 13
if numero % 2 == 0:
    print ("numero par,")
    if numero < 10:
        print("y menor a 10")
    elif numero == 10:
        print("es 10")
    else:
        print("mayor que 10")

elif numero % 2 != 0: 
    print ("numero impar")
    if numero < 10:
        print("y menor a 10")
    elif numero == 10:
        print("es 10")
    else:
        print("mayor que 10")

monto = 900
es_cliente_vip = False
tiene_cupon = True

if monto > 1000 and es_cliente_vip or tiene_cupon:
    print("Se aplica descuento")
else:
    print("No hay descuento")

#imprime "se aplica descuento" ya que primero se evalua un "not" si hay, luego el "and" y por ultimo el "or"
#por lo tanto primero ve si el monto es mayor a 1000, lo cual toma como false y todo el and pasa a ser falso
#pero como despues evalua el or ques verdadero, el programa toma como verdadero todo, por eso imprime el primer print
#ejercicio 9
#Usar un forpara imprimir una tabla simple de multiplicar del 2.
for i in range (2,3):
    for j in range (1, 11):
        print (f"{i} x {j} = {i * j}")
        print()
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
for i in range(len(dias)):
    print (f"{i}: {dias[i]}")
