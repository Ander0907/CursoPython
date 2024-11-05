cliente = {'nombre' : 'Anderson',
           'edad' : 17,
           'ocupacion' : 'estudiante'}

pelicula = {'titulo' : 'Matrix',
            'ficha_tecnica' : {'protagonista' : 'Keanu reeves', 
                               'director' : 'Lana y Lilly Wachoski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        case {'nombre' : nombre,
           'edad' : edad,
           'ocupacion' : ocupacion}:
            print("Es un cliente")
            print(nombre, edad, ocupacion)
        case {'titulo' : titulo,
                'ficha_tecnica' : {'protagonista' : protagonista, 
                                'director' : director}}:
            print("Es una pelicula")
            print(titulo, protagonista, director)
        case _:
            print("No sé que es esto")