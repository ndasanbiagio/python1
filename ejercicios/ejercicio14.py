jugador = {}

jugador["Nombre"] = input("Nombre del jugador: \n")

jugador["Apellido"] = input("Apellido del jugador: \n")

jugador["Edad"] = int(input("Eddad del jugador: \n"))

jugador["Precio"] = float(input("Precio del jugador: \n"))

print(jugador)

for clave in jugador:
    print(f"{clave} -------------> {jugador[clave]}")