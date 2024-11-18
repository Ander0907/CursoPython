import os
from pathlib import Path

ruta = 'C:\Users\zapataan\Music\CursoPythonLocal'

#Se usa para indentificar la ruta actual del archivo
ruta_uno = os.getcwd() 

ruta_dos = os.chdir()

#Se usa para crear directorios
ruta_tres = os.makedirs()

#Se usa para obtener el nombre del directorio
elemento_uno = os.path.dirname(ruta)

#Se usa para eliminar el directorio
os.rmdir()

otro_archivo = open('C:\Users\zapataan\Music\CursoPythonLocal\otro_archivo.txt')
print(otro_archivo.read())

carpeta = Path()