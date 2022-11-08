from lab_mundo_pc.Monitor import Monitor
from lab_mundo_pc.Raton import Raton
from lab_mundo_pc.Teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
            Monitor: {self._monitor}
            Teclado: {self._teclado}
            Raton: {self._raton}
        '''

if __name__ == '__main__':
    teclado1 = Teclado('USB','HP')
    raton1 = Raton('USB', 'Genius')
    monitor1 = Monitor('Samsung',23)
    computadora1 = Computadora('HP', monitor1,teclado1,raton1)

    print(computadora1)

    teclado2 = Teclado('Bluetooth','Lenovo')
    raton2 = Raton('USB-2', 'Lenovo')
    monitor2 = Monitor('Lenovo',24)
    computadora2 = Computadora('Lenovo', monitor1,teclado1,raton1)

    print(computadora2)



