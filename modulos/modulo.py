import modulo_saludar as m_saludar
# Objeto Name Space - con el AS estamnos haciendo
# referencia al modulo de otras forma O CON OTRO NOMBRE QUE QUERRAMOS - por comodidad (es una funcion)
# saludo = m_saludar.saludar = modulo_saludar.saludar

# ->Importamos SOLAMENTE UNA O MAS FUNCIONES/metodo/clase...etc y hasta se le puede cambiar el nombre de la funcion
from modulo_saludar import saludar, saludar_raro as saludar_como_mal

# Sino podemos importar todo el modulo de la siguiente manera:
from modulo_saludar import *


saludo = saludar("Diego")
saludar_raro = saludar_como_mal("Nico")

print(saludo)
print(saludar_raro)

print(type(m_saludar))


print(__name__)
