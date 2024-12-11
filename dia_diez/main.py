import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Se define el tamaño de la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Personalizar titulo e icono
pygame.display.set_caption("Sonaloss")
icono = pygame.image.load("C:\\Users\\zapataan\\Music\\CursoPython\\utils\\img\\ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("C:\\Users\\zapataan\\Music\\CursoPython\\utils\\img\\fondo.jpg")

# Agregar sonidos
pygame.mixer.music.load("C:\\Users\\zapataan\\\Music\\CursoPython\\utils\\sounds\\MusicaFondo.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

# Texto final del juego
fuente_final = pygame.font.Font('freesansbold.ttf', 32)

def mostrar_texto_final():
    final = fuente_final.render("GAME OVER MI PAPA", True, (179, 19, 18))
    pantalla.blit(final, (60, 200))

# Definir personaje jugador y posicion inicial
img_jugador = pygame.image.load("C:\\Users\\zapataan\\Music\\CursoPython\\utils\\img\\cohete.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# Bloque para duplicar enemigos
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 5

for e in range(cantidad_enemigos):
    # Definir personaje enemigo y posicion inicial
    img_enemigo.append(pygame.image.load("C:\\Users\\zapataan\\Music\\CursoPython\\utils\\img\\enemigo.png"))
    enemigo_x.append(random.randint(0, 736)) 
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5) 
    enemigo_y_cambio.append(50)

# Definir bala y posicion inicial
img_bala = pygame.image.load("C:\\Users\\zapataan\\Music\\CursoPython\\utils\\img\\bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0.3
bala_y_cambio = 3
bala_visible = False

# Variable puntaje
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# Mostar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255))
    pantalla.blit(texto, (x, y))

# Función jugador
def jugador(x, y):
    # blit sirve para mostrar
    pantalla.blit(img_jugador, (x, y))

# Función enemigo
def enemigo(x, y, enemi):
    # blit sirve para mostrar
    pantalla.blit(img_enemigo[enemi], (x, y))

# Funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

# Funcion detectar colisiones
def validar_colison(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False

# Con este bloque indicamos que cuando se realize el evento QUIT finalice la ejecución del programa
se_ejecuta = True
while se_ejecuta:
    # Imagen de fondo
    pantalla.blit(fondo, (0,0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        
        # Valida si se presionó alguna tecla
        if evento.type == pygame.KEYDOWN:
            # Valida si se presiono la tecla izquierda
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            # Valida si se presiono la tecla derecha
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            # Valida si se presiono la tecla espacio
            if evento.key == pygame.K_SPACE:
                sonido_bala = pygame.mixer.Sound("C:\\Users\\zapataan\\\Music\\CursoPython\\utils\\sounds\\disparo.mp3")
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # Valida si se liberó la tecla
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Aca se modifica la posición del jugador
    jugador_x += jugador_x_cambio

    # Limitar posiciones del jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] > 490:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            mostrar_texto_final()
            break

        # Aca se modifica la posición del enemigo
        enemigo_x[e] += enemigo_x_cambio[e]

        # Limitar posiciones del enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.5 
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.5
            enemigo_y[e] += enemigo_y_cambio[e]

        # Colision
        colision = validar_colison(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = pygame.mixer.Sound("C:\\Users\\zapataan\\\Music\\CursoPython\\utils\\sounds\\Golpe.mp3")
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 734)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)

    # Actualizar 
    pygame.display.update()