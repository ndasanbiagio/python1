altura = 1.72
peso = 93

imc = peso / (altura ** 2)

print(f"IMC : {imc}")


if (imc < 18.5):
    print("Insuficiencia ponderal")
    
elif (imc >18.5 and imc < 24.9):
    print("Normal")
    
elif (imc >= 25 and imc <= 29.9 ):
    print("Sobrepeso")
    
elif (imc >= 30 and imc <= 34.9):
    print("Obesidad Clase 1")
    
elif (imc >= 35 and imc <= 39.9):
    print("Obesidad Clase 2")
    
elif (imc >= 40 ):
    print("Obesidad Clase 3")
    