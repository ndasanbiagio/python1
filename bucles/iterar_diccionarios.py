frutas = ["banana", "manzana", "ciruela",
          "pera", "naranja", "granada", "durazno"]
cadena = "Hola Nico"
numeros = [2, 5, 8, 10]

# Evitando que se coma una granada
for fruta in frutas:
    if fruta == 'granada':
        continue  # Seria una condicion que saltee ese elemento de la lista con "Continue" - es decir que lo quita de la lista y continua con el bucle
    print(f'Me voy a comer una {fruta}')


# Evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == "pera":
        break  # Condicion para cortar ese bucle con el elemento seleccionado antes en el "IF" - Break corta todo el BUCLE
    print(f'Me voy a comer una {fruta}')
print("Bucle terminado")


# Recorrer una cadena de texto
for letra in cadena:
    print(letra)


# For en una sola linea de codigo - UNA OPCION MAS ALARGADA
numeros_duplicados = list()
for numero in numeros:
    numeros_duplicados.append(numero*2)

print(numeros_duplicados)

# Una forma para simplificar codigo
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)
