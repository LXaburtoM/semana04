
total_amount = 0.0  # Variable para almacenar el total

def calculate_total(price, quantity):
    """Función que calcula el total multiplicando el precio por la cantidad."""
    return price * quantity

# PascalCase: utilizado para clases
class ShoppingCart:
    """Clase que representa un carrito de compras."""
    
    def __init__(self):
        self.items = []  # Lista para almacenar los artículos en el carrito

    def add_item(self, price, quantity):
        """Método para agregar un artículo al carrito."""
        total = calculate_total(price, quantity)
        self.items.append(total)  # Agrega el total del artículo a la lista

    def get_total(self):
        """Método para obtener el total de todos los artículos en el carrito."""
        return sum(self.items)  # Suma todos los totales de los artículos

# SCREAMING_SNAKE_CASE: utilizado para constantes
TAX_RATE = 0.07  # Tasa de impuesto

# Ejemplo de uso
if __name__ == "__main__":
    cart = ShoppingCart()  # Crear una instancia del carrito de compras

    while True:

        price = float(input("Ingrese el precio del artículo (o -1 para terminar): "))
        if price == -1:
            break  # Salir del bucle si el usuario ingresa -1
        quantity = int(input("Ingrese la cantidad del artículo: "))

    
        cart.add_item(price, quantity)

    total_before_tax = cart.get_total()  # Obtener el total antes de impuestos
    total_with_tax = total_before_tax * (1 + TAX_RATE) 
    print(f"Total antes de impuestos: {total_before_tax:.2f}")
    print(f"Total con impuestos: {total_with_tax:.2f}")