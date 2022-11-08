
class DispositivoEntrada():

    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    # Metodo GET - Tipo de Entrada
    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    # Metodo SET - Tipo de Entrada
    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self._tipo_entrada = tipo_entrada

    # Metodo GET - Marca
    @property
    def marca(self):
        return self._marca

    # Metodo SET - Marca
    @marca.setter
    def marca(self, marca):
        self._marca = marca

    def __str__(self):
        return f'Tipo de Entrada: {self._tipo_entrada}, Marca: {self._marca}'

if __name__ == '__main__':

    dispo_entrada1 = DispositivoEntrada('USB', 'Lenovo')
    dispo_entrada2 = DispositivoEntrada('PCI', 'Genius')
    print(dispo_entrada1)
    print(dispo_entrada1.marca)
    print(dispo_entrada2)
    print(dispo_entrada2.marca)