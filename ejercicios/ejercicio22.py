# def pedirDatosDePersona():
    
#     d = {}
    
#     d["Nombre"] = input("Por favor ingresa tu nombre: \n")
#     d["Apellido"] = input("Por favor ingresa tu Apellido: \n")
#     d["Edad"] = int (input("Por favor ingresa tu Edad: \n"))
    
#     return d

# print(pedirDatosDePersona(d))


def pedirDatosDePersona():
    d = {}
    d["Nombre"] = input("Por favor ingresa tu nombre: \n")
    d["Apellido"] = input("Por favor ingresa tu Apellido: \n")
    d["Edad"] = int(input("Por favor ingresa tu Edad: \n"))
    return d


diccionario1 = {}
diccionario1 = pedirDatosDePersona()

print(diccionario1)