codigo = input("dame un codigo de materia, por ej PROG-101 :")
if codigo.count("-") == 1:
    a = codigo.strip()
    b = a.split("-")
    if b[0].isalpha() and b[-1].isnumeric():
        print(f"codigo válido: {a.upper()}")
    else:
        print("codigo invalido")
else:
    print("solo un gion") 