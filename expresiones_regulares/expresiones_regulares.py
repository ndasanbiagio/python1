# Expresiones regulares -> es encontrar coincidencias y mostrarlas
import re       # re -> el modulo de expresiones regulares

texto = '''Hola Nico, como estas??, esta es. la cadena 1. Como que onda
Que se ababab cuenta por ahí 111. Estas ab bien onda
Alguna novedad.??  y se termina...'''

# Haciendo una busqueda simple
resultado = re.search("esta", texto)

# \d -> busca digitos númericos de 0 a 9
resultado = re.findall(r"\d", texto)

# \D -> busca TOTO MENOS digitos númericos del 0 - 9
resultado = re.findall(r"\D", texto)


# \w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w", texto)


# \W -> busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W", texto)


# \s -> busca espacios en blanco -> espacios, tabs, saltos de lineas
resultado = re.findall(r"\s", texto)


# \S -> busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de lineas
resultado = re.findall(r"\S", texto)


# . -> busca TODO MENOS saltos en linea
resultado = re.findall(r"\.", texto)


# \n -> busca saltos de linea
resultado = re.findall(r"\n", texto)

# \ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\.", texto)

# Armando una cadena que busque un numero, seguido de un punto y un espacio
resultado = re.findall(f' \d\. \s', texto)


# Buscando el principio de una linea
# ^ -> busca el comienzo de una linea
resultado = re.findall(f'^Que', texto, flags=re.M)


# $ -> busca el final de una linea
resultado = re.findall(r'onda$', texto, flags=re.M)


# {n} -> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}', texto)

# {n,m} -> al menos n, como maximo m
resultado = re.findall(r'\d{1,2}', texto)
resultado = re.findall(r'[ab]{2}', texto)


# | -> busca una cosa o la otra
resultado = re.findall(r'\d{1,2}|Hola', texto)


print(resultado)
