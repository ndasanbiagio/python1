import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\dispersion.csv")

# Creando el grafico
sns.scatterplot(x="dinero", y="tiempo", data=df)

# Mostrando el grafico
plt.show()
