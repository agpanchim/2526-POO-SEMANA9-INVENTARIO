from modelos.producto import Producto
from servicios.inventario import Inventario

# Función que muestra el menú principal del sistema
def menu():
    print("\n--- SISTEMA DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir")

# Se crea una instancia del inventario
inventario = Inventario()

# Bucle principal del programa
while True:
    menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
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
        id_producto = input("Ingrese el ID a eliminar: ")
        inventario.eliminar_producto(id_producto)

    elif opcion == "3":
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
        print("Buscar por:")
        print("1. ID")
        print("2. Nombre")
        tipo = input("Seleccione una opción: ")

        if tipo == "1":
            id_producto = input("Ingrese el ID: ")
            producto = inventario.buscar_por_id(id_producto)

            if producto:
                print(producto)

            else:
                print(" Producto no encontrado.")


        elif tipo == "2":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)

            if resultados:
                for p in resultados:
                    print(p)

            else:
                print(" No se encontraron productos.")

        else:
            print(" Opción inválida.")

    elif opcion == "5":
        inventario.listar_productos()

    elif opcion == "6":
        print(" Saliendo del sistema...")
        break

    else:
        print(" Opción inválida.")
