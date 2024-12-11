import shutil, math, datetime, os, re, timeit, pathlib

# Esta fué la forma en la que descomprimí el archivo .zip
# shutil.unpack_archive('C:\\Users\\zapataan\\Music\\CursoPython\\utils\\Proyecto_Dia_9.zip', 'Instrucciones', 'zip')

ruta = "C:\\Users\\zapataan\\Music\\CursoPython\\utils\\Instrucciones\\Mi_Gran_Directorio"
patron = r'N\D{3}-\d{5}'
numeros_agregados = []
archivos_encontrados = []

def obtener_fecha_busqueda():
    fecha = datetime.datetime.today()
    print(f"Fecha de busqueda: {fecha}")

def obtener_duracion_busqueda():
    duracion = timeit.timeit('prueba_for(20000)', globals=globals(), number=1)
    print(f"Duración de la busqueda: {duracion}")

def buscar_por_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()

    if re.search (patron, texto):
        return re.search (patron, texto)
    else:
        return ''
    
def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            resultado = buscar_por_numero(pathlib.Path(carpeta, arch), patron)
            if resultado != '':
                numeros_agregados.append((resultado.group()))
                archivos_encontrados.append(arch.title())
                