#Funcion recursiva

def cuenta(numero):
    numero -=1
    
    if numero >0:
        print(f"-----> {numero}")
        cuenta(numero)
    
    else:
        print("Boooomm!!!!!")

cuenta(7)