from pathlib import *
import os
from os import system

print('Bienvenido a este programa de recetas')
ruta = "C:\\Users\\zapataan\\Music\\CursoPythonLocal\\Recetas"


def leer_receta():
    pass

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def inicio():
    system('cls')
    print(f'La recetas están en: {ruta}')
    print(f'Total de recetas:  {contar_recetas(ruta)}')

    opcion_elegida = 'x'
    while not opcion_elegida.isnumeric() or int(opcion_elegida) not in range(1,7):
        print("******************************************")
        print("*            MENÚ DE OPCIONES            *")
        print("******************************************")
        print("* 1. Leer receta                         *")
        print("* 2. Crear receta                        *")
        print("* 3. Crear categoría --Melo              *")
        print("* 4. Eliminar receta                     *")
        print("* 5. Eliminar categoría --Melo           *")
        print("* 6. Finalizar programa                  *")
        print("******************************************")
        opcion_elegida = input()
    return (opcion_elegida)

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('Elige una categoría: ')
    
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Recetas:")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta_str)
        contador += 1


inicio()

menu = 0



def mostrar_categorias(ruta):
    print("Categorias: ")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def crear_categoria(ruta_completa):
    os.makedirs(ruta_completa)

def eliminar_categoria(ruta_completa):
    os.rmdir(ruta_completa)


if menu == 1:
    categorias = mostrar_categorias(ruta)
    recetas = mostrar_categorias(ruta)
    
elif menu == 2:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
elif menu == 3:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
    ruta_completa = os.path.join(ruta, resultado) 
    crear_categoria(ruta_completa)
elif menu == 4:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
    recetas = mostrar_categorias(ruta)
elif menu == 5:
    categorias = mostrar_categorias(ruta)
    categoria = elegir_categoria(categorias)
    ruta_completa = os.path.join(ruta, resultado) 
    eliminar_categoria(ruta_completa)
