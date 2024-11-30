def suma():
    num1 = int(input("Ingresa un numero: "))
    num2 = int(input("Ingresa otro numero: "))
    print(num1 + num2)

try:
    #Codigo que se quiere probar
    suma()
except TypeError:
    #Codigo a ejecutar si hay un error
    print("Estás intentando concatenar tipos distintos")
except ValueError:
    #Codigo a ejecutar si hay un error
    print("Ese no es un numero")
else:
    #Codigo a ejecutar si no hay un error
    print("Todo salió bien")
finally:
    #Codigo que se va a ejecutar de todos modos
    print("Eso fué todo")