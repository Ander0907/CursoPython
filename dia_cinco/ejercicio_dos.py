from random import choice

lista_numeros = [1,2,3,4]

def lanzar_moneda():
    opciones = ['Cara', 'Cruz']
    resultado = choice(opciones)
    return resultado

def probar_suerte(resultado, lista):
    if resultado == 'Cara':
        lista_vacia = lista.clear()
        print("La lista se autodestruirá")
        return []
    elif resultado == 'Cruz':
        print("La lista fue salvada")
        return lista

ensayo = lanzar_moneda()
ensayo_dos = probar_suerte(ensayo, lista_numeros)
print(ensayo)
print(ensayo_dos)