# Solicitar al usuario que ingrese su nombre y apellido
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Generar el correo electrónico
correo = f"{nombre.lower()}.{apellido.lower()}@miuniversidad.edu.ni"

# Mostrar el correo electrónico generado
print(f"\nSu posible correo electrónico es: {correo}")
