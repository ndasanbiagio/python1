# Crear 2 listas, una con nombres y otra con apellidos
nombres = ["Nico", "Beni", "Ame", "Erika", "Diego"]
apellidos = ["Zarg", "Zirg", "Zerg", "Zorg", "Zurg"]


# Registrar esta informacion en un TXT de forma óptima

with open("archivos_problemas_resueltos\\nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombre: {nom}\nApellido: {ape}\n----------\n")
     for nom, ape in zip(nombres, apellidos)]
