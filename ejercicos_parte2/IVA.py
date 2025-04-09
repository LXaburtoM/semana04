# Solicitar al usuario que ingrese el precio de 3 productos
precio_producto1 = float(input("Ingrese el precio del primer producto: "))
precio_producto2 = float(input("Ingrese el precio del segundo producto: "))
precio_producto3 = float(input("Ingrese el precio del tercer producto: "))

# Calcular el subtotal
subtotal = precio_producto1 + precio_producto2 + precio_producto3

# Calcular el IVA (15%)
iva = subtotal * 0.15

# Calcular el total a pagar
total_a_pagar = subtotal + iva

# Mostrar los resultados
print(f"\nSubtotal: {subtotal:.2f}")
print(f"IVA (15%): {iva:.2f}")
print(f"Total a pagar: {total_a_pagar:.2f}")