class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")


arquero1= Arquero()
mago1 = Mago()
samurai1 = Samurai() 

personajes = [arquero1, mago1, samurai1]

for i in personajes:
    i.atacar()