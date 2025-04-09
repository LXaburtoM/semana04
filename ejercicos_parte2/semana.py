# Inicializar una lista para almacenar los tiempos
tiempos = []

# Solicitar los tiempos de cada día
for dia in ["lunes", "miércoles", "viernes"]:
    tiempo = float(input(f"Ingrese el tiempo en minutos que tardó en correr el {dia}: "))
    tiempos.append(tiempo)

# Calcular el tiempo promedio
tiempo_promedio = sum(tiempos) / len(tiempos)

# Mostrar el resultado
print(f"\nEl tiempo promedio que tarda en recorrer la ruta en una semana es: {tiempo_promedio:.2f} minutos")