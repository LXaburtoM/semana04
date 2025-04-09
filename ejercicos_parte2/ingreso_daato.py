# Solicitar al usuario que ingrese los datos
nombre_producto = input("Ingrese el nombre del producto: ")
precio_producto = float(input("Ingrese el precio del producto: "))
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))

# Calcular el descuento
descuento = (precio_producto * porcentaje_descuento) / 100

# Calcular el precio final
precio_final = precio_producto - descuento

# Mostrar los resultados
print(f"\nNombre del producto: {nombre_producto}")
print(f"Precio final después de aplicar el descuento: {precio_final:.2f}")