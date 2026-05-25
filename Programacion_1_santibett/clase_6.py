"""

var1 = 4
var2 = 2.1
var3 = True
var4 = "hola"

print (f"int: {var1} ")
print (f"float: {var2}" )
print (f"bool: {var3}" )
print (f"str: {var4}" )

nums= [1, 100, 300, 1000]
print(sum(nums))
print(len(nums))
print(sum(nums)/len(nums))

total = 0
for i in nums:
    total += i
cantidad = len(nums)
promedio = ({total / cantidad})
print (total)
print (cantidad)
print(promedio)

#ejercicio 3
x  = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]
minimo = 0
maximo = 0
for i in x:
    if i > maximo:
        maximo = i
print(maximo)
for i in x:
    minimo = 0
    if i < minimo:
        minimo = i
print(minimo)

x  = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]
for i in range(len(x)):
        if x[i] % 2 == 0:        
            print (x[i])

productos = ["papa", "manzana", "zanahoria"]
print (productos [-1])
print (productos [0])

contador = 0
for i in productos:
    contador += 1
print (contador)

```python
# Mi codigo
```

def saludo():
    print("Buenas")
def saludo2():
    return "Holaa"
def personalizado(nom):
    return f"que tal {nom}? "


saludo()
print(saludo2())
print(personalizado("santi"))

def pedir():
    numeros = []
    print("ingresa 0 para terminar")
    while True:
        n = int(input("ingresa un numero: "))
        if n != 0:
            numeros.append(n)
        else:
            break
    return numeros

def suma (lista_numero):
    total = 0
    for i in lista_numero:
        total += i
    return total

lista = pedir()
if len(lista) > 0:
    lasuma = suma(lista)
    cantidad = len(lista)
    promedio = lasuma / cantidad
    
    print(f"la suma de los numeros ingresados es {lasuma}, la cantidad es {cantidad}, el promedio es {promedio}")
else:
    print("no se ingesaron numeros")

#el primer codigo, el for lo que hace es recorrer los elementos uno por uno de la lista y luego suma el valor a una variable llamada total, por lo que es 1 +2 +3
#el segundo es una funcion que el for recorre los elementos de la lista uno por uno y si es mayor a 0 suma uno a la variable de contador, por lo que devuelve 3
nums = [1, 2, 2, 3, 4, 4, 4, 5]
n = []
for i in range(len(nums)):
    if nums[i] in n:
        pass
    else:
        n.append(nums[i])
print(n)
"""
print("ingrese fin para terminar")
L = []
while True:
    N = input("mete un producto: ")
    if N != "fin":
        L.append(N)
    else:
        break
print(f"la cantidad de productos son {len(L)}")

c = 0
Lu = []
for i in L:
    c += 1
    if i not in Lu:
        Lu.append(i)
print(f"productos unicos: {Lu}")
print("detalles del pedido:")
for i in Lu:
    unidades = 0
    for j in L:
        if j == i:
            unidades += 1
    print(f"{i}, {unidades} unidades")
