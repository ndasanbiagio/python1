import re   # importando la libreria

# Detectando un numero CBA y ocultandolo
texto = "Hola Nico, mi numero es: +54 351 661-7649"

# Condicionales
pattern = r'\+\d{2}\s\d{3}\s\d{3}-\d{4}'

reemplazo = re.sub(pattern, "(Numero oculto)", texto)

print(reemplazo)
