min = 42
seg = 42
seg_totales = (min * 60 + seg)

print (f"{seg_totales}, segundos"  )
'''
Definir una variable mensajecon el valor "Hola mundo!"y mostrarla por pantalla.
Definir las variables nombrey apellidoy mostrar el mensaje: "Bienvenido [nombre] [apellido] al mundo Python".
Cree un programa donde se defina una variable de cada uno de los siguientes tipos: str, inty float. Utilizar type()para imprimir, junto con su valor, el tipo de cada variable.
Cree un programa donde se asigne un valor a una variable de tipo inty otra de tipo float, sumarlas y mostrar el resultado, indicando también el tipo de dato del resultado.
Crear un programa que:
Calcule cuantos meses viviste aproximadamente.
Calcula tu edad dentro de 10 años.
Calcula el doble de tu altura.
Imprime los resultados con mensajes descriptivos.
Crear un programa que:
Cree una variable saludoque diga: "Hola <tu nombre>".
Cree otra variable que repita el saludo tres veces.
Cuente cuantas letras tiene tu nombre usando len().
'''
var="hola mundo"
print (var)
nombre= "santi"
apellido= "bettoli"
print (f"Bienvenido {nombre} {apellido} al mundo Python")


altura = 173
print (altura * 2)
print ("doble de tu altura en centimetros")
saludo = (f"Hola {nombre}")
print (saludo)
for i in range (3):
    print (saludo)

print(len(nombre))
