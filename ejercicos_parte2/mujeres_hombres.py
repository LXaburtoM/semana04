# Solicitar al usuario que ingrese los datos
total_estudiantes = int(input("Ingrese el número total de estudiantes: "))
num_mujeres = int(input("Ingrese el número de mujeres: "))
num_varones = int(input("Ingrese el número de varones: "))

# Verificar que el total de estudiantes sea igual a la suma de mujeres y varones
if num_mujeres + num_varones != total_estudiantes:
    print("Error: La suma de mujeres y varones no coincide con el total de estudiantes.")
else:
    # Calcular el porcentaje de mujeres y varones
    porcentaje_mujeres = (num_mujeres / total_estudiantes) * 100
    porcentaje_varones = (num_varones / total_estudiantes) * 100

    # Mostrar los resultados
    print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
    print(f"Porcentaje de varones: {porcentaje_varones:.2f}%")