import numpy as np

# Codigo fuente tarea 3 de Fundamentos de programacion.
# Le agregué algunas cosas...


students_grades = np.array([
    [10., 9.5, 8],
    [9., 8.5, 9.],
    [8., 6.5, 8.],
    [3.,6., 10.], # Aqui el estudiante remontó el semestre entero
    [7.,8.,8,],
    [9., 9., 9.],
    [8., 7.5, 9.5]
])

# print(students_grades)

promedios_estudiante = np.mean(students_grades, axis=1)  # of each student
# dejo afuera esta variable porque luego la usaré

def promedio_final():
    promedio_final = np.mean(promedios_estudiante)
    print(f'{promedio_final:.2f}')


def calificacion_max():
    # Interpreto que usted quiere el promedio final mas alto
    print(np.max(promedios_estudiante))

def calificacion_min():
    print(np.min(promedios_estudiante))

def cal_max_parcial1():
    cal = (students_grades[:,0])
    cal = np.max(cal)
    print(cal)

def cal_min_parcial2():
    cal_min = (students_grades[:,1])
    cal_min = np.min(cal_min)
    print(cal_min)

while True:
    print("Registro de calificaciones con NumPy\n")
    print("Opciones:")
    print("1. Obtener el promedio final del grupo")
    print("2. Obtener la calificacion mas alta del grupo")
    print("3. Obtener la calificacion mas baja del grupo")
    print("4. Obtener la calificacion mas alta del primer parcial")
    print("5. Obtener la calificacion mas baja del segundo parcial")
    print("6. Salir del programa")
    option = input("\nQue opcion eliges?: ")
    try:
        option = int(option)
        if option < 1 or option > 6:
            print("Opcion invalida")
            continue
    except ValueError:
        print("Opcion invalida")
        continue

    if option == 1:
        promedio_final()
    elif option == 2:
        calificacion_max()
    elif option == 3:
        calificacion_min()
    elif option == 4:
        cal_max_parcial1()
    elif option == 5:
        cal_min_parcial2()
    elif option == 6:
        break
