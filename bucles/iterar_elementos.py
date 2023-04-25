animales = ["gato", "perro", "loro", "cocodrilo"]  # Lista
numeros = (52, 16, 14, 72)

# Recorrriendo la lista animales - Bucle FOR
for animal in animales:
    print(f'Ahora la variable animal es igual a: {animal}')


# REcorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)


# Iterando DOS listas del mismo tamaño al mismo tiempo
for numero, animal in zip(animales, numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")


# Forma no optima de recorrer una lista con su indice
for num in range(len(numeros)):
    print(numeros[num])


for num in range(20):
    print(num)


# Forma CORRECTA de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es: {indice} y el valor es: {valor}')


# Usando el FOR/ELSE
for numero in numeros:
    print(f"ejecutandoe el último bucle, valor actual: {numero} ")
else:
    print("el bucle termino")


# Todo lo anterior funciona para listas y tuplas
