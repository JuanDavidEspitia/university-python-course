from lab_mundo_pc.DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_raton = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_raton += 1
        self.id_raton = Raton.contador_raton
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'ID Raton: {self.id_raton}, Tipo Entrada: {self.tipo_entrada}, Marca: {self.marca}'

if __name__ == '__main__':
    raton1 = Raton('USB','Genius')
    print(raton1)

    raton2 = Raton('USB-2','Microsoft')
    print(raton2)