mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]
#(tipo_medicion, valor, ubicacion)
tipos_medicion = set()
ubicacion = set()
dicc = {}
for i in mediciones:
    ubicacion.add(i[2])
    tipos_medicion.add(i[0])
    if i[2] not in dicc:
        dicc[i[2]] = [f"{i[0]}: {i[1]}"]
    else:
        dicc[i[2]].append(f"{i[0]}: {i[1]}")

print(dicc)
print(tipos_medicion)
