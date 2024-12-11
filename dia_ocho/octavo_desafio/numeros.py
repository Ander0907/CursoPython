def generar_turnos_perfumeria():
    for turno in range(1, 400):
        yield f"P - {turno}"

def generar_turnos_farmacia():
    for turno in range(1, 400):
        yield f"F - {turno}"
        
def generar_turnos_cosmetica():
    for turno in range(1, 400):
        yield f"C - {turno}"
        
perfumeria = generar_turnos_perfumeria()
farmacia = generar_turnos_farmacia()
cosmetica = generar_turnos_cosmetica()

def generar_decoracion(eleccion):
    print("********************************")
    print("* Su numero de turno es:       *")
    if eleccion == "P":
        print(next(perfumeria))
    elif eleccion == "F":
        print(next(farmacia))
    elif eleccion == "C":
        print(next(cosmetica))
    print("* Espere y será atentido       *")
    print("********************************")