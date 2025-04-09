# Solicitar al usuario que ingrese los datos necesarios
presion = float(input("Ingrese la presión en psi: "))
volumen = float(input("Ingrese el volumen en pies cúbicos: "))
temperatura = float(input("Ingrese la temperatura en grados Fahrenheit: "))

# Calcular la masa usando la fórmula proporcionada
masa = (presion * volumen) / (0.37 * (temperatura + 460))

# Mostrar el resultado
print(f"\nLa masa calculada es: {masa:.2f} unidades de masa")
