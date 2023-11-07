from datetime import date

date.today()

print(date.today())


#Nuevo ejericio

lista = [21, 33, -25, 85 , -3.6, 27]

minimo = lista[0]

for x in lista:
    
    if  (x < minimo):
        
        minimo = x

print(f"El minimo es: {minimo}")