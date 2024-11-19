from Persona import Persona
from random import randint

class Cliente(Persona):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.numero_cuenta = sum(randint(0, 9) * 10**i for i in range(10))
        self.balance = 0

    def mostrar_info(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nNúmero de cuenta: {self.numero_cuenta}\nSaldo: ${self.balance}"
    

    def depositar(self):
        cantidad = int(input("¿Cuanto dinero desea depositar?: "))
        self.balance = cantidad
        print("El proceso de realizó con exito")
        print(self.mostrar_info())



    def retirar(self):
        cantidad = int(input("¿Cuanto dinero desea retirar?: "))
        if cantidad < self.balance:
            self.balance -= cantidad
            print(f"Proceso realizado con exito, por favor retire ${cantidad}")
            print(self.mostrar_info())
        else:
            print("Usted no tiene suficiente dinero para retirar esa cantidad")

