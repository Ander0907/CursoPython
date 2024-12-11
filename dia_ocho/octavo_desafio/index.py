from numeros import generar_decoracion

print("Bienvenido a AZB Services")

def inicio():
    while True:
        print('''
        [P] - Perfumería
        [F] - Farmacia
        [C] - Cosmética
        ''')
        eleccion_menu = input("Ingresa una opción: ").strip().upper()

        if eleccion_menu in ['P', 'F', 'C']:
            return eleccion_menu
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

finalizar_programa = False

while not finalizar_programa:
    eleccion = inicio()
    generar_decoracion(eleccion)
    if eleccion == "0":
        finalizar_programa = True
