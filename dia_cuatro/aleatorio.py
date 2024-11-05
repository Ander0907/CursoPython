#Desde libreria importa metodo
from random import randint

# Importamnos todo lo que está adentro de la libreria
from random import *

aleatorio = randint(1, 10)
print(aleatorio)

aleatorio_dos = round(uniform(1,5),1)
print(aleatorio_dos)

aleatorio_tres = random()
print(aleatorio_tres)

colores = ['Rojo', 'Azul', 'Verde']
aleatorio_cuatro = choice(colores)
print(aleatorio_cuatro)

numeros = list(range(10, 6, 2))
shuffle(numeros)
print(numeros)