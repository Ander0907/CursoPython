from random import shuffle

# Lista inicial
palitos = ['-', '--', '---', '----']

# Mezclar palos
def mezclar_palitos(lista):
    shuffle(lista)
    return lista

# Pedir intento
def probar_suerte():
    intento = ''

    while intento not in ['1', '2', '3', '4']:
        intento = input("Elige un número del 1 al 4: ")
    return int(intento)

# Comprobar intento
def check_intento(lista, intento):

    if lista[intento - 1] == '-':
        print("Sacaste el palito más corto")
    else:
        print("Te salvaste")
    
    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclados = mezclar_palitos(palitos)
seleccion = probar_suerte()
check_intento(palitos_mezclados, seleccion)

