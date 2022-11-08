from lab_mundo_pc.DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclado += 1
        self._id_teclado = Teclado.contador_teclado
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'ID Teclado: {self._id_teclado}, Tipo Entrada: {self._tipo_entrada}, Marca: {self._marca}'

if __name__ == '__main__':
    teclado1 = Teclado('Bluetooth','HP')
    print(teclado1)

    teclado2 = Teclado('Micro USB','Unit')
    print(teclado2)