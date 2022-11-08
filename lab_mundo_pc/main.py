from lab_mundo_pc.Computadora import Computadora
from lab_mundo_pc.Monitor import Monitor
from lab_mundo_pc.Raton import Raton
from lab_mundo_pc.Teclado import Teclado
from lab_mundo_pc.Orden import Orden

if __name__ == '__main__':
    teclado1 = Teclado('USB','HP')
    raton1 = Raton('USB', 'Genius')
    monitor1 = Monitor('Samsung',23)
    computadora1 = Computadora('HP', monitor1,teclado1,raton1)

    teclado2 = Teclado('Bluetooth','Lenovo')
    raton2 = Raton('USB-2', 'Lenovo')
    monitor2 = Monitor('Lenovo',24)
    computadora2 = Computadora('Lenovo', monitor2,teclado2,raton2)

    teclado3 = Teclado('Bluetooth','Logitech')
    raton3 = Raton('Bluetooth', 'Logitech')
    monitor3 = Monitor('Acer',34)
    computadora3 = Computadora('Acer', monitor3,teclado3,raton3)

    list_computadoras = [computadora1, computadora2, computadora3]
    orden1 = Orden(list_computadoras)
    print(orden1)

