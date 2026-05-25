"""

archivo = open("mis_datos.txt", "w")
archivo.write("hola, que tal\n")
archivo.write("hola, que talamos")
archivo.close()

#archivo = open("mis_datos.txt", "w")
archivo = open("lista_de_nombres.txt", "w")
for i in range(5):
    n = input("dame un nombre: ")
    archivo.write(f"{n}")
    if i != 4:
        archivo.write("\n")

archivo.close()
"""
archivo = open("registros.csv", "w")
for i in range(5):
    n = input("dame un nombre: ")
    j = input("dame el documento: ")
    archivo.write(f"{n} : {j}\n")
archivo.close()
