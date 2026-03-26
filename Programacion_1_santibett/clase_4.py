for i in range (1, 11):
    for j in range (1, 11):
        print (f"{i} x {j} = {i*j}")
        if j == 10:
            print()

contraseña = "12345"
intentos = 3
contraseña_ingresada = input("contraseña: ")
if contraseña_ingresada == contraseña:
    print ("acceso permitido")
else:
    while intentos > 0 and contraseña_ingresada != contraseña:
        print (f"contraseña incorrecta, te quedan {intentos} intentos")
        intentos -= 1 
        contraseña_ingresada = input("vuelve a ingresar la contraseña: ")
        if contraseña_ingresada == contraseña:
                print("acceso permitido")
        elif intentos == 0:
                print("te quedaste sin intentos")

numero = -1
while numero < 0:
     numero = int(input("ingresar un numero valido: "))
print ("numero valido ingresado")

total = 0
opcion = "" 
pizza = 25
hamburguesa = 15
empanada = 20
carta = [pizza, hamburguesa, empanada]
menu = input("para ver el menú escriba carta: ")
if menu == "carta":
     print (carta)
print("selecciona la comida para llevar, para salir del programa escriba: terminar pedido ")
while opcion != "terminar pedido":
     opcion = input("escriba la comida que quieras agregar al pedido : "). lower()
     if opcion == "pizza":
          total += 25
          print (f"perfecto, agregamos una pizza {pizza}usd")
     elif opcion == "empanada":
        total += 20
        print (f"perfecto, agregamos una empanada {empanada}usd")
     elif opcion == "hamburguesa":
          total += 15
          print (f"perfecto, agregamos una hamburguesa{hamburguesa}usd")
     elif opcion == "terminar pedido" :
          print ("cerrando pedido")
     else:
          print (f"lo siento, no tenemos {opcion}, prueba con otra cosa")
print(f"pedido finalizado, el total es {total}")

lista_de_super = ["huevos", "pan" , "coca", "azucar", "leche", "fideos"]
print (type(lista_de_super))
lista_de_super2 = ["pizza", "empanada", "hamburguesa"]

for i in range (len(lista_de_super)):
     print (i)
     print (lista_de_super[i])
nombres = ["pedro", "juan", "gero","pedro", "juan", "gero"]
for i in range(len(nombres)):
     print (f"el plato numero {i} lo lava")
     print (nombres[i])
while True:
     indice_seleccionado = int(input("elegi la comida"))
     if indice_seleccionado < len(lista_de_super2):
          comida = lista_de_super2[indice_seleccionado]
          print(f"elegiste el indice {indice_seleccionado}: {comida}")
     else:
          print("elegiste una comida invalida")
#crea tu propio anotador de compras
#usa un while y una lista
#usa input para preguntar que agregar a la lista
#usar append par agregar elementos
#la lista solo puede tener 5 cisas
#cuando termine imprimi la lista y la cantidad de cosas en pantalla

anotador = []
agregado = ""
print("si quiere terminar la lista, ingrese: terminar lista")
while len(anotador) < 5 and agregado != "terminar lista":
     agregado = str(input("que comida quieres agregar a la compra? "))

     if agregado == "terminar lista":
          break

     anotador.append (str(agregado))
     print (f"perfecto, agregamos {agregado} a la lista")
     print()

if len(anotador) == 5:
     print("llegaste a la compra maxima permitida")
     print()

print(f"su lista quedó asi {anotador}")