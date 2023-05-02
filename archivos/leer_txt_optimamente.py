# Forma correcta de abrir con WITH OPEN y cerrar un archivo en forma de read (lectura) -> para
# poder utilizarlo al archivo usamos " as "
with open("archivos\\texto_de_nico.txt") as archivo:
    
    #Mostrando el archivo
    print(archivo.read())
