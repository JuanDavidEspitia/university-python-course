class Producto:

    contador_productos = 0

    # Metodo inicializador o metodo constructor de la clase
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        # Autoincremental por cada instacia que se crea del objeto
        self._id_producto =  Producto.contador_productos
        # Las variables encapsuladas llevan _
        self._nombre = nombre
        self._precio = precio

    # Metodo GET
    @property
    def id_producto(self):
        return self._id_producto

    # Metodo SET
    @id_producto.setter
    def id_producto(self, id_producto):
        self._id_producto = id_producto

    # Metodo GET
    @property
    def nombre(self):
        return self._nombre

    # Metodo SET
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Metodo GET
    @property
    def precio(self):
        return self._precio

    # Metodo SET
    @precio.setter
    def precio(self, precio):
        self._precio = precio


    def __str__(self):
        return f'Id Producto {self._id_producto},  Nombre: {self._nombre}, Precio: {self._precio}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)

    producto2 = Producto('Pantalon', 50.00)
    print(producto2)
    producto2.precio = 70.00
    print(producto2.precio)

