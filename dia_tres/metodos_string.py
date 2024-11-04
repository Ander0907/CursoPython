texto = "Hola beba, ¿Cómo tú te llamass?"
a = "Aprender"
b = "Python"
c = "es"
d = "genial!"


minuscula = texto.lower() #Imprime el contenido en minuscula
mayuscula = texto.upper() #Imprime el contenido en mayuscula

separar = texto.split("t") #Muestra el contenido en elementos separados

unir = " ".join([a,b,c,d]) #Une los elementos con un espacio entre ellos

buscar = texto.find("s") #Busca un determinado caracter 

remplazar = texto.replace("beba", "bebe")


print(minuscula)
print(mayuscula)
print(separar)
print(unir)
print(remplazar)
print(buscar)