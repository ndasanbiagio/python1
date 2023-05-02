import re
text = "Reemplazando todas las vocales por el asterisco"

# Como esta entre corchetes, le estamos pidiendo esas letras en cualquier orden - Sin corchetes, pasa a ser una cadena exacta
new_text = re.sub("[aeiou]", "*", text)

print(new_text)
