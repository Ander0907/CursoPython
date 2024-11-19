class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")


escudo = Mago()
esconderse = Arquero()
bloqueo = Samurai()

def personaje_defender(personaje):
    personaje.defender()

personaje_defender(escudo)