#Crea una funcion esMultiplo que reciba los dos numeros y devuelva si el primero es multiplo del segundo

# def esMultiplo(n1, n2):
    
#     resultado = False 
    
#     if ( n1 % n2 == 0 or n2 % n1 == 0):
        
#         resultado = True
    
#     return resultado

# esMultiplo(7, 100)




# Cuando el usuario ingresa los datos

# def esAlgunoMultiplo():
    
#     num1 = int (input("Ingrese un numero entero: "))

#     num2 = int (input("Ingrese un numero entero: "))
    
#     resultadoNew = False
    
#     resultadoNew = esAlgunoMultiplo( num1, num2 ) or esAlgunoMultiplo( num2, num1 )
    
#     return resultadoNew

# esAlgunoMultiplo()


#Forma Pro de hacerlo

def esMultiploPRO(n1, n2):
    
    return ( n1 % n2 == 0 )

esMultiploPRO(10,100)





#Otra opcion de hacerlo

def esMultiplo(num1, num2):
    # Verifica si num1 es múltiplo de num2
    return num1 % num2 == 0

def esAlgunoMultiplo():
    num1 = int(input("Ingrese un número entero: "))
    num2 = int(input("Ingrese otro número entero: "))
    
    resultado = esMultiplo(num1, num2) or esMultiplo(num2, num1)
    
    return resultado

# Llama a la función
resultadoFinal = esAlgunoMultiplo()

# Muestra el resultado
print("¿Alguno de los números es múltiplo del otro?", resultadoFinal)
