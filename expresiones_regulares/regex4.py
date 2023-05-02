import re

email = "example@example.com"

# son conjuntos en condiciones
pattern = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, email)

if result:
    print("Dirección de correo Válida")
else:
    print("Dirección de correo Inválida")
