mi_archivo = open("utils/textos/prueba.txt") # Ruta donde está alojado el archivo de texto

print(mi_archivo.read()) # Ver lo que hay dentro del archivo
print(mi_archivo.readline()) # Ver lo que hay en la primera linea del archivo
print(mi_archivo.readline()) # También sirve para leer linea por linea 

for linea in mi_archivo:
    print("Aquí dice: " + linea)

mi_archivo.close() # Cerar el archivo