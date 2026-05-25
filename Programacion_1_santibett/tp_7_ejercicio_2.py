linea = " mara ; programacion ; 8 "

partes = linea.split(";")
nombre = partes[0].strip().capitalize()
materia = partes[1].strip().capitalize()
nota_texto = partes[2].strip()

if nota_texto.isnumeric():
    nota = int(nota_texto)
    print(f"{nombre} cursa {materia} y obtuvo {nota}")
else:
    print("La nota no es valida")
"""
1)
en partes, queda guardado el texto pero dividido en una lista 
ya que se esta cortando en los ;
2)
strip se usa antes del capitalize, ya que el programa
primer borra los espacios con el strip, y el resultado
pasa luego por el capitalize
3)
antes de convertir el texto de nota en un int, se stripea para 
sacarle los espacios y luego valida con isnumeric() para asegurarse
que es un numero y no romper el programa. si isnumeric da False, 
simplemente recurre al else y no se convierte en int.
4)
si tuviese "ocho" el isnumeric() devolveria False, por lo tanto
imprime print("La nota no es valida").

"""
