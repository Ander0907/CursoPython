print("Bienvenido!")
texto = (input("Ingresa por favor un texto: ")) 
letras = []

texto = texto.lower()

print("¡Muy bien! Ahora piensa en 3 letras")
letras.append(input("Ingresa por favor la primera letra: ").lower()) 
letras.append(input("Ingresa por favor la segunda letra: ").lower()) 
letras.append(input("Ingresa por favor la tercera letra: ").lower()) 



print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])


print(f"Se ha encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Se ha encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Se ha encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} en tu texto")

print("LETRAS DE INICIO Y FIN")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra inicial es {letra_inicio} y la letra final es {letra_fin}")

print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir '{texto_invertido}'")


print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")