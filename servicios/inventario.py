from modelos.producto import Producto
menu()
opcion = input("Seleccione una opción: ")


if opcion == "1":
# Añadir un nuevo producto
try:
id_producto = input("ID: ")
nombre = input("Nombre: ")
cantidad = int(input("Cantidad: "))
precio = float(input("Precio: "))


producto = Producto(id_producto, nombre, cantidad, precio)
inventario.agregar_producto(producto)
except ValueError:
print(" Error: datos inválidos.")


elif opcion == "2":
# Eliminar un producto por ID
id_producto = input("Ingrese el ID a eliminar: ")
inventario.eliminar_producto(id_producto)


elif opcion == "3":
# Actualizar cantidad o precio de un producto
id_producto = input("ID del producto: ")
try:
cantidad = input("Nueva cantidad (Enter para omitir): ")
precio = input("Nuevo precio (Enter para omitir): ")


inventario.actualizar_producto(
id_producto,
int(cantidad) if cantidad else None,
float(precio) if precio else None
)
except ValueError:
print(" Error en los datos.")


elif opcion == "4":
# Buscar productos por nombre
nombre = input("Nombre a buscar: ")
resultados = inventario.buscar_producto(nombre)
if resultados:
for p in resultados:
print(p)
else:
print("🔍 No se encontraron productos.")


elif opcion == "5":
# Listar todos los productos
inventario.listar_productos()


elif opcion == "6":
# Salir del sistema
print(" Saliendo del sistema...")
break


else:
print(" Opción inválida.")