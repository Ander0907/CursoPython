print("Bienvenido!")
nombre = input("¿Cuál es tu nombre?: ")

print(f"Gusto en conocerte {nombre}")
ventas = input("Ahora dime, ¿Cuál es tu numero de ventas?: ")

calculo_ventas = int(ventas) * 13 / 100 
resultado_redondeado = round(calculo_ventas, 2)

print(f"{nombre} tus comisiones de este mes son de: {resultado_redondeado}" )