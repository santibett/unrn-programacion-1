nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []
for i in nombres:
    n = i.strip().capitalize()
    nombres_normalizados.append(n)
print(nombres_normalizados)
