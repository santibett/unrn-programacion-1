"""
registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]
st = set()
st_fecha = set()
for i in registros:
    st_fecha.add(i[0])
    st.add(i[1])
print(st)
print("___" * 10)
print(st_fecha)
print("___" * 10)
suma_temp = {}
ciudades = {}
for i in registros:
    ciudad = i[1]
    temperatura = i[2]
    if ciudad in suma_temp:
        suma_temp[ciudad] += temperatura
        ciudades[ciudad] += 1
    else:
        suma_temp[ciudad] = temperatura
        ciudades[ciudad] = 1
print(f"promedio por ciudad: ")
max = {"ciudad": "",
       "promedio": 0.0}
for i in suma_temp:
    promedio = suma_temp[i] / ciudades[i]
    print(f"{i} promedio es: {promedio:.2f} grados")
    if promedio > max["promedio"]:
        max["ciudad"] = i
        max["promedio"] = promedio
print("___" * 10)
c = max["ciudad"]
p = max["promedio"]
print(f"El mayor promedio lo tiene {c}con un promedio de {p}")
print("___" * 10)

inventario = {
    "cuaderno": {"precio": 2500, "stock": 4},
    "lapiz": {"precio": 800, "stock": 15},
    "goma": {"precio": 600, "stock": 2}
}
p = " "
for i in inventario:
    if inventario[i]["stock"] < 5:
        print(f"{i} tiene menos de 5 stock")
print("___" * 10)
total = 0
for i in inventario:
    total += inventario[i]["precio"] * inventario[i]["stock"]
print(f"el precio total del inventario es {total}")
productos_urgentes = set()
for i in inventario:
    if inventario[i]["stock"] <= 2:
        productos_urgentes.add(i)
        print(f"{productos_urgentes} necesita reposicion urgente")

libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Física para la ciencia y la tecnología", "Serway", 2010, "Ciencia")
]
for i in libros:
    if i[2] > 2010:
        print(f" ''{i[0]}'' de {i[1]} fue publicado luego de 2010")
l = set()
d = {}
for i in libros:
    l.add(i[3])
    if i[3] in d:
        d[i[3]] += 1
    else:
        d[i[3]] = 1
print(l)
print (d)
cantidad_max = 0
genero_max = []
for i in d:
    if d[i] >= cantidad_max:
        cantidad_max = d[i]
        genero_max.append(i)
print(f"la/s categoria/s con mas libros es/son {genero_max} con un total dde {cantidad_max} libros")

# primero hago un for de estudiantes, asigno promedio a la suma del i en "notas" sobre la cantidad de notas, e imprimo el promedio por estudiante
# con el mismo for, clasifico i por su promedio, si es >= 8  y sus asistencias >= 8 promociona y asi con los otros casos
# para ver cuantos estudiantes hay por categoria, creo 2 listas (c1 y c2) y ahi con un for de estudiantes los añado a la lista segun su i "comision"
# para el promedio por comision creo prom 1 y prom 2, y sumo el promedio de los que vayam a esa comision y luego divido por la cantidad
# para los estudiantes que recursan, creo un set y uso el for donde saque su promedio, y a los que desaprueban los agrego al set

estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6], "asistencias": 9, "comision": "C1"},
    {"nombre": "Luis", "notas": [4, 5, 3], "asistencias": 6, "comision": "C1"},
    {"nombre": "Mora", "notas": [9, 8, 10], "asistencias": 10, "comision": "C2"},
    {"nombre": "Pedro", "notas": [2, 4, 3], "asistencias": 7, "comision": "C2"}
]
recursantes= set()
for i in estudiantes:
    promedio = sum(i["notas"])/ len(i["notas"])
    asistencias = i["asistencias"]
    print(f"{i["nombre"]} tiene un promedio de {promedio} ")
    if promedio >= 8 and asistencias >= 8:
        print(f"{i['nombre']} promociona")
    elif promedio >= 4 and asistencias >= 6:
        print(f"{i['nombre']} regulariza")
    else:
        recursantes.add(i["nombre"])
        print(f"{i['nombre']} recursa")

c1 = []
pr_1 = 0
c2 = []
pr_2 = 0
for i in estudiantes:
    if i["comision"] == "C1":
        c1.append(i["nombre"])
        pr_1 += sum(i["notas"]) / len(i["notas"])
    else:
        c2.append(i["nombre"])
        pr_2 += sum(i["notas"]) / len(i["notas"])
print(f"hay {len(c1)} alumnos en la comision 1")
print(f"hay {len(c2)} alumnos en la comision 2")
if pr_1 > pr_2:
    print(f"el mejor promedio lo tiene C1: {pr_1 / len(c1)}")
else:
    print(f"el mejor promedio lo tiene C2: {pr_2 / len(c2)}")
print(f"los recursantes son {recursantes}")
"""

libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("1984", "George Orwell", 1949, "Novela"),
    ("Rayuela", "Julio Cortázar", 1963, "Novela"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Armas, gérmenes y acero", "Jared Diamond", 1997, "Historia"),
    ("Historia mínima de América Latina", "Carlos Malamud", 2014, "Historia"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Cosmos", "Carl Sagan", 1980, "Ciencia"),
    ("Una breve historia del tiempo", "Stephen Hawking", 1988, "Ciencia"),
    ("El arte de la guerra", "Sun Tzu", -500, "Estrategia"),
    ("Pensar rápido, pensar despacio", "Daniel Kahneman", 2011, "Psicología")
]

#primero creo un set y hago un for de libros para agregar cada genero al set y que no se repitan
#pido al usuario un genero con input y .capitalize(), si es genero esta en el set que cree, se ejecuta
#un titulo de "los libros del genero son:" y abajo con un for de libros, los que tengan i[3] igual al input, se imprimen
#y si no estan en el set, le mando que no tenemos ningun libro
#para repetirlo uso un while true, y si el usuario quiere irse escribe salir, entonces agrego un elif input == "Salir" break
lib_disp = set()
for i in libros:
    lib_disp.add(i[3])
print(lib_disp)
while True:
    print("escriba salir para finalizar")
    genero = input("elige un genero de los mencionados: ").capitalize()
    if genero == "Salir":
        print("saliendo...")
        break
    elif genero in lib_disp:
        print(f"los titulos de ese genero son:")
        for i in libros:
            if i[3] == genero:
             print({i[0]})
    else:
        print("no existe ese genero en los libros")

