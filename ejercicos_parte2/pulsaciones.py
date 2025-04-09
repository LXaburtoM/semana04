# Solicitar al usuario que ingrese su edad
edad = int(input("Ingrese su edad en años: "))

# Calcular el número de pulsaciones por cada 10 segundos de ejercicio
pulsaciones = (220 - edad) / 10

# Mostrar el resultado
print(f"\nEl número de pulsaciones que debe tener por cada 10 segundos de ejercicio es: {pulsaciones:.2f} pulsaciones")
