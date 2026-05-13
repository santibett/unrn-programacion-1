"""
materia = ("programacion 1", 3, "miercoles")
print(materia[0])
print(materia[1])
print(materia[2])
a, b, c = materia
print(a)
print(b)
print(c)

numeros = (4, 7, 2, 9, 7)
print(numeros[0])
print(numeros[-1])
veces = 0
for i in numeros:
    if i == 7:
        veces +=1
print(veces)
print(len(numeros))

valores = [3, 3, 5, 7, 5, 8, 8, 8, 10]
print(set(valores))
print(len(set(valores)))

materias = {"Matemática", "Programación"}
materias.add("fisica")
print(materias)
if "quimica" in materias:
    print("quimica esta en las materias")
else:
    print("quimica no esta en las materias")

alumno = {"nombre": "santi",
          "apellido":"bettoli" ,
          "edad": 18}
print(alumno["nombre"], alumno["apellido"])
alumno["edad"] += 1
print(alumno["edad"])
alumno["activo"] = True
print(alumno)
"""
producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}
for i in producto:
    print(producto[i])
for j in producto.keys():
    print(j)
for h in producto:
    print(f"{h} : {producto[h]}")