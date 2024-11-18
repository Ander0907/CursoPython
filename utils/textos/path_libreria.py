from pathlib import Path

carpeta = Path('C:/Users/zapataan/Music/CursoPythonLocal/otro_archivo.txt')
print(carpeta.read_text())

#Muestra la terminación del archivo
print(carpeta.suffix)

#Muestra el nombre del archivo sin la terminación
print(carpeta.stem)

if not carpeta.exists:
    print("Este archivo existe")
else:
    print("Genial, existe")