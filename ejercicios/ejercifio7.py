num = 11

while (num >= 4): #Mientras que el numero sea mayo que 4 - hago algo
    print(f"Estoy en el numero: {num}")
    num = num -1
  

#Nuevo ejericio

n = 0
while n <= 5:
    n += 1
    print(f"N vale {n}!!")
    
    
#Nuevo ejericio

numero = 10
while numero <= 5:
    numero += 1
    print(f"N vale {numero}!!")
    
else:
    print("No entro")
    
    
#Nuevo ejericio

chance = 1    
while chance <=3:
    txt = input("Escribi SI: ")
    if txt == "SI":
        print("Ok, lo conseguiste em eñ omtemtp. chance")
        break
    chance += 1
else:
    print("Has agotado tus tres intentos")
    
    
#Nuevo ejericio
numero1 = -1

while (numero1 != 0):
    print(f"Tu numero vale {numero1}\n")
    numero1 = int(input("Ingresa otro numero. con 0 para salir"))