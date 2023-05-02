import re

# La cadena en la que se buscata los patrones
text = "La fecha es 02/05/2023 y el telefono es +54-9-351-661-7649"

# El patron a buscar -> de la fecha -> cantidad de numeros
patter = r"\d{2}/\d{2}/\{4}"

# El texto con el que se reemplazara el patron
replacement = "Fecha Oculta"

# Reemplazar todas las apariciones del patron en la cadena de texto
new_text = re.sub(patter, replacement, text)

# Imprimir el resultado
print("Texto Modificado:", new_text)
