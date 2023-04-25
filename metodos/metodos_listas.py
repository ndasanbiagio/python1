# Creando una lista con list()

lista = list(["hola", "Nico", 1, 2, 3, 4, True])

# Devuelve la cantidad de elementos de la lista
cantidad_elemento = len(lista)

# Agregando un elemento a la lista
lista.append("Jajajaja")

# Agregando un elemento a la lista en un indice especifico
lista.insert(2, "Toma")

# Agregando varios elementos a la lista
lista.extend([False, 2023])

# Eliminando un elemento de la lista(por su indice)
lista.pop(0)

# Removiendo un elemento de la lista por su valor
lista.remove("Toma")

# Elimando todos los elemento de la lista
lista.clear()

# Ordena la lista
lista.sort()

# INvertir los elemento
lista.reverse()

print(lista)
