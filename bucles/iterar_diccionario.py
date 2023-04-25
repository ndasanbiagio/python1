diccionario = {
    "nombre": "Nico",
    "apellido": "Dasanbiagio",
    "numero": 38
}


# Recorriendo diccionario con items() para obtener las claves
for key in diccionario.items():
    key
    print(f"la clave es: {key}")


# Recorriendo diccionario con items() para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la clave es: {key} y el valor es {value}")
