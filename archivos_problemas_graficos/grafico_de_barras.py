import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("archivos_problemas_graficos\\nico_ingresos.csv")
print(df)


# Vamos a trabajar con sns = objetos -> Y creamos el gráfico
# Además establecemos que datos van en cada eje - por este tipo de gráfico que usamos
sns.barplot(x="fuente", y="ingresos", data=df)

# Hacemos que haga la suma total de ingresos
total_ingresos = df['ingresos'].sum()

# Mostramos la suma de ingresos total
print(f"El total que gano es de: {total_ingresos} en USD ")


# Mostramos el gráfico
plt.show()
