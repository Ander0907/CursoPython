import os
import shutil

#Saber el directorio donde estamos
print(os.getcwd())

archivo = open('prueba.txt' , 'w')
archivo.write('Esto es un archivo de prueba')
archivo.close()

#Listar elemntos del directorio
print(os.listdir())

#Con esta linea podemos cambiar de directorio el archivo espesificado
#shutil.move('prueba.txt', "C:\\Users\\zapataan\\Music\\CursoPython\\utils")

#Elimina un archivo en una ruta especifica
#os.unlink()

#Elimina un directorio
#os.rmdir()

#Elimina el contenido espesificado permanetmente sin enviarlo a la papelera
#shutil.rmtree()

#Recorre todos los elementos de una ruta
print(os.walk("C:\\Users\\zapataan\\Music\\CursoPython\\utils"))

ruta = "C:\\Users\\zapataan\\Music\\CursoPython\\utils\\Recetas"

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {ruta}")
    print(f"Las subcarpetas son:")
    for sub in subcarpeta:
        print(f"\t {sub}")
    
    print("Los archivos son:")
    for arch in archivo:
        if arch.startswith("Carne"):
            print(f"\t {arch}")
    print("\n")