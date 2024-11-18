class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def sonido(self):
        print(f"Pio, mi color es {self.color}")
    
    def volar(self, metros):
        print(f'Y he volado {metros} metros')
        self.sonido()

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} de huevos")

piolin = Pajaro('Azul', 'Rara')