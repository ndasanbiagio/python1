archivo_sin_leer = open("archivos\\texto_de_nico.txt", encoding="UTF-8")

# Leer archivo completo
# archivo = archivo_sin_leer.read()


# Leer linea por linea
lineas = archivo_sin_leer.readlines()

print(lineas)

# Leer una sola linea
linea = archivo_sin_leer.readline()


# Cerrar el archivo
archivo_sin_leer.close()

print(linea)
