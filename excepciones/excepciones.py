# Creando funcion que suma numeros
def sumar_dos():
    # Iniciando el Bucle
    while True:
        # Pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numeor 2: ")
        # Intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
            # Si lanzo una excepción, pedirle que reingrese los datos
        except ValueError as e:
            print("Te pedi un numero....")
            print(f"ERROR: {e}")
            # Si todo salio bien, terminamos el bucle
        else:
            break
        finally:
            print("Esto se ejecuta siempre")
# Mostrando el resultado
    return resultado


print(f"La suma te da: {sumar_dos()}")
