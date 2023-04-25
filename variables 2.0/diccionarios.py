# Creando diccionarios con dict()
diccionario = dict(nombre="Nico", apellido="Dasanbiagio")

# Creando diccionarios con fronkeys() valor por defecto: none
diccionario = dict.fromkeys(["nombre", "apellido"])


# Creando diccionarios con fromkeys() cambiando el valor por defecto a "no se"
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")


print(diccionario)
