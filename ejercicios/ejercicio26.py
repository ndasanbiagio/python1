while(True):
    #Try es obligatorio y except
    try:
        n = float(input("Ingresa un numero: "))
        
    except:
        print("Esto no se puede castear!!!")
        
    
    #Bloque opcional
    
    else: #else se ejecuta cuando no estras al except
        print("Todo esta OK!!!")
        break
    
    finally:
        print("No paso nada")
    