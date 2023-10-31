import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("archivos_problemas_graficos\\salidas.csv")
print(df)


# Vamos a trabajar con sns = objetos -> Y creamos el gráfico
# Además establecemos que datos van en cada eje - por este tipo de gráfico que usamos
sns.lineplot(x="fecha", y="salidas", data=df)


# El ultimo objeto deciamos que usamos una "x" como para marcar un punto especifico
plt.plot("01-09", 19, "o")


# Mostramos el gráfico
plt.show()
