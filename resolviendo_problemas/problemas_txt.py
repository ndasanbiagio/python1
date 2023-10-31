#2 listas, una con nombre otra con apellidos
nombres = ["Nico", "Nico1", "Nico2", "Nico3", "Nico4"]
apellidos = ["Diego", "Diego1", "Diego2", "Diego3", "Diego4"]

#Registrar esta informacion en un TXT de forma optima

with open("resolviendo_problemas\\nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------------\n") for n,a in zip(nombres,apellidos)]