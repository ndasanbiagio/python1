#Ejercicio 2 Nuevo
#Falto el profesor y los alumnos van a armar la clase.

#Pedir el nombre y la edad de los compañeros que vinieron hoy a clases


#Funcion para obtener al asistente y al profesor segun la edad
def obtener_companieros(cantidad_de_companieros): 
    
    #Creando la lista con los compañeros
    companieros = []
    
    #Ejecutando un FOR para pedir informacion de cada compañero
    for i in range(cantidad_de_companieros):
        nombre = input("Ingreso el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compeñero: "))
        companiero = (nombre, edad)
        
        #Agregando la informacion a la lista
        companieros.append(companiero)
        
    #Ordenandolos de menor a mayor segun su edad
    companieros.sort(key=lambda x:x[1])     #sort es para ordenar
    
    #Compañeros[x] devuelve una tupla con (nombre,edad) y despues accdemos al nombre
    #para definir al asistente y al profesor
    asistente = companieros[0][0]
    profesor = companieros[-1][0]
    
    #Retornamos una tupla
    return asistente,profesor


#Desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_companieros(5)
print(f"El profesor es: {profesor} y su asistente es {asistente}")
    