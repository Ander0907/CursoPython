def check_tres_cifras(numero):
    return numero in range(100,1000)

resultado = check_tres_cifras(659)
print(resultado)


def check_cuatro_cifras(lista):

    for n in lista:
        if n in range(1000, 10000):
            return True
    else:
        pass
    return False

resultado_dos = check_cuatro_cifras([300, 500, 100])
print(resultado_dos)

lista_numeros = [1,2,3,4,5]


def suma_menores(lista_numeros):
    suma = 0
    for n in lista_numeros:
        if 0 < n < 1000:
            suma += n 
    return suma

def cantidad_pares(lista_numeros):
    par = 0
    for i in lista_numeros:
        if i % 2 == 0:
            par += 1
    return par