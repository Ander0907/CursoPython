class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        print(self.nombre + " hace muuuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        print(self.nombre + " hace beeee")

vaca1 = Vaca('Lola')
oveja1 = Oveja('Sonia')

def sonido_animal(animal):
    animal.sonido()

sonido_animal(vaca1)