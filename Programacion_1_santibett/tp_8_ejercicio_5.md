```python
def limpiar(texto):
    return texto.strip().capitalize()

def es_valido(nombre):
    if len(nombre) >= 3:
        return True
    return False

nombres = [" bart ", "ED", " walter", "rick "]
validos = []

for nombre in nombres:
    nombre_limpio = limpiar(nombre)

    if es_valido(nombre_limpio):
        validos.append(nombre_limpio)

print(validos)
```

¿Qué hace el programa?
encuentra que nombres de la lista cumplen tener mas de 2 caracteres

¿Qué hace la función limpiar?
saca los espacios de principio y final si es que hay 
y pone mayuscula solo la primer letra

¿Qué hace la función es_valido?
valida si tiene mas de 2 caracteres

¿Qué nombres quedan almacenados en validos?
deberian quedar Bart, Walter y Rick

¿Qué imprime el programa al finalizar?
una lista con los nombres validos.
["Bart", "Walter", "Rick"]