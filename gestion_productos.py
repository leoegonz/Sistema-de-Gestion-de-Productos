productos = []

def cargar_datos():
    try:
        with open('productos.txt', 'r') as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                productos.append({
                    'nombre': nombre,
                    'precio': float(precio),
                    'cantidad': int(cantidad)
                })
        print("Los datos han sido cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo productos.txt, se iniciara una lista vacía.")
    except ValueError:
        print("Error al leer el archivo, formato de datos incorrecto.")


def guardar_datos():
    try:
        with open('productos.txt', 'w') as archivo:
            for producto in productos:
                archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
        print("Los datos han sido guardados correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos: {e}")

def añadir_producto():
    # Lógica para añadir un producto
    nombre = input("Introduce el nombre del producto: ") #Un producto debe de tener nombre
    while True:
        try:
            precio = float(input("Introduce el precio del producto: ")) #Un producto debe de tener precio
            break
        except ValueError:
            print("Por favor, introduce un precio válido.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible: ")) #Cantidad para saber el stock
            break
        except ValueError:
            print("Por favor, introduce una cantidad válida.")

    productos.append({ #append para agregar los elementos a la lista
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    print(f"Producto {nombre} ha sido añadido.")

def ver_productos():
    # Lógica para ver todos los productos
    if not productos: #para asegurarme si no hay productos
        print("No hay productos en la lista.")
        return
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    # Lógica para actualizar un producto
    nombre = input("Introduce el nombre del producto que desea actualizar: ").strip()
    for producto in productos:
        if producto['nombre'] == nombre:
            print("Producto encontrado. ¿Qué desea actualizar?")
            nuevo_nombre = input("Introduce el nuevo nombre del producto (presiona tecla enter para no cambiar): ") or producto['nombre']
            
            while True:
                nuevo_precio = input("Introduce el nuevo precio del producto (presiona tecla enter para no cambiar): ")
                if nuevo_precio:
                    try:
                        nuevo_precio = float(nuevo_precio)
                        break
                    except ValueError:
                        print("Por favor, introduce un precio válido.")
                else:
                    nuevo_precio = producto['precio']
                    break
            
            while True:
                nueva_cantidad = input("Introduce la nueva cantidad (presiona tecla enter para no cambiar): ")
                if nueva_cantidad:
                    try:
                        nueva_cantidad = int(nueva_cantidad)
                        break
                    except ValueError:
                        print("Por favor, introduce una cantidad válida.")
                else:
                    nueva_cantidad = producto['cantidad']
                    break

            producto['nombre'] = nuevo_nombre
            producto['precio'] = nuevo_precio
            producto['cantidad'] = nueva_cantidad
            print(f"Producto {nombre} actualizado.")
            return
    print(f"Producto {nombre} no ha sido encontrado.")

def eliminar_producto():
    # Lógica para eliminar un producto
    nombre = input("Introduce el nombre del producto que desea eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado.")
            return
    print(f"Producto {nombre} no ha sido encontrado.")

#Menu del codigo base
def menu():
    cargar_datos()
    
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Seleccione una opción del 1 al 5: ")
        
        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, seleccione una opción válida.")

# Ejecutar el menú
menu()
