from random import randint

print("¡Bienvenido!")
nombre = str(input("¿Cuál es tu nombre?: "))
print(f'Mucho gusto {nombre}, he pensado en un numero del 1 al 100 y quiero que lo adivines, tienes 8 intentos para adivinarlo')

numero_secreto = randint(1,100)
intento = 0

while intento < 8:
    numero_ingresado = int(input("Ingresa un numero del 1 al 100: "))
    intento += 1
    if numero_ingresado < 1 or numero_secreto > 100:
        print("El número ingresado no está en el rango de 1 a 100") 
    elif numero_ingresado < numero_secreto:
        print("Incorrecto, el numero ingresado es menor al numero secreto")
    elif numero_ingresado > numero_secreto:
        print("Incorrecto, el numero ingresado es mayor al numero secreto")
    elif numero_ingresado == numero_secreto:
        print(f"Felicidades, has acertado el numero secrecto en {intento} intentos")
        break


if intento == 8:
    print(f"Perdiste, has superado los 8 intentos, el numero secreto era: {numero_secreto}")