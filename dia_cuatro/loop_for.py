lista = ['a','b','c','d']

for i in lista:
    numero_letra = lista.index(i) + 1
    print(f"Letra {numero_letra}: {i}")

lista_nombres = ['Ander', 'Jefer', 'Paula', 'Juan']

for nombre in lista_nombres:
    if nombre.startswith('A'):
        print(nombre)