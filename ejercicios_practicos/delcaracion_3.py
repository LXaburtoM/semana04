
nombreCompletoEstudiante = "Luis Xavier"          # camelCase
numero_matricula = 123456                        # snake_case
TotalVentasDelMes = 5000.75                      # PascalCase
LIMITE_MAXIMO_INTENTOS = 3                       # SCREAMING_SNAKE_CASE
cantidadProductos = 25                            # camelCase

def mostrar_informacion():
    print(f"Nombre Completo del Estudiante: {nombreCompletoEstudiante}")
    print(f"Número de Matrícula: {numero_matricula}")
    print(f"Total de Ventas del Mes: {TotalVentasDelMes:.2f}")
    print(f"Límite Máximo de Intentos: {LIMITE_MAXIMO_INTENTOS}")
    print(f"Cantidad de Productos: {cantidadProductos}")

if __name__ == "__main__":
    mostrar_informacion()