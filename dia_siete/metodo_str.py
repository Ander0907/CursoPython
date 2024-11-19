class Album:
    def __init__(self, autor, nombre, canciones):
        self.autor = autor
        self.nombre = nombre
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.nombre} de {self.autor}"
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print("Se ha eliminado exitosamente")
    
mi_album = Album('ANUEL AA', 'LLNM', 17)
        
print(mi_album)
print(len(mi_album))
del mi_album