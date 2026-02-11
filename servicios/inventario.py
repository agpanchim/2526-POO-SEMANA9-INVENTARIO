from modelos.producto import Producto

# Clase Inventario
# Se encarga de la gestión de los productos
class Inventario:
    def __init__(self):
        # Lista que almacena los productos del inventario
        self.productos = []

    def agregar_producto(self, producto):
        # Validar que el ID no esté repetido
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" Error: El ID ya existe.")
                return
        self.productos.append(producto)
        print(" Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        # Eliminar un producto por ID
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print(" Producto eliminado.")
                return
        print(" Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        # Actualizar cantidad y/o precio de un producto
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print(" Producto actualizado.")
                return
        print(" Producto no encontrado.")

    def buscar_producto(self, nombre):
        # Buscar productos por coincidencia parcial de nombre
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)
        return encontrados

    def listar_productos(self):
        # Mostrar todos los productos del inventario
        if not self.productos:
            print(" Inventario vacío.")
        else:
            for p in self.productos:
                print(p)

print("Inventario cargado")