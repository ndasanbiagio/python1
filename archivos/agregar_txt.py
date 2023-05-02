with open('archivos\\texto_de_nico.txt', 'a') as archivo:  # -> a = append

    # Sobre escribe el archivo
    archivo.write("Hola tito! como estas??\n" "Aca estoy probando esto")

    for i in range(5):
        archivo.write(f"\n - Linea {i+1} agregada\n")
