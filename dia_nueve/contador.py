# Counter cuenta los elementos que se le pasen, listas, variables, etc...
from collections import Counter, defaultdict, namedtuple

numeros = [1, 2, 3, 4, 5, 6]
print(Counter(numeros))

mi_dic = defaultdict(lambda: 'nada')

mi_dic['uno'] = 'verde'

