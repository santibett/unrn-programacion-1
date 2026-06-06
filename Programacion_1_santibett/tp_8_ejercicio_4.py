a = open("temperaturas.txt", "r")
dicc = {}
for linea in a:
    linea = linea.strip()
    ciudad, temperatura = linea.split(";")
    if ciudad not in dicc:
        dicc[ciudad] = [temperatura]
    else: 
        dicc[ciudad].append(temperatura)
print(dicc)