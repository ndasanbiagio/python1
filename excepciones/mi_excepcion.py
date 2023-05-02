# Creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"Impresionante, cometiste el siguiente error: {err}")


# Manejando la excepcion
try:
    raise MiExcepcion("Jajaja, hiciste mal...")
except:
    print("Como vas a errar asi???")
