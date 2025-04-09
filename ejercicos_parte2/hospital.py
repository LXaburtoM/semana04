# Presupuesto total del hospital
presupuesto_total = float(input("Ingrese el presupuesto total del hospital: "))

# Porcentajes de distribución
porcentaje_urgencias = 0.37  # 37% para Urgencias
porcentaje_pediatria = 0.42   # 42% para Pediatría
porcentaje_traumatologia = 0.21  # 21% para Traumatología

# Calcular el presupuesto para cada área
presupuesto_urgencias = presupuesto_total * porcentaje_urgencias
presupuesto_pediatria = presupuesto_total * porcentaje_pediatria
presupuesto_traumatologia = presupuesto_total * porcentaje_traumatologia

# Mostrar los resultados
print(f"\nPresupuesto total del hospital: {presupuesto_total:.2f}")
print(f"Presupuesto para Urgencias: {presupuesto_urgencias:.2f}")
print(f"Presupuesto para Pediatría: {presupuesto_pediatria:.2f}")
print(f"Presupuesto para Traumatología: {presupuesto_traumatologia:.2f}")