# Solicitar al usuario que ingrese el salario actual
salario_actual = float(input("Ingrese el salario actual del empleado: "))

# Calcular el incremento del 8%
incremento = salario_actual * 0.08
nuevo_salario_con_incremento = salario_actual + incremento

# Calcular el descuento del 2.5%
descuento = nuevo_salario_con_incremento * 0.025
nuevo_salario_final = nuevo_salario_con_incremento - descuento

# Mostrar los resultados
print(f"Salario actual: {salario_actual:.2f}")
print(f"Incremento del 8%: {incremento:.2f}")
print(f"Nuevo salario con incremento: {nuevo_salario_con_incremento:.2f}")
print(f"Descuento del 2.5%: {descuento:.2f}")
print(f"Nuevo salario final: {nuevo_salario_final:.2f}")