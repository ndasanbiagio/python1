# Creando una funcion simple         - ()van los parametros
def saludar():
    print("Hola Nico, como estas??")


saludar()


# Crando una funcion con parametros -> parametro es una variable que existe dentro de la funcion
def saludo(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
    elif (sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = 'amor'

    print(f"Hola {nombre}, mi {adjetivo} ... como estas??")


saludo("Nico", "hombre")
saludo("Camila", "mujer")
saludo("xxx", "no binario")


# Crear una funcion que nos retorne valores
def crear_contrasenia_randon(num):
    chars = "acbdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasenia = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasenia, num


# Desempaquetando la funcion
password, primer_numero = crear_contrasenia_randon(52)

# Mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es : {password}")
print(f"El numero utlizados para crearla fue: {primer_numero}")
