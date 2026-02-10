# Clase Producto
# Representa un producto dentro del sistema de inventarios
class Producto:
def __init__(self, id_producto, nombre, cantidad, precio):
# Constructor: inicializa los atributos del producto
# Se usan atributos privados para aplicar encapsulación
self._id = id_producto # Identificador único del producto
self._nombre = nombre # Nombre del producto
self._cantidad = cantidad # Cantidad disponible
self._precio = precio # Precio unitario


# ===== GETTERS =====
# Permiten acceder a los atributos privados
def get_id(self):
return self._id


def get_nombre(self):
return self._nombre


def get_cantidad(self):
return self._cantidad


def get_precio(self):
return self._precio


# ===== SETTERS =====
# Permiten modificar los atributos de forma controlada
def set_nombre(self, nombre):
self._nombre = nombre


def set_cantidad(self, cantidad):
self._cantidad = cantidad


def set_precio(self, precio):
self._precio = precio


# Método especial para mostrar el producto como texto
def __str__(self):
return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"