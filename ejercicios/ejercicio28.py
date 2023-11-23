def dividir(a,b):
    try:
        print("------ CARGANDO ------")
        return a/b
    
    except:
        print("No se puede dividir entre cero")
    
    else:
        print("Se pudo dividir!!!")
        
    finally:
        print("Gracias por usar mi funcion!!!")
        
dividir(5,9)