import re
text = "Este es un ejemplo de una pagina web: https://www.google.com y tambien podemso buscar cosas"

# ? -> Si encontras esa parte mostralo, sino no pasa nada y lo muestra igual - El resto son condiciones
pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)
