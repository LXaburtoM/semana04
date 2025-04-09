# Solicitar el nombre del trabajador
nombre_trabajador = input("Ingrese el nombre del trabajador: ")

# Solicitar las horas trabajadas
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))

# Solicitar el precio por hora
precio_por_hora = float(input("Ingrese el precio que cobra por hora: "))

# Calcular el sueldo bruto
sueldo_bruto = horas_trabajadas * precio_por_hora

# Calcular el descuento por impuesto sobre la renta (5%)
descuento_renta = sueldo_bruto * 0.05

# Calcular el salario a pagar
salario_a_pagar = sueldo_bruto - descuento_renta

# Mostrar los resultados
print(f"\nNombre del trabajador: {nombre_trabajador}")
print(f"Sueldo bruto: {sueldo_bruto:.2f}")
print(f"Descuento de renta (5%): {descuento_renta:.2f}")
print(f"Salario a pagar: {salario_a_pagar:.2f}")