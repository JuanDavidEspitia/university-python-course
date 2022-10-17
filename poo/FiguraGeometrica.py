class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    # Los metodos GET y SET son los que se encargar de encapsular

    # Metodo GET
    @property
    def ancho(self):
        return self._ancho

    # Metodo SET
    @ancho.setter
    def ancho(self,ancho):
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    def __str__(self):
        return f'Figura Geometrica [Ancho: {self._ancho}, Alto: {self._alto} ]'


