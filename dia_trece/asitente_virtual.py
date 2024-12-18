import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Esta función devuelve el audio ingresado en texto
def convertir_audio_en_texto():
    # Esta varaiable almacena recognizer en una variable
    r = sr.Recognizer()

    # Se configura el microfono
    with sr.Microphone() as origen: 
        # Se define el tiempo de espera
        r.pause_threshold = 0.8
        # Informar que comenzo la grabación
        print('Listo, puedes hablar')
        # Guardar el audio recibido
        audio = r.listen(origen)

        try:
            # Se reconoce el audio
            pedido = r.recognize_google(audio, language="es-ar")
            # Esto es una prueba
            print(f"Digiste: {pedido}")
            return pedido
        
        # Si el audio ingresado no es reconocido
        except sr.UnknownValueError:
            print("No se entendió") 
            return "Sigo experando..."

        # Si se encuentra un error relacionado con el servicio
        except sr.RequestError as e:
            print(f"Ocurrió un error: {e}")
            return "Sigo experando..."
        
        # Si finalmente ocurre un error con el codigo
        except:
            return "Revisa el código"

# Función para que el assitente pueda ser escuchado
def hablar(mensaje):
    # Encender el motor de pyttsx3
    motor = pyttsx3.init()
    # Pesonalizar voz
    motor.setProperty('voice', 1)
    # Pronunciar mensaje
    motor.say(mensaje)
    motor.runAndWait()

# Función para que el asistente nos diga el día actual
def pedir_dia():
    # Crear variable con los datos de hoy
    dia = datetime.date.today()
    print(dia)

    # Crear varaiables para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    # Diccionario con nombres del dia
    calendario = {0:'Lunes', 1: 'Martes', 2:'Miércoles', 3:'Jueves', 4:'Viernes', 5:'Sabado', 6:'Domingo'}

    # Decir el dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

# Función para que el asistente nos diga la hora y minutos actuales
def pedir_hora():
    # Crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    print(hora)

    # Decir hora
    hablar(hora)

# Función que devuelve el saludo inicial
def saludar():
    # Crear varaible con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'{momento}, soy tu asistente virtual, por favor, dime en que te puedo ayudar')

# Función central del asistente
def peticiones():
    # Llamar al saludo
    saludar()
    # Variable de corte
    comenzar = True

    # Loop central:
    while comenzar:
        # Activar el microfono y guaradr el pedido en un tipo de dato string
        pedido = convertir_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Breve pa, ya le abro el youtube mi rey')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('De una pai')
            webbrowser.open('https://www.google.com.co')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'que hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Ya se lo busco mi niño')
            pedido = pedido.replace('wikipedia', '')
            wikipedia.set_lang('es')
            # Resultado almacena un resumen del pedido
            resultado = wikipedia.summary(pedido, sentences= 1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('De una mi leon')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que encontré')
        elif 'reproducir' in pedido:
            hablar('Muy buena idea mi papacho')
            pywhatkit.playont(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple': 'APPL', 'amazon': 'AMZN', 'google': 'GOOGL'}

            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La enontré, el precio actual de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdón pero no la he encontrado')
                continue
        elif 'adios' in pedido:
            hablar('Chao mor, cualquier cosita me marca')
            break

# Llamamos la función para que sea ejecutada
peticiones()