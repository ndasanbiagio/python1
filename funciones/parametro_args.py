# Forma NO OPTIMA de sumar valores
def suma(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados = numeros_sumados + numero
    return numeros_sumados


resultado = suma([5, 3, 9, 10, 20, 3])
print(resultado)


# Forma OPTIMA - utilizando el operador * como argumento *ARGS
def suma_nueva(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: { sum(numeros)} "


resultado_nuevo = suma_nueva("Nico", 5, 3, 9, 10, 20, 3)
print(resultado_nuevo)


# Forma OPTIMA de sumar valores
def suma_total(numeros):
    return sum([*numeros])


resultado2 = suma_total([5, 3, 9, 10, 20, 3])
print(resultado2)
