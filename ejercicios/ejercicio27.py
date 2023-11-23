try:
    n= float(input("Ingresa un numero divisor: "))
    5/n

except TypeError:
    print("No se puede dividir el numero entre una cadena")

except ValueError:
    print("Debes introducir una cadena que sea un numero")

except ZeroDivisionError:
    print("No se puede dividir por ceo, prueba otro numero")

except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )