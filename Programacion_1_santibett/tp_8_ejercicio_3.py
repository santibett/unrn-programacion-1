d = []
while len(d) < 4:
    i = input("nombre: ").strip()
    if i.isalpha and i != "":
        d.append(i)
archivo = open("alumnos.txt", "w")
for i in d:
    archivo.write(f"{i} \n")
archivo.close()