"""
tupla
n = 1,3
t = (1, "santi")
def operaciones (a, b):
    return  (a + b, a - b, a / b)
suma, resta, division = operaciones(5, 10)
print(suma)
print(resta)
print(division)

def tup(nom, eda,):
    bol = False
    if eda >= 18:
        bol = True
    return (nom, eda, bol)
print(tup("santi", 18))
#set
n = {1,2,3,4,5,6,2,1,3,4}
print (n)
print(len(n))

#sets
a = {"ana", "juan", "pedro"}
b = {"juan", "lucia"}
print("Grupo A:", a)
print("Grupo B:", b)
#union: junta los elementos de ambos grupos
print("union:", a|b)
#intersección: muestra elementos en comun
print("interseccion:", a & b)
#diferencia: elementos en a pero no en b
print("diferencia A - B", a - b)

n = set(["Ana","juan","Ana", "pedro", "juan", "lucia"])
print(n)
print(len(n))

#diccionarios
#modificar
persoa = {"nombre" : "santi", "edad": 18}
persoa["edad"] = 21
#agregar
persoa ["ciudad"] = "bariloche"
print(persoa.keys())
print(persoa.values())
#recorrer clave y valor

#3
p = {"nombre": "martillo",
     "precio": 3000,
     "stock": 5}
print(p.items())
p["precio"] *= 1.10
p["stock"] -= 1
print(f"producto: {p['nombre']} - precio actualizado: {p["precio"]} - stock restante: {p["stock"]}")

alumno = {"nombre": "santi",
          "notas": [8, 9, 1],
          "ubicacion": ("bariloche", "rio negro"),
          "materias": {"matematica", "programacion", "ilea", "iie"}}
alumno["materias"].add ("ingles")
print(alumno["materias"])
alumnos = [{"nombre": "juan", "nota": 8},
           {"nombre": "santi" ,"nota": 4},
           {"nombre":"pepe" ,"nota": 2}]
alumnos.append({"nombre": "manu", "nota":10})
for i in alumnos:
    if i["nota"] >= 4:
        print(i["nombre"], "aprobo")
    else:
        print(i["nombre"], "desaprobo")
"""
alumnos = [ 
    {"nombre": "san" ,
            "notas": 8,
            "materias": {"programacion", "matematica"}},

           {"nombre":"juan" ,
            "notas": 3,
            "materias": {"programacion"}},

           {"nombre":"lucia" ,
            "notas": 9,
            "materias": {"programacion", "ingles"}}
           ]
for i in alumnos:
    print( i["nombre"])
print("-" * 30)
for i in alumnos:
    if i["notas"]>= 4:
        print(i["nombre"], "aprobó")
print("-" * 30)

for i in alumnos:
    if "matematica" in i["materias"]:
        print(i["nombre"], "cursa matematica")
print("-" * 30)
alumnos[0]["materias"].add ("laboratorio")
print(alumnos[0])