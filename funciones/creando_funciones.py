#Creando una funcion simple - entre los () van los parametros
# def saludar():
#     print("Hola Nico, como va??")

# saludar()
# saludar()
# saludar()


#Creando una funcion con parametros -> son una variable que se crean para ser usadas dentro de un funcion
# def saludar(nombre,sexo):
#     sexo =sexo.lower()
#     if (sexo == "mujer"):
#         adjetivo = "reina"
#     elif (sexo == "hombre"):
#         adjetivo = "titan"
#     else:
#         adjetivo = "amor"
    
#     print(f"Hola {nombre},mi {adjetivo} como estas???")

# saludar("Nico","Hombre")


#Creando una funcion que nos retorne valores

def crear_constrania_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num -2
    c2 = num
    c3 = num -5
    contrasenia = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contrasenia
    
password = crear_constrania_random(3)
frase = f"Tu contraseña nueva es {password}"
print(password)