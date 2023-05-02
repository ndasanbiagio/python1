import pandas as pd
print(type(pd))

# Usando la funcion read_csv para leer el archivo CSV
# archivo = pd.read_csv("archivos\\datos.csv")
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

nombres = df["nombre"]


# Como ordenar por la edad
df_ordenado_ascendente = df.sort_values("edad")
print(df_ordenado_ascendente)


# # Ordenando en forma descendete
df_ordenado_descente = df.sort_values("edad", ascending=False)
print(df_ordenado_descente)


# # Slicing -> extraemos una parte de la lista o cadena
cadena = "0123456789"
print(cadena[2:7])


# Concatenando los 2 dataframes
df_concatenado = pd.concat([df, df2])
print(df_concatenado)

# Accediendo a la primer fila con head()
primer_fila = df.head(1)
# Mostrando la primer fila
print(primer_fila)


# Accediendo a la ultima fila con tail()
ultimas_filas = df.tail(2)
# Mostrando la primer fila
print(ultimas_filas)


# Accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape
print(filas_y_columnas_totales)


# Obteniendo data estadistica del dataframe
df_info = df.describe()
print(df_info)


# Accediendo a la edad de la fila 2
elemento_especifico_loc = df.loc[2, "edad"]
print(elemento_especifico_loc)


# Accediendo a la edad de la fila 2 con iloc
elemento_especifico_iloc = df.iloc[2, 2]
print(elemento_especifico_iloc)


# Accediendo a todos los apellidos con iloc
apellidos = df.iloc[:, 1]
print(apellidos)


# Accediendo a la fila 3 con iloc
fila_3 = df.loc[2, :]
print(fila_3)


# Accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"] > 30]
print(mayor_que_30)
