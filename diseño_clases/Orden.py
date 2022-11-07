from diseño_clases.Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos) # Nos aseguramos que sea una  lista


    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '

        return f'Orden: {self._id_orden}, \n Productos: {productos_str} \n'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    producto2 = Producto('Pantalon', 50.00)
    producto3 = Producto('Zapatos', 70.00)
    producto4 = Producto('Medias', 10.00)

    list_productos1 = [producto1, producto2, producto3]
    list_productos2 = [producto3, producto4]

    order1 = Orden(list_productos1)
    print(order1)

    order2 = Orden(list_productos2)
    print(order2)

