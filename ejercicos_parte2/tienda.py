# Solicitar al usuario que ingrese el precio de compra del artículo
precio_compra = float(input("Ingrese el precio de compra del artículo: "))

# Calcular el precio de venta para obtener una ganancia del 30%
ganancia = 0.30
precio_venta = precio_compra + (precio_compra * ganancia)

# Mostrar el resultado
print(f"\nEl precio de venta para obtener una ganancia del 30% es: {precio_venta:.2f}")
