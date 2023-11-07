# Cambiar el tipo de datos de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas_resueltos\\datos.csv")

# Convertir a String los datos de una columna
df['edad'] = df['edad'].astype(str)

# Mostrar el tipo de dato del primer elemento de la columna edad
print(type(df['edad'][0]))


# Reemplazando los datos "Dasanbiagio" por "Master"
df['apellido'].replace("Dasanbiagio", "Master", inplace=True)
print(df['apellido'])


# Eliminando las filas con datos faltantes
df = df.dropna()
# print(df)

# Eliminando las filas repetidas
df = df.drop_duplicates()
# print(df)


# Creando un CSV com el dataframe
df.to_csv("archivos_problemas_resueltos\\datos_limpios.csv")
