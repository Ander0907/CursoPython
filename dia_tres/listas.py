mi_lista = ['a', 'b', 'c']
mi_lista_desordenada = [1,9,0,1]

resultado = mi_lista[0]

mi_lista[0] = 'hola'
mi_lista.append('d') #Agrega elementos a la lista
mi_lista.pop(0) #Elimina elemento de la lista, si se deja vacio elimina el ultimo elemnto agregado
print(mi_lista)
print(len(mi_lista))

mi_lista_desordenada.sort() #Ordena la lista
print(mi_lista_desordenada)