def funcion_linda(palabra):
    letras_ordenadas = sorted(palabra.lower())
    return ''.join(letras_ordenadas)


print(funcion_linda("Hola"))