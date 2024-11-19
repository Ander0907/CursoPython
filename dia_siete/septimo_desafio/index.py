from Persona import Persona
from Cliente import Cliente
from os import system


def tomar_datos():
    nombre = str(input("Por favor ingresa tu nombre: "))
    apellido = str(input("Por favor ingresa tu apellido: "))
    return nombre, apellido


def inicio():
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1, 4):  
        print("Elige una opción:")
        print('''
        [1] - Depositar
        [2] - Retirar
        [3] - Finalizar
        ''')
        eleccion_menu = input()

    return int(eleccion_menu)


def crear_cliente(nombre, apellido):
    cliente = Cliente(nombre, apellido)
    print(cliente.mostrar_info())
    return cliente


datos = tomar_datos()
cliente = crear_cliente(*datos)

finalizar_programa = False

# Ciclo principal para mostrar el menú
while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        cliente.depositar() 
    elif menu == 2:
        cliente.retirar()  
    elif menu == 3:
        finalizar_programa = True
        print("Gracias por usar el sistema. ¡Hasta luego!")