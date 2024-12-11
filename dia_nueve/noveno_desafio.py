import shutil, math, datetime, os, re, time, pathlib

# Esta fué la forma en la que descomprimí el archivo .zip
# shutil.unpack_archive('C:\\Users\\zapataan\\Music\\CursoPython\\utils\\Proyecto_Dia_9.zip', 'Instrucciones', 'zip')

# Con esta variable tomo el tiempo de inicio del aplicativo
inicio = time.time()

# Esta variable alamcena la ruta donde alamcené el contenido del archivo .zip
ruta = "C:\\Users\\zapataan\\Music\\CursoPython\\utils\\Instrucciones\\Mi_Gran_Directorio"
# Esta variable almacena el patron de busqueda
patron = r'N\D{3}-\d{5}'
numeros_agregados = []
archivos_encontrados = []

# Esta función devuelve la hora y fecha cuando se hizo la busqueda 
def obtener_fecha_busqueda():
    fecha = datetime.datetime.today()
    print(f"Fecha de busqueda: {fecha}")

# En esta función se busca por cada archivo el patrón requerido
def buscar_por_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()

    if re.search (patron, texto):
        return re.search (patron, texto)
    else:
        return ''
    
# En esta función recorremos la carpeta, subcarpetas y archivos 
def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for arch in archivo:
            resultado = buscar_por_numero(pathlib.Path(carpeta, arch), patron)
            if resultado != '':
                numeros_agregados.append((resultado.group()))
                archivos_encontrados.append(arch.title())

# Por ultimo en esta función, ordeno la forma en la que se van a mostrar los datos
def mostrar_busqueda():
    indice = 0
    print("x"*46)
    obtener_fecha_busqueda()
    print('\n')
    print("ARCHIVO\t\t\t NRO.SERIE")
    print('-------\t\t\t----------')
    for a in archivos_encontrados:
        print(f"{a}\t\t{numeros_agregados[indice]}")
        indice+=1
    fin = time.time()
    duracion = fin - inicio
    print('\n')
    print(f"Duracion de la busqueda: {math.ceil(duracion)}")
    print("x"*46)

crear_listas()
mostrar_busqueda()  