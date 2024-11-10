def devolver_distintos (num1, num2, num3):
    lista = [num1, num2, num3]
    suma = sum(lista)
    
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        numeros_ordenados = sorted(lista)
        return numeros_ordenados[1]
        

print(devolver_distintos(1,2,10))