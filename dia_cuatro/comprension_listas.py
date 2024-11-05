lista = [letra for letra in 'python']
print(lista)

lista_dos = [n if n * 2 < 10 else 'No' for n in range(1,11)]
print(lista_dos)

pies = [10,20,30,40,50]
metros = [p * 2.281 for p in pies]
print(metros)