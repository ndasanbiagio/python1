decimal1 = float(input("Ingresar un 1er numero decimal: "))
decimal2 = float(input("Ingresar un 2do numero decimal: "))

opcion = 1

while (opcion != 3):
    opcion = int(input("Ingresa una opcion\n1-Sumar, 2-Maximo, 3-Salir \n\n"))
    
    if (opcion == 1):
        suma = decimal1 + decimal2
        print(f"La suma es: {suma}")
        
    elif (opcion == 2):
        maximo = decimal1
        if ( decimal1 < decimal2):
            maximo = decimal2
        print(f"El maximo es: {maximo}")
    
    else:
        print("El comando es invalido")
        

