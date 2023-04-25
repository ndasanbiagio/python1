# Creando una funcion de 3 parametros
def frase(nombre, apellido, adjetivo):
    # Parametro posicional por defecto
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'


# Utilizando Keyword Arguments
frase_resultante = frase(
    adjetivo="capo", nombre="Nico", apellido="Dasanbiagio")  # Estoy forzando los parametros - ubicandolos como yo quiero
print(frase_resultante)


# Creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre, apellido, adjetivo="Tonto"):
    return f'Hola {nombre} {apellido}, sos muy {adjetivo}'


# Ultimo parametro lo estoy colocando a la fuerza
frase_resultante1 = frase("Diego", "Mercado", "Inteligente")
print(frase_resultante1)
