# Solicitar al usuario que ingrese las calificaciones
calificacion_tareas = float(input("Ingrese la calificación de tareas (0-100): "))
calificacion_examen_parcial = float(input("Ingrese la calificación del examen parcial (0-100): "))
calificacion_examen_final = float(input("Ingrese la calificación del examen final (0-100): "))

# Calcular la calificación final con ponderaciones
ponderacion_tareas = 0.30
ponderacion_examen_parcial = 0.30
ponderacion_examen_final = 0.40

calificacion_final = (calificacion_tareas * ponderacion_tareas +  calificacion_examen_parcial * ponderacion_examen_parcial +  calificacion_examen_final * ponderacion_examen_final)

# Mostrar la calificación final
print(f"\nLa calificación final del estudiante es: {calificacion_final:.2f}")