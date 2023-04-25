def saludar(name):
    return f"Hola {name}! Espero que estes bien!!!"


def saludar_raro(name):
    return f"Hola {name}! como estas groso!!!!"


saludo = saludar("Nico")
print(saludo)

# Siempre se hace asi    -> variable = "Valor" -> pero existe otra forma que siempre funciona en
# modulos que seria: -> "valor" as variable

print(__name__)