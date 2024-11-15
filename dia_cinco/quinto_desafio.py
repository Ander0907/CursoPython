from random import choice

print("Bienvenido al juego del Ahorcado\nEn este juego se usarán palabras del área de desarrollo de software\nTienes 10 intentos para adivinar la palabra")

# Lista de palabras y configuración inicial
lista_palabras = ["python", "java", "javascript", "html", "angular", "react", "kotlin"]
# Se agregan las letras adivinadas por el usuario
letras_adivinadas = set() 
# Número de intentos
intentos = 8  

def elegir_palabra(lista):
    return choice(lista)

def mostrar_guiones(palabra, letras_adivinadas):
    progreso = [letra if letra in letras_adivinadas else "_" for letra in palabra]
    print(" ".join(progreso))

def pedir_letra():
    return str(input("Ingrese una letra: ").strip().lower()) 

def chequear_letra(letra, palabra, letras_adivinadas):
    if letra in palabra:
        print(f"La letra '{letra}' está en la palabra.")
        letras_adivinadas.add(letra)
    else:
        print(f"La letra '{letra}' no está en la palabra.")
        return False

# Elección de palabra aleatoria
palabra = elegir_palabra(lista_palabras)

# Bucle principal del juego
while intentos > 0:
    mostrar_guiones(palabra, letras_adivinadas)
    letra = pedir_letra()

    # Verificar si la letra ya fue adivinada
    if letra in letras_adivinadas:
        print("Ya adivinaste esa letra, intenta con otra.")
        continue

    # Chequear si la letra está en la palabra
    if not chequear_letra(letra, palabra, letras_adivinadas):
        intentos -= 1  # Restar un intento si la letra es incorrecta
        print(f"Te quedan {intentos} intentos.")

    # Verificar si se ha ganado
    if all(letra in letras_adivinadas for letra in palabra):
        print("\n¡Felicidades! Has adivinado toda la palabra:")
        mostrar_guiones(palabra, letras_adivinadas)
        break

# Si se terminan los intentos
if intentos == 0:
    print(f"\nTe has quedado sin intentos. La palabra era '{palabra}'. ¡Sigue practicando!")
