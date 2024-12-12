import bs4
import requests

# Crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

# Lista de titulos con 4 0 5 estrellas
titulos_rating_alto = []

# Iterar paginas
for pagina in range(1, 51):
    # Crear sopa en cada pagina
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    # Seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    # Iterar sobre cada uno de los libros
    for libro in libros:
        # Verificar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')):
            # Guardar titulo del libro en variable
            titulo_libro = libro.select('a')[1]['title']

            # Guardar titulo del libro en lista
            titulos_rating_alto.append(titulo_libro)

# Mostrar libros de 4 y 5 estrellas
for t in titulos_rating_alto:
    print(t)