from collections import Counter, defaultdict, namedtuple

# Counter sirve para contar lo elementos que se le pasen como parametro
numeros = [1,2,3,4,5,6,7,8]
print(Counter(numeros))

serie = Counter([67,2,2,3,45,6,78,6,5,3])
print(list(serie))

# Defaultdic sirve para guaradr valores por defecto en diccionarios
mi_diccionario = defaultdict(lambda: 'Verde')
mi_diccionario['uno'] = 'Rojo'
print(mi_diccionario['dos'])

print(mi_diccionario)

# namedTuple facilita la busqueda de elementos
Persona = namedtuple('Persona', ['nombre', 'apellido', 'edad'])
ariel = Persona('Ariel', 'Zapata', 19)

print(ariel.edad)