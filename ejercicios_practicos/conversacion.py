
edad_usuario = 25                     # La edad del usuario
precio_total_carrito = 150.75        # El precio total del carrito de compras
estado_inicio_sesion = "activo"      # El estado de inicio de sesión (activo o inactivo)
nombre_curso_actual = "Matemáticas"   # El nombre del curso actual
temperatura_promedio = 22.5           # La temperatura promedio registrada

def mostrar_informacion():
    print(f"Edad del Usuario: {edad_usuario} años")
    print(f"Precio Total del Carrito: ${precio_total_carrito:.2f}")
    print(f"Estado de Inicio de Sesión: {estado_inicio_sesion}")
    print(f"Nombre del Curso Actual: {nombre_curso_actual}")
    print(f"Temperatura Promedio: {temperatura_promedio} °C")

if __name__ == "__main__":
    mostrar_informacion()