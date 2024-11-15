mi_archivo = open('utils/textos/prueba.txt', 'a')
mi_archivo.write('\nMy artist favorite is Anuel AA')
lista = ['Crack', 'Idolo', 'Futbol']

for i in lista:
    mi_archivo.writelines(i + '\n')
    
mi_archivo.close()