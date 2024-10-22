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

def guardar_datos():
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Los datos han sido guardados correctamente.")

def añadir_producto():
    # Lógica para añadir un producto
    nombre = input("Introduce el nombre del producto: ") #Un producto debe de tener nombre
    precio = float(input("Introduce el precio del producto: ")) #Un producto debe de tener precio
    cantidad = int(input("Introduce la cantidad disponible: ")) #Cantidad para saber el stock
    
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
    nombre = input("Introduce el nombre del producto que desea actualizar: ") #para futura leo ver para que despliegue la lista de productos disponibles para poder seleccionar y actualizarlo directo
    for producto in productos:
        if producto['nombre'] == nombre:
            print("Producto encontrado. ¿Qué desea actualizar?")
            nuevo_nombre = input("Introduce el nuevo nombre del producto (presiona tecla enter para no cambiar): ") or producto['nombre']
            nuevo_precio = input("Introduce el nuevo precio del producto (presiona tecla enter para no cambiar): ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else producto['precio']
            nueva_cantidad = input("Introduce la nueva cantidad (presiona enter para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto['cantidad']
            
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
