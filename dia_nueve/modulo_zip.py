import zipfile
import shutil

mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')

mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()

carpeta_origen = "C:\\Users\\zapataan\\Music\\CursoPython\\utils\\Recetas"
archivo_destino = 'Todo_Comprimido.zip'

shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Todo_Comprimido.zip', 'Extracción terminada', 'zip')