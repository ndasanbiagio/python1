# Promedio de duración
otros_curos_min = 2.5
otros_curos_max = 7
otros_curos_promedio = 4
curso_nico = 1.5

# Duracion de crudos
crudo_promedio = 5
crudo_nico = 3.5


# Diferencia de duración
diferencia_con_min = 100 - (curso_nico / otros_curos_min * 100)
otros_curos_max = 100 - (curso_nico * 1000 // otros_curos_max / 10)
otros_curos_promedio = 100 - (curso_nico / otros_curos_promedio * 100)

# calculando el porcentaje de tiempo vacio removido
tiempo_vacio_promedio = 100 - otros_curos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_nico = 100 - curso_nico * 1000 // crudo_nico / 10


# Mostrando las diferencias de duracion  - Ejercicio A
print("---------------")
print(
    f'EL curso de Nico dura un {diferencia_con_min}% menos que el más rápido')
print(f'EL curso de Nico dura un {otros_curos_max}% menos que el más lento')
print(
    f'EL curso de Nico dura un {otros_curos_promedio}% menos que el promedio')
print("---------------")


# Mostrando las diferencias que se sacan  - Ejercicio B
print("---------------")
print(
    f' - Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimno el {tiempo_vacio_nico}% de tiempo vacio')
print("---------------")


# Mostrando diferencias si los cursos duraran 10 horas
print("---------------")
print(
    f'Ver 10 horas de este curso equivale a ver {otros_curos_promedio * 1000 //curso_nico / 10}')
print(
    f'Ver 10 horas de otros cursos equivale a ver {curso_nico * 100 // otros_curos_promedio / 10} horas de este curso')
print("---------------")
