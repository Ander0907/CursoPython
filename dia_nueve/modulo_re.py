import re

texto = "Si necesitas ayuda llama al 658-598-9977 las 24 horas al servicio de ayuda online"
patron = "ayuda"

busqueda = re.search(patron, texto)
busqueda = re.findall(patron, texto)
print(busqueda)

# patron = r'\d\d\d-\d\d\d-\d\d\d\d'
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron, texto)
print(resultado)

clave = input("Ingrese una clave: ")
patron = r'\D{1}\w{7}'

chequear = re.search(patron, clave)
print(chequear)

texto = "No atentedemos los luhes por la tarede, no venga"

buscar = re.search(r'')