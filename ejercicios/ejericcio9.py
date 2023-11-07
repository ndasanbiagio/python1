# Ejercicio Paises
paises = ["Canada","USA","Mexico","Australia", "Argentina", "China", "India"]

for indice, numero in enumerate(paises):
    print(f"{indice} {paises[indice]}")







#Ejercicio de numero pares

#Iniciamos una variable para almacenar la suma de los numeros pares
suma_pares = 0

#Iteramos a traves de los numeros 0 al 100 con un paso de 2
for i in range(0, 101, 2):
    #Verificamos si el numero actual es par
    if i % 2 == 0:
        #Si es par, lo sumamos a la variable suma_pares
        suma_pares += i

#Imprimimos el resultado
print(f"La suma de los numeros pares del 0 al 100 es: {suma_pares}")






# Iteramos a través de los números del 10 al 1 con un paso de -1
for i in range(10, 0, -1):
    # Imprimimos el número actual
    print(i)






# Inicializamos una lista vacía para almacenar los números en orden inverso
numeros_inversos = []

# Iteramos a través de los números del 10 al 1 con un paso de -1
for i in range(10, 0, -1):
    # Agregamos el número actual a la lista
    numeros_inversos.append(i)

# Imprimimos la lista de números en orden inverso
print(numeros_inversos)