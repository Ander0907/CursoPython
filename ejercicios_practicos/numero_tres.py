def funcion_hermosa(*args):
    lista = list(args)
    contador_cero = lista.count(0)
    
    if contador_cero >= 2:
        return True
    else: 
        return False
        
print(funcion_hermosa(0, 0, 1, 2)) 