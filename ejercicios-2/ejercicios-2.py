# Falto el profe y los pibes van a armar la clase.

# Pedir el nombre y la edad de los compañeros que vinieron hoy a clases.


# Funcion par obtener al asistente y al profesor segun la edad
def obtenet_companieros(cantidad_de_companieros):

    # Creando la lista con los compañeros
    companieros = []

    # Ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_companieros):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        companiero = (nombre, edad)

        # Agregando la informacion a la lista
        companieros.append(companiero)

    # Ordenandolos de menor a mayor segun su edad
    companieros.sort(key=lambda x: x[1])

    # Compañeros [x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre para definir al asistente y al profesor
    asistente = companieros[0][0]
    profesor = companieros[-1][0]

    # Retornamos la tupla
    return asistente, profesor


# Desempaquetamos lo que nos retorna la funcion
asistente, profesor = obtenet_companieros(5)


# Mostrando el resultado
print(f"El profesor es: {profesor} y el asistente es: {asistente}")
