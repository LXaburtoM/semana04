# Solicitar al usuario que ingrese los datos
total_cuenta = float(input("Ingrese el total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo, 10 para 10%): "))

# Calcular la propina
propina = (total_cuenta * porcentaje_propina) / 100

# Mostrar el resultado
print(f"\nTotal de la cuenta: {total_cuenta:.2f}")
print(f"Propina a dejar (al {porcentaje_propina}%): {propina:.2f}")