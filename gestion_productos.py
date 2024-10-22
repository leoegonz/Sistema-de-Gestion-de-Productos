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
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo productos.txt, iniciando con una lista vacía.")

def guardar_datos():
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados correctamente.")

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    cantidad = int(input("Introduce la cantidad disponible: "))
    
    productos.append({
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })
    print(f"Producto {nombre} añadido.")

def ver_productos():
    if not productos:
        print("No hay productos en la lista.")
        return
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            print("Producto encontrado. ¿Qué quieres actualizar?")
            nuevo_nombre = input("Introduce el nuevo nombre (presiona enter para no cambiar): ") or producto['nombre']
            nuevo_precio = input("Introduce el nuevo precio (presiona enter para no cambiar): ")
            nuevo_precio = float(nuevo_precio) if nuevo_precio else producto['precio']
            nueva_cantidad = input("Introduce la nueva cantidad (presiona enter para no cambiar): ")
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else producto['cantidad']
            
            producto['nombre'] = nuevo_nombre
            producto['precio'] = nuevo_precio
            producto['cantidad'] = nueva_cantidad
            print(f"Producto {nombre} actualizado.")
            return
    print(f"Producto {nombre} no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    for producto in productos:
        if producto['nombre'] == nombre:
            productos.remove(producto)
            print(f"Producto {nombre} eliminado.")
            return
    print(f"Producto {nombre} no encontrado.")

def menu():
    cargar_datos()
    
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")
        
        opcion = input("Selecciona una opción: ")
        
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
            print("Por favor, selecciona una opción válida.")

# Ejecutar el menú
menu()
