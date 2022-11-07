from diseño_clases.Orden import Orden
from diseño_clases.Producto import Producto

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 50.00)
producto3 = Producto('Zapatos', 70.00)
producto4 = Producto('Medias', 10.00)

list_productos1 = [producto1, producto2, producto3]
list_productos2 = [producto3, producto4]

order1 = Orden(list_productos1)
print(order1)
print('Total orden 1: ',order1.calcular_total())
producto5 = Producto('Bluza', 20.00)
print(order1.agregar_producto(producto5))
print(order1)

order2 = Orden(list_productos2)
print(order2)
print('Total a pagar:', order2.calcular_total())