numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 20]

# Creando una funcion lambda para multiplicar por dos


def multiplicar_por_dos(x): return x*2

# Creando funcion comun que diga si es par o no


# Forma comun de armar una funcion -> despues la reemplazamos con LAMBDA
def es_par(num):
    if (num % 2 == 0):
        return True


# Usando FILTER con una funcion comun
numeros_pares = filter(es_par, numeros)
print(list(numeros_pares))


# Usando LAMBDA
numeros_pares2 = filter(lambda numero: numero % 2 == 0, numeros)
print(list(numeros_pares2))
