from tkinter import *
from paleta_colores import palette

# Iniciar Tkinter
app = Tk()

# Tamaño de la ventana
app.geometry('1150x630+0+0')

# Evitar la accion de maximizar
app.resizable(0, 0)

# Definir titulo de la ventana
app.title("Sistema de facturación - LasGordas")

# Color de fondo de la ventana
app.config(bg=palette['background'])

# Panel superior
panel_superior = Frame(app, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# Etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de facturación', fg=palette["text"],
                        font=('Dosis', 58), bg=palette["background"], width=27)
etiqueta_titulo.grid(row=0, column=0)

# Panel izquierdo
panel_izquierdo = Frame(app, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg= 'azure4', padx=50)
panel_costos.pack(side=BOTTOM)

# Panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg=palette["text"])
panel_comidas.pack(side=LEFT)

# Panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg=palette["text"])
panel_bebidas.pack(side=LEFT)

# Panel postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres', font=('Dosis', 19, 'bold'),
                           bd=1, relief=FLAT, fg=palette["text"])
panel_postres.pack(side=LEFT)

# Panel derecha
panel_derecha = Frame(app, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg=palette['frame'])
panel_calculadora.pack()

# Panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Panel botones
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg=palette["text"])
panel_botones.pack()

# Lista de productos
lista_comidas = ['pollo', 'cordero', 'salmon', 'merluza', 'kebab', 'pizza1', 'pizza2']
lista_bebidas = ['agua', 'soda', 'jugo', 'cola', 'vino', 'cerveza', 'limonada']
lista_postres = ['helado', 'fruta', 'brownies', 'flan', 'mousse', 'paleta', 'torta']

# Generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0

for comida in lista_comidas:
    # Crear CheckButtons
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                        text=comida.title(),
                        font=('Dosis', 19, 'bold',),
                        onvalue=1,
                        offvalue=0, 
                        variable=variables_comida[contador])
    comida.grid(row=contador, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                font=('Dosis', 18, 'bold',),
                                bd= 1,
                                width= 6,
                                state= DISABLED,
                                textvariable= texto_comida[contador])
    cuadros_comida[contador].grid(row= contador, column = 1)
    contador += 1

# Generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0

for bebida in lista_bebidas:
    # Crear CheckButtons
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                        text=bebida.title(),
                        font=('Dosis', 19, 'bold',),
                        onvalue=1,
                        offvalue=0,
                        variable=variables_bebida[contador])
    bebida.grid(row=contador, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                font=('Dosis', 18, 'bold',),
                                bd= 1,
                                width= 6,
                                state= DISABLED,
                                textvariable= texto_bebida[contador])
    cuadros_bebida[contador].grid(row= contador, column = 1)
    contador += 1

# Generar items postre
variables_postre = []
cuadros_postre = []
texto_postre = []
contador = 0

for postre in lista_postres:

    # Crear CheckButtons
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', 19, 'bold',),
                        onvalue=1, offvalue=0, variable=variables_postre[contador])
    postre.grid(row=contador, column=0, sticky=W)

    # Crear los cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                font=('Dosis', 18, 'bold',),
                                bd= 1,
                                width= 6,
                                state= DISABLED,
                                textvariable= texto_postre[contador])
    cuadros_postre[contador].grid(row= contador, column = 1)
    contador += 1

# Variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Etiquetas de costo y campos de entrada - Comida
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo comida',
                              font=('Dosis', 12, 'bold',),
                              bg= 'azure4',
                              fg = 'white'
                              )
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold',),
                           bd= 1,
                           width= 10,
                           state= 'readonly',
                           textvariable= var_costo_comida)
texto_costo_comida.grid(row= 0, column= 1, padx = 40)

# Etiquetas de costo y campos de entrada - Bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo bebida',
                              font=('Dosis', 12, 'bold',),
                              bg= 'azure4',
                              fg = 'white'
                              )
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold',),
                           bd= 1,
                           width= 10,
                           state= 'readonly',
                           textvariable= var_costo_bebida)
texto_costo_bebida.grid(row= 1, column= 1, padx = 40)

# Etiquetas de costo y campos de entrada - Postres
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo postre',
                              font=('Dosis', 12, 'bold',),
                              bg= 'azure4',
                              fg = 'white'
                              )
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold',),
                           bd= 1,
                           width= 10,
                           state= 'readonly',
                           textvariable= var_costo_postre)
texto_costo_postre.grid(row= 2, column= 1, padx = 40)

# Etiquetas de costo y campos de entrada - Subtotal
etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                              font=('Dosis', 12, 'bold',),
                              bg= 'azure4',
                              fg = 'white'
                              )
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold',),
                           bd= 1,
                           width= 10,
                           state= 'readonly',
                           textvariable= var_subtotal)
texto_subtotal.grid(row= 0, column= 3, padx = 40)

# Etiquetas de costo y campos de entrada - Impuesto
etiqueta_impuesto = Label(panel_costos,
                              text='Impuestos',
                              font=('Dosis', 12, 'bold',),
                              bg= 'azure4',
                              fg = 'white'
                              )
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold',),
                           bd= 1,
                           width= 10,
                           state= 'readonly',
                           textvariable= var_impuesto)
texto_impuesto.grid(row= 1, column= 3, padx = 40)

# Etiquetas de costo y campos de entrada - Total
etiqueta_total = Label(panel_costos,
                              text='Total',
                              font=('Dosis', 12, 'bold',),
                              bg= palette['frame'],
                              fg = 'white'
                              )
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos, 
                           font=('Dosis', 12, 'bold',),
                           bd= 1,
                           width= 10,
                           state= 'readonly',
                           textvariable= var_impuesto)
texto_total.grid(row= 2, column= 3, padx = 40)

# Botones
botones = ['total', 'recibo', 'guardar', 'resetear']
columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                    text= boton.title(),
                    font=('Dosis', 12, 'bold',),
                    fg= 'white',
                    bg = 'azure4',
                    bd= 1,
                    width= 9
                    )
    boton.grid(row=0, column= columnas)
    columnas +=1

# Area de recibos
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 12, 'bold',),
                    bd= 1,
                    width= 42,
                    height= 10
                    )
texto_recibo.grid(row= 0, column= 0)

# Diseño de calculadora
visor_calculadora = Entry(panel_calculadora,
                    font=('Dosis', 16, 'bold',),
                    width= 38,
                    bd= 1,
                    )
visor_calculadora.grid(row= 0, column= 0, columnspan=4)

botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-',
                    '1', '2', '3', 'x', 'CE', 'Borrar', '0', '/']

fila = 1
columna = 0

for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                text= boton.title(),
                font=('Dosis', 16, 'bold',),
                fg= 'white',
                bg= palette['frame'],
                bd= 1,
                width=8)
    boton.grid(row= fila, column= columna)

    if columna == 3:
        fila +=  1
    
    columna += 1

    if columna == 4:
        columna = 0

# Evitar que la app se cierre
app.mainloop()