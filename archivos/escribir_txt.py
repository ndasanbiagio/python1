with open('archivos\\texto_de_nico.txt', 'w') as archivo:

    # Sobre escribe el archivo
    archivo.write("Hola tito! como estas?? Aca estoy probando esto")

    #
    archivo.writelines(
        ["Hola master, como la llevas con Python???\n", "falta poco!!"])
