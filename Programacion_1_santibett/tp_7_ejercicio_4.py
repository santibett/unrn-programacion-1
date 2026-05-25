edad = input("escribe tu edad en numero, ej: 34 : ")
p = edad.strip()
if p.isnumeric():
    e = int(p)
    if 120 >= e >= 0:
        print(f"edad registrada: {e}")
    else:
        print("edad irreal")
else:
    print("error, escriba solo los numeros enteros")