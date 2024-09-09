class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

class Menu:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def imprimir_menu(self):
        tammax = 0
        for item in self.productos:
            tamactual = len(str(item.id)) + len(item.nombre) + len(str(item.precio))
            if tamactual > tammax:
                tammax = tamactual
        print('-' * (int(tammax / 2 + 2)) + 'Menú' + '-' * (int(tammax / 2 + 2)))
        for item in self.productos:
            print(f"{item.id}. {item.nombre} -> RD${item.precio}")


producto1 = Producto(1, "Arroz", 50)
producto2 = Producto(2, "Habichuelas", 80)
producto3 = Producto(3, "Aceite", 300)
producto4 = Producto(4, "Pollo", 85)
producto5 = Producto(5, "Lechuga", 80)


menu = Menu()
menu.agregar_producto(producto1)
menu.agregar_producto(producto2)
menu.agregar_producto(producto3)
menu.agregar_producto(producto4)
menu.agregar_producto(producto5)

carrito = []

def imprimir_menu():
    menu.imprimir_menu()

def imprimir_factura(carrito):
    tamid = 1
    tamnombre = 1
    tamprecio = 1
    for item in carrito:
        tamidact = len(str(item['id']))
        tamnombreact = len(item['nombre'])
        tamprecioact = len(str(item['precio']))
        if tamidact > tamid:
            tamid = tamidact
        if tamnombreact > tamnombre:
            tamnombre = tamnombreact
        if tamprecioact > tamprecio:
            tamprecio = tamprecioact
    if tamid - 2 < 0:
        tamid = 1
    else:
        tamid -= 2
    if tamnombre - 6 < 0:
        tamnombre = 1
    else:
        tamnombre -= 6
    if tamprecio - 6 < 0:
        tamprecio = 1
    else:
        tamprecio -= 6
    
    subtotal = 0
    print(f"{'ID':<5}{'Nombre':<15}{'Precio':<10}{'Cantidad':<10}{'Total':<10}")
    for item in carrito:
        t_producto = item['precio'] * item['cantidad']
        subtotal += t_producto
        print(f"{item['id']:<5}{item['nombre']:<15}{item['precio']:<10}{item['cantidad']:<10}{t_producto:<10}")
    
    impuestos_t = subtotal * 0.18
    total = subtotal + impuestos_t
    print(f"\nSubtotal: RD${subtotal:.2f}")
    print(f"Impuestos (18%): RD${impuestos_t:.2f}")
    print(f"Total: RD${total:.2f}")

def agregar_al_carrito(id_producto, cantidad_1):
    for producto in menu.productos:
        if producto.id == id_producto:
            for item in carrito:
                if item['id'] == id_producto:
                    item['cantidad'] += cantidad_1
                    return
            carrito.append({'id': producto.id, 'nombre': producto.nombre, 'precio': producto.precio, 'cantidad': cantidad_1})
            return
    print("Producto no encontrado.")

def main():
    continuar = True
    while continuar:
        imprimir_menu()
        
        try:
            id_producto = int(input("Ingresa el ID del producto que quieres agregar: "))
        except ValueError:
            print("Por favor ingrese un número válido para el ID.")
            continue
        
        ids_validos = [item.id for item in menu.productos]
        if id_producto not in ids_validos:
            print("ID no es valido. Intentalo de nuevo.")
            continue
        
        try:
            cantidad_1 = int(input("Que cantidad del producto que desea agregar: "))
        except ValueError:
            print("Ingresa un número que sea valido para la cantidad.")
            continue
        
        if cantidad_1 <= 0:
            print("Cantidad no es válida. Intenta de nuevo.")
            continue

        agregar_al_carrito(id_producto, cantidad_1)

        c_respuesta = input("¿Te gustaria agregar otro producto? (s/n): ")
        if c_respuesta.lower() != 's':
            continuar = False

    imprimir_factura(carrito)

if __name__ == "__main__":
    main()
