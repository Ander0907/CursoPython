nombres = ['Anderson', 'Juan', 'Kevin', 'Manuel']
edades = [17, 18, 19, 20]
ciudades = ['Madrid', 'Napoles', 'Milan', 'Buenos Aires']

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombres, edades, ciudades in combinados:
    print(f"Nombre: {nombres}, Edad: {edades}, Ciudad: {ciudades}")