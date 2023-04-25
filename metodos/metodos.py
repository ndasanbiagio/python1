cadena1 = "Hola soy Nico"
cadena2 = "Ben,vindo,tudo,bem"


# convierte a mayuscula
mayusc = cadena1.upper()

# convierte a miniscula
minusc = cadena1.lower()

# primera letra en mayuscula
primera_letra_mayusc = cadena1.capitalize()

# buscamos una cadena en otra cadena, si no hay coincidencia devuelve -1
busqueda_find = cadena1.find("a")

# buscamos una cadena en otra cadena,si no hay coincidencia tira una exepcion
busqueda_index = cadena1.index("")

# si es numerico, devuelve true sino un false
es_numerico = cadena1.isnumeric()

# si es alfanumerico, nos devuelve true sino false
es_alfanumerico = cadena1.isalpha()

# buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida
contar_coincidencias = cadena1.count("e")

# contameos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencias
contar_caracteres = len(cadena1)

# verificamos si una cadena empieza con otra cadena dada, si es asi da un true
empieza_con = cadena1.startswith("H")

# verificamos si una cadena termina con otra cadena dada, si es asi da un true
empieza_con = cadena1.endswith("ico")

# reemplaza una pedazo de la cadena con otra dada
cadena_nueva = cadena1.replace("la", "lu")

# separar cadenas con la cadena que le pasemos
cadena_separada = cadena2.split(",")

print(type(cadena_separada))
