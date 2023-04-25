# Hacemos la importacion primero va la carpeta y despues el archivo separado por " .  "
# Luego le cambiamos el nombre por m_saludar
import funciones_buenas.saludar as m_saludar

# Si hacemos el import desde una carpeta fuera de este nivel usamos -> " import sys "
import sys
print(sys.path)


# Llamamos la funcion PRINT -> carpeta de origen -> el archivo -> " . " la funcion
# Corregimos el nombre del archivo por el nuevo que acabamos de modificar -> funciones_buenas X m_saludar
# Y simplificamos la ruta (quitando el nombre del archivo)
print(m_saludar.saludar_raro("Nico"))
