mi_diccionario = {'color' : 'rojo', 'marca': 'BMW', 'c3' : [10, 20, 30]}
print(mi_diccionario)

resultado = mi_diccionario['color']
consulta = (mi_diccionario['marca'])
print(resultado)
print(consulta)
print(mi_diccionario['c3'][1])

dic = {'c1': ['a', 'b', 'c'], 'c2' : ['d', 'e', 'f']}
print(dic['c2'][1].upper())

dic[2] = 'c'

print(dic)
print(dic.keys()) #Sirve para visualizar todas las claves de un diccionario
print(dic.values()) #Sirve para visualizar todos las valores de un diccionario