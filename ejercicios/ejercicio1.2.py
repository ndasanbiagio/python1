frase = input(
    "Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")

palabras_separadas = frase.split(" ")

cantidad_de_palabras = len(palabras_separadas)


# en caso de que se tarde mas de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras > 120:
    print("Para un poco, no te pedi un testamento")


print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(
    f'Nico lo diria en {cantidad_de_palabras * 100 // 2 * 1.3 / 100} segundos en decirlos')
